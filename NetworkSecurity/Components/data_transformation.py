import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from NetworkSecurity.Constant.training_pipeline import TARGET_COLUMN
from NetworkSecurity.Constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from NetworkSecurity.Entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact,
)
from NetworkSecurity.Entity.config_entity import DataTransformationConfig
from NetworkSecurity.Exception.exception import NetworkSecurityException 
from NetworkSecurity.logger.logger import logging
#from networksecurity.utils.ml_utils.model.estimator import TargetValueMapping
from NetworkSecurity.utils.main_utils.utils import save_numpy_array_data, save_object
class DataTransformation:
    def __init__(self):
        pass