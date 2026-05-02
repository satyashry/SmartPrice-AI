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
        original_price:int,
        discount_price:int,
        brand:str,
        os:str,
        graphics:str,
        processor:str ) :
        
        self.brand =brand
        self.ram = ram
        self.storage = storage
        self.original_price = original_price
        self.graphics = graphics
        self.processor = processor
        self.os = os
        self.discount_price = discount_price 

    def get_data_as_dataframe (self):
        try :
              
            custom_data_input_dict = {
                   "brand":[self.brand],
                   "ram":[self.ram],
                   "storage":[self.storage],
                   "original_price":[self.original_price],
                   "graphics": [self.graphics],
                   "processor":[self.processor],
                    "os": [self.os],
                    "discount_price":[self.discount_price]
                }

            return pd.DataFrame(custom_data_input_dict)

        except  Exception as e:
            raise CustomException(e,sys)
