import cryptowatch as cw
import database as db
import datetime
import time
#TODO Access API to get data
#TODO Create database tables to store data
#TODO Store Data In tables
#TODO run the service every minute

class Metric():
    """A coin/metric to follow
    
    Parameters:
        exchange: string
        market:   string
        code:     string"""
    def __init__(self,exchange: str, market: str):
        self.exchange = exchange
        self.market = market
        self.code = exchange + ':' + market
       

    def get_price(self, code: str) -> str:
        response = cw.markets.get(code)
        #print(type( response.market.price.last))
        print("{:f}".format(response.market.price.last), response.market.price.last)
        return "{:f}".format(response.market.price.last)

    def __repr__(self):
        return f'Metric(exchange:{self.exchange}, market: {self.market}, Code: {self.code})'


class DataService():
    """Service that tracks the given metrics/coin """
    def __init__(self, metric_list: list, logger = None):
        self.metric_list = metric_list
        self.engine = db.create_engine(db.info)
        #TODO take this out, might be needed earlier
        db.Base.metadata.create_all(self.engine)
        self.session = db.sessionmaker(bind=self.engine)
        self.logger = logger

    def track_metrics(self, wait_time = 60):
        while True:
            session  = self.session() # Create SQL session
            for metric in self.metric_list: # For every metric, get and save price
                price = metric.get_price(metric.code)
                price_point = db.PricePoint(code=metric.code, exchange=metric.exchange, market=metric.market, price=price, time=datetime.datetime.now())
                session.add(price_point)
            session.commit()
            print("sleeping")
            time.sleep(wait_time) 


# engine  = db.create_engine(db.info)
#db.Base.metadata.create_all(engine)
# session = db.sessionmaker(bind=engine)

metric = Metric("HITBTC", "CBCETH")
metric_list = []
metric_list.append(metric)

service = DataService(metric_list)
service.track_metrics(5)

# ses = session()
# price = get_price(metric.code)
# price_point = db.PricePoint(code=metric.code, exchange= metric.exchange, market = metric.market, price=price, time=datetime.datetime.now())
# ses.add(price_point)
# ses.commit()
            