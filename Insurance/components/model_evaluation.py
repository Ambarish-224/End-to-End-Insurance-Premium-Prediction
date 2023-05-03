from Insurance.predictor import ModelResolver
from Insurance.entity import config_entity,artifact_entity
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.utils import load_object
from sklearn.metrics import r2_score
import pandas  as pd
import sys,os
from Insurance.config import TARGET_COLUMN






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
            


            ## Find location for Previous Model
            transformer_path = self.model_resolver.get_latest_transformer_path()
            model_path = self.model_resolver.get_latest_model_path()
            target_encoder_path = self.model_resolver.get_latest_target_encoder_path()


            ## Previous Model 
            transformer = load_object(file_path= transformer_path)
            model = load_object(file_path= model_path)
            target_encoder = load_object(file_path= target_encoder_path)


            ## New Model
            current_transformer = load_object(file_path=self.data_transformation_artifact.transform_object_path)
            current_model = load_object(file_path=self.model_trainer_artifact.model_path)
            current_target_encoder = load_object(file_path=self.data_transformation_artifact.target_encoder_path)


            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            target_df = test_df[TARGET_COLUMN]
            y_true = target_df


            input_features_name = list(transformer.features_names_in_)
            for i in input_features_name:
                if test_df[i].dtypes =='object':
                    test_df[i] = target_encoder.fit_transform(test_df[i])


            input_arr = transformer.transform(test_df[input_features_name])
            y_pred = model.predict(input_arr)


            ## Comparison between NEW Model and Old Model

            previous_model_score = r2_score(y_true=y_true, y_pred=y_pred)


            ## Accuracy of Current Model

            input_feature_name = list(current_transformer.feature_names_in_)
            input_arr = current_transformer.transform(test_df[input_feature_name])
            y_pred = current_model.predict(input_arr)
            y_true = target_df


            current_model_score = r2_score(y_true=y_true, y_pred=y_pred)


            ## FINAL Comparisation between Both Model
            if current_model_score <= previous_model_score:
                logging.info(f"Current trained model is not better than previous model")
                raise Exception("Current model is not better than previous model")
            

            model_eval_artifact = artifact_entity.MOdelEvaluationArtifact(is_model_accepted= True,
            improved_accuracy=current_model_score - previous_model_score)

            return model_eval_artifact
                                    
        except Exception as e:
            raise InsuranceException(e,sys)


## Cloud ( AWS -> s3 bucket)
## Database -> Model Pusher
