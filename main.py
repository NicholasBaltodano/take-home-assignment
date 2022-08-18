from fastapi import FastAPI, Request, HTTPException
import config
import database as db
import logging
import data_service
import threading
from dateutil.relativedelta import relativedelta
import datetime

# Set up logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

#Set up SQL connection
engine  = db.create_engine(db.info)
session = db.sessionmaker(bind=engine)
s       = session()


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    db.Base.metadata.create_all(engine)
    thread = threading.Thread(target=data_service.start_service, args=(config.metric_list, logger))
    thread.start()

@app.get("/")
async def root(request: Request):
    return  f"Welcome to the Monte Carlo Interview Challenge! Please head over to {request.url._url}docs for API documentation"


#TODO Refactor this 
@app.get("/metric/{metric_name}")
async def get_metric_chart(metric_name: config.MetricName):
    # Raise error if not in the metricName list
    if not isinstance(metric_name, config.MetricName):
        raise HTTPException(status_code=404, detail="Metric Not Found")
    
    # Calculate X amount of hours back to filter the data
    past_time = datetime.datetime.now() - relativedelta(hours=config.hour_look_back)
    result = s.query(db.PricePoint).with_entities(db.PricePoint.time, db.PricePoint.price).order_by(db.desc(db.PricePoint.time)).filter(db.PricePoint.market == metric_name.value.upper(), db.PricePoint.time > past_time).all()
    chart_data = []
    for datapoint in result:
        chart_data.append( {"price": datapoint.price, "time":datapoint.time})
    
    # Generate Reponse 
    response = {}
    response["name"] = metric_name.value
    response["chart_data"] = chart_data
    response["rank"] = s.query(db.Ranking).with_entities(db.Ranking.rank).filter(db.Ranking.market == metric_name.value.upper()).first()
    
    return response