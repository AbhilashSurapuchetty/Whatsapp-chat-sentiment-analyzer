from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Load the model and vectorizer
with open('sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Preprocessing function
def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    text = ' '.join(tokens)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([preprocessed_text]).toarray()
    prediction = model.predict(vectorized_text)
    sentiment = ['Neutral', 'Negative', 'Positive'][prediction[0]]
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
