import cryptowatch as cw
import database as db
import datetime
#TODO Access API to get data
#TODO Create database tables to store data
#TODO Store Data In tables
#TODO run the service every minute

class Metric():
    def __init__(self,exchange,market):
        self.exchange = exchange
        self.market = market
        self.code = exchange + ':' + market
       

    def get_price(code: str) -> str:
        response = cw.markets.get(code)
        #print(type( response.market.price.last))
        return "{:f}".format(response.market.price.last)



    def __repr__(self):
        return f'Metric(exchange:{self.exchange}, market: {self.market}, Code: {self.code})'


engine  = db.create_engine(db.info)
db.Base.metadata.create_all(engine)
session = db.sessionmaker(bind=engine)


metric = Metric("HITBTC", "CBCETH")


ses = session()
price = get_price(metric.code)
price_point = db.PricePoint(code=metric.code, exchange= metric.exchange, market = metric.market, price=price, time=datetime.datetime.now())
ses.add(price_point)
ses.commit()
            