import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------------------------
# LOAD YOUR MODEL + ENCODERS
# ---------------------------
model = joblib.load("model.pkl")
cab_le = joblib.load("cab_le.pkl")
sex_le = joblib.load("sex_le.pkl")
emb_le = joblib.load("emb_le.pkl")
sur_le = joblib.load("sur_le.pkl")  # only if y was encoded

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details")

# ---------------------------
# USER INPUTS
# ---------------------------
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
cabin = st.text_input("Cabin", value="Unknown")
embarked = st.selectbox("Embarked", ["S", "C", "Q"])

# ---------------------------
# ENCODE INPUT VALUES
# ---------------------------
try:
    sex_enc = sex_le.transform([sex])[0]
except ValueError:
    st.error("Unknown sex value")
    st.stop()

try:
    emb_enc = emb_le.transform([embarked])[0]
except ValueError:
    st.error("Unknown embarked value")
    st.stop()

# Handle unseen cabin safely
if cabin in cab_le.classes_:
    cab_enc = cab_le.transform([cabin])[0]
else:
    cab_enc = cab_le.transform(["Unknown"])[0]

# ---------------------------
# CREATE MODEL INPUT (ORDER MUST MATCH TRAINING)
# ---------------------------
# ⚠️ Change order ONLY if your training order was different
input_encoded = pd.DataFrame([[
    pclass,
    sex_enc,
    age,
    cab_enc,
    emb_enc
]], columns=["Pclass", "Sex", "Age", "Cabin", "Embarked"])

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict"):
    pred = model.predict(input_encoded)[0]
    prob = model.predict_proba(input_encoded)[0][1]

    # Decode prediction if target was encoded
    if "sur_le" in locals():
        pred_label = sur_le.inverse_transform([pred])[0]
    else:
        pred_label = pred

    if pred_label == 1 or pred_label == "Survived":
        st.success(f"🎉 Likely to SURVIVE (Probability: {prob:.2f})")
    else:
        st.error(f"❌ Likely NOT to survive (Probability: {prob:.2f})")
