# Coding-Raja-Technologies-Internship
# Sentiment Analysis Web Application

## Project Description
This project is a Sentiment Analysis web application that classifies social media posts as positive, negative, or neutral. The model is trained using a dataset of labeled social media posts and utilizes Natural Language Processing (NLP) techniques to preprocess the data and extract features. The classification model is implemented using a Multinomial Naive Bayes algorithm.

## Features
- Text Preprocessing: Cleaning and tokenizing the text data.
- Feature Extraction: Converting text data into numerical features using TF-IDF.
- Model Training: Training a classification model to predict sentiment.
- Web Interface: A user-friendly web interface to input text and analyze sentiment.

## Tech Stack
- Python
- Flask
- Scikit-learn
- NLTK
- HTML/CSS/JavaScript

## Setup Instructions
Follow these steps to set up the project on your local machine.

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtual Environment (optional but recommended)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/AbhilashSurapuchetty/sentiment-analysis-webapp.git
    cd sentiment-analysis-webapp
    ```

2. **Create a Virtual Environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

### Files and Directories
- `app.py`: The main Flask application file.
- `model.py`: The file containing the code for training and saving the model.
- `train.csv`: The dataset used for training the model.
- `model.pkl`: The pickled trained model.
- `vectorizer.pkl`: The pickled TF-IDF vectorizer.
- `templates/`: Directory containing the HTML and CSS template files.
    - `index.html`: The main HTML file including css and javascript code.
    
### Training the Model
To retrain the model, run the `model.py` script:
```bash
python model.py