from fastapi import FastAPI, Request, HTTPException
import config
import database as db
import logging

# Set up logging
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)




app     = FastAPI()
engine  = db.create_engine(db.info)
session = db.sessionmaker(bind=engine)
s = session()


@app.get("/")
async def root(request: Request):
    return  f"Welcome to the Monte Carlo Interview Challenge! Please head over to {request.url._url}docs for API documentation"

@app.get("/metric/{metric_name}")
async def get_metric_chart(metric_name: config.MetricName):
    if not isinstance(metric_name, config.MetricName):
        raise HTTPException(status_code=404, detail="Metric Not Found")
    
    
  
    result = s.query(db.PricePoint).with_entities(db.PricePoint.time, db.PricePoint.price).order_by(db.desc(db.PricePoint.time)).filter(db.PricePoint.market == metric_name.value.upper()).all()
    chart_data = []
    for datapoint in result:
        chart_data.append( {"price": datapoint.price, "time":datapoint.time})
    

    response = {}
    response["name"] = metric_name.value
    response["chart_data"] = chart_data
    response["rank"] = 1
    
    return response