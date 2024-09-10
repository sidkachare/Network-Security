from NetworkSecurity.Constant.training_pipeline import SCHEMA_FILE_PATH
from NetworkSecurity.Entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from NetworkSecurity.Entity.config_entity import DataValidationConfig
from NetworkSecurity.Exception.exception import NetworkSecurityException 
from NetworkSecurity.logger.logger import logging 
from NetworkSecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingesttion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def validate_number_of_column(self, dataframe: pd.DataFrame) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def is_numerical_column_exist(self, dataframe: pd.DataFrame) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def detect_dataset_drift(self, base_df, current_df, threshold = 0.05) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.read_data()
            self.validate_number_of_column()
            self.detect_dataset_drift()
        except Exception as e:
            raise NetworkSecurityException(e, sys)