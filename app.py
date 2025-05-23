import streamlit as st
import joblib
from preprocessing import clean_text

# Load the trained model
model = joblib.load("spam_classifier.pkl")

# App title
st.title("📧 Spam Email Classifier")
st.write("Enter a message below to check whether it's **Spam** or **Ham**.")

# Input text box
user_input = st.text_area("Type or paste an email message:", height=150)

# Predict
if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned_input = clean_text(user_input)
        prediction = model.predict([cleaned_input])[0]
        st.success(f"This message is predicted to be: **{prediction.upper()}** ✅" if prediction == "ham" else f"⚠️ This message is predicted to be: **{prediction.upper()}**")
