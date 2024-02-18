import os
import pandas as pd
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Specify paths and initial setups
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Unified text processing and analysis functions
def preprocess_text(text):
    # Placeholder for text preprocessing logic
    return text

def estimate_reading_time(text):
    word_count = len(text.split())
    return round(word_count / 200, 2)  # Returns reading time in minutes

def is_professional(text, keywords):
    return any(keyword.lower() in text.lower() for keyword in keywords)

def read_text_from_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return pytesseract.image_to_string(Image.open(file_path))
    else:
        raise ValueError("Unsupported file format.")

def predict_originality(processed_text, vectorizer, tfidf_matrix):
    user_vec = vectorizer.transform([processed_text])
    similarity = cosine_similarity(user_vec, tfidf_matrix)
    max_similarity = similarity.max()
    originality_score = (1 - max_similarity) * 100
    return f"Originality Score: {originality_score:.2f}%"

def load_dataset(file_path):
    return pd.read_csv(file_path)

def predict_email(email, vectorizer, model):
    email_counts = vectorizer.transform([email])
    prediction = model.predict(email_counts)
    return prediction[0]

if __name__ == "__main__":
    # Initialize sentiment analysis, vectorizers, classifiers, and datasets
    emotion_detector = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
    
    # Load and preprocess datasets
    df_eca = pd.read_csv('C:/KaliAIMailer/Email Reader/eca_data.csv')
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_eca['email_content'])
    
    df_emails = pd.read_csv('C:/KaliAIMailer/Email Reader/inbox_and_spam_db.csv')
    X_train, X_test, y_train, y_test = train_test_split(df_emails['email'], df_emails['label'], test_size=0.25, random_state=42)
    count_vectorizer = CountVectorizer()
    X_train_counts = count_vectorizer.fit_transform(X_train)
    
    nb_classifier = MultinomialNB()
    nb_classifier.fit(X_train_counts, y_train)
    
    # Example of processing a file for sentiment analysis, reading time, etc.
    folder_path = "C:/KaliAIMailer/Email Reader/input"  # Adjust this path as needed
    professional_keywords = pd.read_csv("C:/KaliAIMailer/Email Reader/professional_keywords.csv", header=None)[0].tolist()
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            text_content = read_text_from_file(file_path)
            processed_text = preprocess_text(text_content)
            
            # Sentiment Analysis
            emotion_result = emotion_detector(processed_text)
            dominant_emotion = emotion_result[0]['label']
            feeling = "positive" if dominant_emotion == "POSITIVE" else "negative"
            print(f"Processing file: {file_name}")
            print(f"Emotion: {dominant_emotion}, The content feels: {feeling}")
            
            # Reading Time Estimate
            reading_time = estimate_reading_time(processed_text)
            print(f"Estimated reading time: {reading_time} minutes")
            
            # Professionalism Check
            professional = is_professional(processed_text, professional_keywords)
            print(f"Is the content professional? {'Yes' if professional else 'No'}")
            
            # Originality Score
            originality_score = predict_originality(processed_text, tfidf_vectorizer, tfidf_matrix)
            print(originality_score + "\n")

            new_email = processed_text 
            prediction = predict_email(new_email, count_vectorizer, nb_classifier)
            print(f'Prediction Email Content: {prediction}')

            
        except ValueError as e:
            print(f"Error processing file {file_name}: {e}")
    
    