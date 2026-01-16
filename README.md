# Student Performance Prediction API

## Project Overview
This project predicts **student performance** using a dataset of student demographics, family background, and education history. It includes:

- **Regression model** to predict final grade (G3)
- **Classification model** to predict whether the student will pass or fail
- A simple **FastAPI backend** to serve predictions through a REST API

This is a full **end-to-end applied ML project**, from data preprocessing and model training to deployment.

---

## Dataset
- Source: Public dataset (student performance)
- Features: 33 columns including demographics, family info, and school-related variables  
- Target:
  - `G3` → final grade (regression)  
  - `pass/fail` → whether the student passed (classification)

---

## ML Models Used

| Task            | Model                    | Notes                          |
|-----------------|-------------------------|--------------------------------|
| Regression      | Random Forest Regressor | Predict final grade            |
| Classification  | Random Forest Classifier| Predict pass/fail              |

- Models trained in **Python** using **pandas, scikit-learn**  
- Categorical variables encoded with **one-hot encoding**  
- Feature alignment ensured during API inference

---

## Model Performance

- **Regression RMSE**: 3.87  
- **Classification F1 Score**: 0.79  
- **Classification ROC-AUC**: 0.73

---

## How to Run

### **Option 1: Explore in Jupyter**
1. Open `notebooks/start_here.ipynb`  
2. Run all cells to see:
   - Data exploration
   - Feature engineering
   - Model training
   - Evaluation metrics (RMSE, F1, ROC-AUC)

### **Option 2: Run API locally (optional)**
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt


2. Start the FastAPI server:
   cd app
   uvicorn main:app --reload


3. Open API docs in browser(local only):
   http://127.0.0.1:8000/docs
   ⚠️ Note: The API link works only while running locally. To access it, start the FastAPI server on your machine first. This is not a public URL.
   

4. Test /predict endpoint by providing a JSON input below.
{
  "school": "GP",
  "sex": "F",
  "age": 17,
  "address": "U",
  "famsize": "GT3",
  "Pstatus": "T",
  "Medu": 4,
  "Fedu": 4,
  "Mjob": "teacher",
  "Fjob": "services",
  "guardian": "mother",
  "traveltime": 1,
  "studytime": 2,
  "failures": 0,
  "schoolsup": "no",
  "famsup": "yes",
  "paid": "no",
  "activities": "yes",
  "nursery": "yes",
  "higher": "yes",
  "internet": "yes",
  "romantic": "no",
  "famrel": 4,
  "freetime": 3,
  "goout": 3,
  "Dalc": 1,
  "Walc": 1,
  "health": 5,
  "absences": 4,
  "G1": 10,
  "G2": 11
}

Notes

Categorical variables were one-hot encoded.

Missing features are filled with 0 during API prediction.

Deployment is optional; the project is fully functional locally.

Demonstrates full ML workflow: data preprocessing → model training → evaluation → optional API.
