import joblib
import os,sys
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error)
from sklearn.model_selection import GridSearchCV
import numpy as np

def save_object(file_path, obj):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        joblib.dump(obj, f)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():
            para = param.get(model_name, {})

            if para:
                gs = GridSearchCV(
                    model,
                    para,
                    cv=3,
                    scoring="r2",
                    n_jobs=-1,
                    verbose=0
                )
                gs.fit(X_train, y_train)
                best_model = gs.best_estimator_
            else:
                model.fit(X_train, y_train)
                best_model = model

            best_models[model_name] = best_model

            # Predictions
            y_train_pred = best_model.predict(X_train)
            y_test_pred  = best_model.predict(X_test)

            # Metrics
            train_r2 = r2_score(y_train, y_train_pred)
            test_r2  = r2_score(y_test,  y_test_pred)
            mae      = mean_absolute_error(y_test, y_test_pred)
            rmse     = np.sqrt(mean_squared_error(y_test, y_test_pred))
            mape     = mean_absolute_percentage_error(y_test, y_test_pred)

            report[model_name] = {
                "train_r2": round(train_r2, 4),
                "test_r2":  round(test_r2,  4),
                "mae":      round(mae,       2),
                "rmse":     round(rmse,      2),
                "mape":     round(mape,      4)
            }

            print(f"✅ {model_name:<25} R²={test_r2:.3f}  MAE=₹{mae:,.0f}  RMSE=₹{rmse:,.0f}")

        return report, best_models

    except Exception as e:
        raise CustomException(e, sys)
