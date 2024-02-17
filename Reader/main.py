from transformers import pipeline

# Load a pre-trained model and tokenizer for sentiment analysis
emotion_detector = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Example email content
email_content = ""

# Detect emotion
result = emotion_detector(email_content)
print(result)
