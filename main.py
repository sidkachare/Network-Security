import os
import sys
import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")

os.environ["AWS_ACCESS_KEY_ID"]=AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"]=AWS_SECRET_ACCESS_KEY

import pymongo
from NetworkSecurity.Constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from NetworkSecurity.Constant.training_pipeline import DATA_INGESTION_DATABASE_NAME
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.logger.logger import logging
from NetworkSecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/', tags = ['authentication'])
async def index():
    return RedirectResponse(url = '/docs')

@app.get('/train')
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
'''    
@app.get('/predict')
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def main():
    try:
        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
'''

if __name__ == '__main__':
    #main()
    #set_env_variable(env_file_path)
    app_run(app, host = 'localhost', port = 8000)