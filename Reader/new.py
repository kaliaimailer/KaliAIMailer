from transformers import pipeline
import re

# Load a pre-trained model for sentiment analysis
emotion_detector = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Function to read email content from a file
def read_email_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Function to estimate reading time (assuming an average reading speed of 200 words/minute)
def estimate_reading_time(text):
    words = text.split()
    word_count = len(words)
    reading_time_minutes = round(word_count / 200, 2)
    return reading_time_minutes

# Function to check if email content is professional
def is_professional(text):
    # List of keywords often found in professional emails
    professional_keywords = ['regards', 'sincerely', 'thank you', 'best', 'yours faithfully']
    # Simple heuristic: email is considered professional if it contains any of the professional keywords
    return any(keyword in text.lower() for keyword in professional_keywords)

# Main program
if __name__ == "__main__":
    # Specify the path to your email content file
    filename = "C:/KaliAIMailer/Reader/content.txt"
    
    # Read email content
    email_content = read_email_content(filename)
    
    # Detect emotion
    emotion_result = emotion_detector(email_content)
    print(f"Emotion: {emotion_result}")

    # Estimate how the email content feels
    # This is a simplification; real feelings would require more nuanced analysis
    dominant_emotion = emotion_result[0]['label']
    feeling = "positive" if dominant_emotion == "POSITIVE" else "negative"
    print(f"The email content feels: {feeling}")

    # Estimate reading time
    reading_time = estimate_reading_time(email_content)
    print(f"Estimated reading time: {reading_time} minutes")

    # Check if email content is professional
    professional = is_professional(email_content)
    print(f"Is the email content professional? {'Yes' if professional else 'No'}")
