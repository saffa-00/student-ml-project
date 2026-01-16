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

## API Usage

The API is implemented using **FastAPI**.

### Start API

```bash
cd app
uvicorn main:app --reload
