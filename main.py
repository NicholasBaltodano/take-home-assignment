from fastapi import FastAPI, Request, HTTPException
import config


print(config.metric_list)
app = FastAPI()


@app.get("/")
async def root(request: Request):
    return  f"Welcome to the Monte Carlo Interview Challenge! Please head over to {request.url._url}docs for API documentation"