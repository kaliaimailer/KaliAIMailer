import os
from transformers import pipeline
import fitz  # For PDF handling
import pytesseract
from PIL import Image
import pandas as pd

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read professional keywords from a CSV file
def read_professional_keywords(csv_path):
    df = pd.read_csv(csv_path, header=None)
    return df[0].tolist()

# Estimate reading time assuming an average reading speed of 200 words per minute
def estimate_reading_time(text):
    word_count = len(text.split())
    return round(word_count / 200, 2)  # Returns reading time in minutes

# Check if email content is professional based on predefined keywords
def is_professional(text, keywords):
    return any(keyword.lower() in text.lower() for keyword in keywords)

# Read text from PDF file
def read_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Extract text from an image file
def read_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

# Unified function to read email content from different file types
def read_email_content(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        return read_text_from_pdf(file_path)
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return read_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format.")

# Initialize the sentiment analysis model
emotion_detector = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

if __name__ == "__main__":
    # Folder containing email content files
    folder_path = "C:/KaliAIMailer/Email Reader/email_content"  # Adjust path as needed
    # Path to the CSV file containing professional keywords
    csv_path = "C:/KaliAIMailer/Email Reader/professional_keywords.csv"

    # Read professional keywords from CSV
    professional_keywords = read_professional_keywords(csv_path)

    # Verify folder existence
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
    else:
        # Process each file in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_name}")

            try:
                email_content = read_email_content(file_path)
                emotion_result = emotion_detector(email_content)
                print(f"Emotion: {emotion_result}")
                
                # Determine the overall feel of the email content
                dominant_emotion = emotion_result[0]['label']
                feeling = "positive" if dominant_emotion == "POSITIVE" else "negative"
                print(f"The email content feels: {feeling}")

                reading_time = estimate_reading_time(email_content)
                print(f"Estimated reading time: {reading_time} minutes")

                professional = is_professional(email_content, professional_keywords)
                print(f"Is the email content professional? {'Yes' if professional else 'No'}\n")
            except ValueError as e:
                print(f"Error processing file {file_name}: {e}")














