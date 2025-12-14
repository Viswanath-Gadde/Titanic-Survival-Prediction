import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("titanic_pipeline.pkl")

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details")

# ---------------------------
# USER INPUTS (5 FEATURES)
# ---------------------------
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
cabin = st.text_input("Cabin", value="Unknown")
embarked = st.selectbox("Embarked", ["S", "C", "Q"])

# ---------------------------
# INPUT DATAFRAME
# ---------------------------
input_data = pd.DataFrame([{
    "Pclass": pclass,
    "Sex": sex,
    "Age": age,
    "Cabin": cabin,
    "Embarked": embarked
}])

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"🎉 Likely to SURVIVE (Probability: {probability:.2f})")
    else:
        st.error(f"❌ Likely NOT to survive (Probability: {probability:.2f})")
