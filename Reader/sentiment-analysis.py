from transformers import pipeline
import os

# Function to read email content from a text file
def read_email_content(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return ""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Load a pre-trained model and tokenizer for sentiment analysis
emotion_detector = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Specify the path to your text file
file_path = 'C:/KaliAIMailer/Reader/content.txt' # Change this to the path of your text file

# Read email content from the file
email_content = read_email_content(file_path)

# Check if email content was successfully read
if email_content:
    # Detect emotion
    result = emotion_detector(email_content)
    print(result)
else:
    print("No email content to analyze.")
