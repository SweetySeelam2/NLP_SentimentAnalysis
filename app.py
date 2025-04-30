# ✅ Step 1: app.py (Streamlit UI with BERT model)

import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import pandas as pd
import shap
import joblib

# Load BERT model and tokenizer
@st.cache_resource
def load_model():
    model = BertForSequenceClassification.from_pretrained("model/bert_model")
    tokenizer = BertTokenizer.from_pretrained("model/bert_model")
    return model, tokenizer

model, tokenizer = load_model()
model.eval()

# Load TF-IDF Vectorizer and Logistic Regression model for SHAP
@st.cache_resource
def load_shap_assets():
    vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
    return vectorizer

tfidf_vectorizer = load_shap_assets()

st.title("🎬 IMDb Movie Review Sentiment Analysis")
st.markdown("Analyze the sentiment of movie reviews using BERT (Phase 5) and interpret results with SHAP/LIME (Phase 6).")

review = st.text_area("✍️ Enter a movie review:", "This movie was absolutely wonderful. Great acting and plot!")

if st.button("Predict Sentiment"):
    # BERT Prediction
    inputs = tokenizer(review, return_tensors="pt", truncation=True, padding=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        label = torch.argmax(probs).item()

    st.subheader("Prediction:")
    st.success("Positive 😊" if label else "Negative 😠")
    st.write(f"Confidence: {probs[0][label].item():.2f}")

    # SHAP Explanation (TF-IDF + Logistic Regression proxy)
    st.subheader("🔍 SHAP Feature Importance (Top Words)")
    from sklearn.linear_model import LogisticRegression
    shap_explainer = shap.Explainer(LogisticRegression(), tfidf_vectorizer.transform([review]))
    shap_values = shap_explainer(tfidf_vectorizer.transform([review]))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    shap.summary_plot(shap_values, tfidf_vectorizer.transform([review]), feature_names=tfidf_vectorizer.get_feature_names_out(), max_display=10)
    st.pyplot()

st.markdown("---")
st.caption("App built using BERT, Streamlit, SHAP and Logistic Regression")
