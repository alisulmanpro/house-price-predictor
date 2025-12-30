
# House Price Prediction

**Machine Learning project to predict house prices using real-world data from King County, USA.**

---

## **Project Overview**

This project predicts the **price of a house** based on features like bedrooms, bathrooms, living area, floors, and construction grade.  
It uses **Linear Regression and XGBoost models** to provide accurate price estimates.  

---

## **Dataset**

- Source: King County House Sales Dataset  
- Total records: 21,613  
- Features used:
  - `bedrooms` — Number of bedrooms
  - `bathrooms` — Number of bathrooms
  - `sqft_living` — Living area in square feet
  - `floors` — Number of floors
  - `grade` — Construction and design quality (1–13)
- Target variable:
  - `price` — Price of the house in USD  

---

## **Tools & Libraries**

- Python  
- pandas, numpy  
- scikit-learn (Linear Regression, Random Forest)  
- XGBoost  
- Streamlit (for web app)  

---

## **How it Works**

1. Load and clean the dataset.  
2. Perform feature selection.  
3. Split data into train and test sets.  
4. Train models: Linear Regression, Random Forest, XGBoost.  
5. Evaluate using:
   - **MAE (Mean Absolute Error)**
   - **RMSE (Root Mean Squared Error)**
   - **R² Score**
6. Deploy interactive Streamlit web app for user input.  

---

## **Model Performance**

| Model                | MAE ($)   | RMSE ($)   | R² Score |
|---------------------|-----------|-----------|----------|
| Linear Regression   | 165,353   | 260,667   | 0.55     |
| Random Forest       | 164,635   | 270,437   | 0.52     |
| XGBoost             | 155,078   | 272,058   | 0.51     |

**Observation:** Linear Regression performs best for normal houses; XGBoost has lowest MAE, showing good accuracy for average-priced houses.

---

## **Suggested Images for README**

1. **Dataset Preview / Table Screenshot**
   - Place under **Dataset** section
   - Shows first 5 rows and columns  

2. **Model Comparison Chart**
   - Place under **Model Performance** section
   - Bar chart comparing MAE, RMSE, R² for all models  

3. **Streamlit App Screenshot**
   - Place under **How it Works / Deployment** section
   - Shows input form and predicted price popup  

> *You can use your uploaded screenshot (the one you just sent) as the Streamlit app image.*

---

## **How to Run the Project**

1. Clone the repository:
```bash
git clone https://github.com/alisulmanpro/house-price-predictor.git
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run Streamlit app:
```bash
streamlit run main.py
```
