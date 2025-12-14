import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# LOAD MODEL & ENCODERS
# ---------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    sex_le = joblib.load("sex_le.pkl")
    cab_le = joblib.load("cab_le.pkl")
    emb_le = joblib.load("emb_le.pkl")
    return model, sex_le, cab_le, emb_le

model, sex_le, cab_le, emb_le = load_artifacts()

# ---------------------------
# PAGE CONFIG
# ---------------------------
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
# ENCODE INPUTS
# ---------------------------
sex_enc = sex_le.transform([sex])[0]
emb_enc = emb_le.transform([embarked])[0]

# handle unseen cabin
if cabin in cab_le.classes_:
    cab_enc = cab_le.transform([cabin])[0]
else:
    cab_enc = cab_le.transform(["Unknown"])[0]

# ---------------------------
# MODEL INPUT (MATCH TRAINING ORDER)
# ---------------------------
X = pd.DataFrame(
    [[pclass, sex_enc, age, cab_enc, emb_enc]],
    columns=["Pclass", "Sex", "Age", "Cabin", "Embarked"]
)

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict"):
    pred = model.predict(X)[0]
    st.success(f"Prediction: {'SURVIVED' if pred == 1 else 'NOT SURVIVED'}")

    # survived_index = list(model.classes_).index(1)
    # prob = model.predict_proba(X)[0][survived_index]

    # if pred == 1:
    #     st.success(f"🎉 Likely to SURVIVE (Probability: {prob:.2f})")
    # else:
    #     st.error(f"❌ Likely NOT to survive (Probability: {prob:.2f})")
