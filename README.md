
[![Hugging Face Spaces](https://img.shields.io/badge/HF%20Spaces-View%20App-blue?logo=huggingface&logoColor=white)](https://huggingface.co/spaces/sweetyseelam/bert-sentiment-imdb-app)

🎬 IMDb Movie Reviews Sentiment Analysis using Machine Learning, Deep Learning, and Explainability Tools

End-to-End NLP Pipeline with EDA, ML & LSTM Models for Business Insights


📄 **Project Overview:**

    This project performs end-to-end Sentiment Analysis on IMDb Movie Reviews and classifies them into Positive or Negative sentiments.

    It combines classical ML models (Logistic Regression, Random Forest), deep learning models (LSTM, BERT Fine-Tuning), and Explainability techniques (SHAP, LIME)..

    The goal is to identify customer satisfaction vs dissatisfaction, helping platforms like Netflix or Amazon Prime drive content recommendations, retention strategies, and marketing decisions.


📊 **Business Problem:**

    Understanding customer feedback at scale is crucial for entertainment platforms like Netflix, Amazon Prime, etc., to:

    Improve content recommendations.

    Detect dissatisfaction early.

    Enhance customer retention and satisfaction.

    Accurately classifying sentiment from millions of reviews supports data-driven business decisions.


📚**Dataset:**

Source: IMDb 50K Review Dataset - Kaggle.                         

Records: 50,000 reviews (balanced: 25K Positive, 25K Negative).                                 

*Features:*

    review: Text of the review

    sentiment: Positive or Negative


🏗️**Phases Completed:**

Phase	     Description	              Key Techniques
------------------------------------------------------------------------------------
1	    Exploratory Data Analysis	     Review Length, Sentiment Distribution

2	    Text Preprocessing	             Cleaning, Removing Stopwords, Lemmatization

3	    Machine Learning Baselines	     TF-IDF + Logistic Regression, Random Forest

4	    Deep Learning	                 LSTM Neural Network

5	    Transformer Fine-Tuning          BERT Model Fine-tuning

6	    Explainability	                 SHAP, LIME for model interpretation


🎯 **Results Summary:**

Model	               Accuracy	      Business Impact
------------------------------------------------------------------------
Logistic Regression	    89.8%	     Fast & lightweight model for basic deployment

Random Forest	        85.9%	     More complex but lower performance

LSTM	                53.4%	     High overfitting, not optimal

BERT Fine-Tuned	        93.1%	     Highest accuracy, ready for real-world deployment

✅ Logistic Regression served as a fast benchmark.

✅ BERT fine-tuning dramatically improved sentiment detection.


🧠 **Explainability Summary:**

Tool	What It Did
----    --------------------------------------------------  
SHAP	Identified top positive/negative influential words.

LIME	Provided local explanations for individual reviews.

✅ Explainability builds stakeholder trust.


📈 **Business Impact:**
        
    - Potential uplift of ~3–5% customer retention by detecting dissatisfaction early.

    - Estimated revenue protection up to $5M–$7M annually for companies like Netflix (based on average churn rates and membership costs).


## 🚀 Live App

👉 [Try the Sentiment Analysis App on Hugging Face](https://huggingface.co/spaces/sweetyseelam/bert-sentiment-imdb-app)  
[![Hugging Face Spaces](https://img.shields.io/badge/HF%20Spaces-View%20App-blue?logo=huggingface&logoColor=white)](https://huggingface.co/spaces/sweetyseelam/bert-sentiment-imdb-app)

> Note: All deployment files for Hugging Face are located in the `/bert_sentiment_space/bert-sentiment-imdb-app/` folder.


📦 **Project Files:** 

    notebooks/ → Full EDA, ML, DL, Explainability work.

    bert_sentiment_space/ → Streamlit App for Hugging Face.

    model/ → Fine-tuned BERT Model files.

    data/ → IMDb Review Sample Dataset.

    app.py → Streamlit Application Code.


⚙️ **Requirements:**

    - torch                            
    - transformers                                 
    - streamlit                                 
    - scikit-learn                                  
    - shap                                  
    - lime                                 
    - pandas                                                  
    - numpy                            
    - matplotlib                                       


**Author:**

Sweety Seelam | Business Analyst | Data Scientist aspirant

Email: sweetyseelam2@gmail.com

Github: https://github.com/SweetySeelam2/NLP_SentimentAnalysis

LinkedIn: https://www.linkedin.com/in/sweetyrao670/

Portfolio: https://sweetyseelam2.github.io/SweetySeelam.github.io/


📄 **License:**                                  

MIT License

Copyright (c) 2025 Sweety Seelam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.