from Insurance.entity import artifact_entity,config_entity
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from typing import Optional
import os,sys 
from sklearn.linear_model import LinearRegression
from Insurance import utils
from sklearn.metrics import r2_score
from Insurance.predictor import ModelResolver






class ModelEvaluation:
    def __init__(self,
                 model_eval_config: config_entity.ModelEvaluationConfig,
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
                 data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                 model_trainer_artifact:artifact_entity.ModelTrainerArtifact):
        
        
        try:
            self.model_eval_config = model_eval_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()
        
        except Exception as e:
            raise InsuranceException(e,sys)
        


    def initiate_model_evaluation(self)->artifact_entity.MOdelEvaluationArtifact:
        try:
            latest_dir_path = self.model_resolver.get_latest_dir_path()

            if latest_dir_path == None:
                model_eval_artifact = artifact_entity.MOdelEvaluationArtifact(is_model_accepted= True, improved_accuracy= None)

                logging.info(f"Model evaluation artifact: {model_eval_artifact}")

                return model_eval_artifact
        except Exception as e:
            raise InsuranceException(e,sys)


