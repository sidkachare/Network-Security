import os
import sys
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.logger.logger import logging
from NetworkSecurity.Entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from NetworkSecurity.Entity.config_entity import ModelTrainerConfig
from xgboost import XGBClassifier
from NetworkSecurity.utils.ml_utils.model.estimator import NetworkModel
from NetworkSecurity.utils.main_utils.utils import save_object, load_object
from NetworkSecurity.utils.main_utils.utils import load_numpy_array_data
class ModelTrainer:
    def __init__(self):
        pass