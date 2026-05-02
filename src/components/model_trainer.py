import os,sys   
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import  LinearRegression,Ridge
from dataclasses import dataclass
from src.logger import logging
from src.utils import evaluate_models,save_object
from src.exception import CustomException

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer (self,train_array,test_array):
        try:
            logging.info("Splitting the Training and Testing data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            

            # Model Selection
            models = {
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBoost": XGBRegressor(),
                "KNN": KNeighborsRegressor(),
            }

            # Hyper-parameter Tuning
            params = {
                "Linear Regression" : {

                    'copy_X': [True,False], 
                    'fit_intercept': [True,False], 
                    'n_jobs': [1,5,10,15,None], 
                    'positive': [True,False]
                },

                
                "Random Forest" : {
                    'n_estimators' : [30,70,100,150,200,250],
                    'max_features' : ['sqrt','log2'],
                    'criterion':['squared_error', 'absolute_error']
                },

                'Gradient Boosting': {
                    'loss':['squared_error', 'absolute_error'],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'criterion' : ['squared_error','friedman_mse'],
                    'n_estimators': [30,70,100,150,200,250],
                    'max_features':['sqrt','log2']
                },

                'XGBoost': {
                    'n_estimators': [100, 500],           
                    'learning_rate': [0.01, 0.05, 0.1],   
                    'max_depth': [3, 6, 9],              
                    'subsample': [0.8, 1.0], 
                },

                "Ridge": {
                'alpha': [0.1, 1.0, 10.0, 100.0],
                'fit_intercept': [True, False],
                'solver': ['auto', 'cholesky', 'sag']
                },

                "KNN": {
                'n_neighbors': [3, 5, 7, 9],
                'weights': ['uniform', 'distance']
                }

            }

            model_report ,best_model = evaluate_models(
                X_train=X_train,y_train=y_train,
                X_test=X_test,y_test=y_test,
                models=models,param=params
            )

            logging.info(f"Model Report: {model_report}")

            best_model_name = max(model_report, key=lambda x: model_report[x]["test_r2"])
            best_model_score = model_report[best_model_name]["test_r2"]
            best_model_obj = best_model[best_model_name]

            logging.info(f"Best Model: {best_model_name} with R²: {best_model_score}")
            print(f"Best Model: {best_model_name} with R²: {best_model_score}")

            save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=best_model
            )

            return best_model_name,best_model_score

        except  Exception as e:
            raise CustomException(e,sys)