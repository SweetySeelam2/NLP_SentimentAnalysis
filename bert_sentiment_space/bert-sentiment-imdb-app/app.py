import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model from Hugging Face Hub
MODEL_NAME = "sweetyseelam/bert-sentiment-imdb"

@st.cache_resource
def load_model():
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
    model = BertForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

st.title("🎬 IMDb Sentiment Analysis with BERT")
st.markdown("Enter a movie review below. The model predicts whether it's **Positive** or **Negative**.")

user_input = st.text_area("Review:", height=150)

if st.button("Analyze Sentiment"):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs)

    sentiment = "Positive 😄" if pred == 1 else "Negative 😞"
    st.markdown(f"### Prediction: **{sentiment}**")
    st.markdown(f"**Confidence:** {probs[0][pred].item():.2%}")