from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load models
reg_model = joblib.load("../regression_model.pkl")
clf_model = joblib.load("../classification_model.pkl")

# FastAPI app
app = FastAPI(title="Student Performance Prediction API")

# Define input data structure
class Student(BaseModel):
    # Add all your features here, example:
    school: str
    sex: str
    age: int
    address: str
    famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    # ... add the rest of your dataset columns
    # Make sure names match your CSV column names (excluding G1,G2,G3)

@app.post("/predict")
def predict(student: Student):
    # Convert input to dataframe
    data = pd.DataFrame([student.dict()])
    
    # Encode categorical variables like in notebook
    categorical_cols = data.select_dtypes(include=['object']).columns
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
    
    # Align columns with training data (fill missing columns with 0)
    trained_columns = reg_model.feature_names_in_
    for col in trained_columns:
        if col not in data.columns:
            data[col] = 0
    data = data[trained_columns]
    
    # Predictions
    grade_pred = reg_model.predict(data)[0]
    pass_pred = clf_model.predict(data)[0]
    pass_label = "Pass" if pass_pred == 1 else "Fail"

    return {
        "predicted_final_grade": round(grade_pred, 2),
        "predicted_pass": pass_label
    }