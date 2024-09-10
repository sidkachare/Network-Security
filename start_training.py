import os
import sys
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.logger.logger import logging
from NetworkSecurity.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        logging.info('Training has started')
        model_training = TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

if __name__ == '__main__':
    start_training()