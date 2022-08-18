import cryptowatch as cw
import database as db
import datetime
import time
from multiprocessing import Process


class DataService():
    """Service that tracks the given metrics/coin and manages rankings"""
    def __init__(self, metric_list: list, logger = None):
        self.metric_list = metric_list
        self.engine = db.create_engine(db.info)
        self.session = db.sessionmaker(bind=self.engine)
        self.logger = logger
        if self.logger is not None:
            logger.info("Starting Data Service")

    def track_metrics(self, wait_time = config.metric_wait_interval):
        """Starts the tracking of metrics defined in an list"""
        if self.logger is not None:
            logger.info("Starting Metric Tracker...")

        while True:
            session  = self.session() # Create SQL session
            for metric in self.metric_list: # For every metric, get and save price
                price = metric.get_price(metric.code)
                price_point = db.PricePoint(code=metric.code, exchange=metric.exchange, market=metric.market, price=price, time=datetime.datetime.now())
                session.add(price_point)
            session.commit()
            time.sleep(wait_time)

    def initialize_ranking(self):
        """ Populated ranking table with initial values"""
        if self.logger is not None:
            self.logger.info("Initializing Rankings...")
        s = self.session()
        result = s.query(db.Ranking).first()

        if result is None:
            for metric in self.metric_list:
                ranking = db.Ranking(code=metric.code, exchange=metric.exchange, rank="Rank not available")
                s.add(ranking)
            s.commit()

    #TODO Create functionality for the calculate ranking
    def calculate_ranking(wait_time=ranking_wait_interval):
        if self.logger is not None:
            logger.info("Calculating Ranking...")

        time.sleep(wait_time)
        
        pass

class Metric():
    """A coin/metric to follow
    
    Fields:
        exchange: string
        market:   string
        code:     string"""
    def __init__(self,exchange: str, market: str):
        self.exchange = exchange
        self.market = market
        self.code = exchange + ':' + market
       
    def get_price(self, code: str) -> str:
        """Get Price of a metric from the cryptowatch SDK"""
        response = cw.markets.get(code)
        return "{:f}".format(response.market.price.last)

    def __repr__(self):
        return f'Metric(exchange:{self.exchange}, market: {self.market}, Code: {self.code})'
            

    


def start_service(list, logger):
    """This function starts the Data Service. It initilizes the ranking 
       data and starts two processes for the Ranking calculation and the 
       metric tracking"""
    service = DataService(list, logger)
    service.initialize_ranking()
    p1 = Process(target=service.track_metrics())
    p1.start()
    p2 = Process(target=service.calculate_ranking())
    p2.start()

        
