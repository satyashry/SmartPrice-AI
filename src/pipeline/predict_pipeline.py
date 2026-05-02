import os, sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            self.model = load_object(file_path=model_path)
            self.preprocessor = load_object(file_path=preprocessor_path)
    def predict(self, features):
        try:
            data_scaled = self.preprocessor.transform(features)
            pred = self.model.predict(data_scaled)
            
            return pred
    
        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self,
        ram:int,
        storage:int,
        brand:str,
        os:str,
        graphics:str,
        processor:str ) :
        
        self.brand =brand
        self.ram = ram
        self.storage = storage
        self.graphics = graphics
        self.processor = processor
        self.os = os

    def get_data_as_dataframe (self):
        try :
              
            custom_data_input_dict = {
                   "brand":[self.brand],
                   "ram":[self.ram],
                   "storage":[self.storage],
                   "graphics": [self.graphics],
                   "processor":[self.processor],
                    "os": [self.os]
                }

            return pd.DataFrame(custom_data_input_dict)

        except  Exception as e:
            raise CustomException(e,sys)
