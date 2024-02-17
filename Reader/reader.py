from transformers import pipeline

# Load the sentiment analysis pipeline
emotion_detector = pipeline('sentiment-analysis')

# Function to detect emotion
def detect_emotion(text):
    results = emotion_detector(text)
    for result in results:
        print(f"Label: {result['label']}, Score: {result['score']:.2f}")

# Example usage
text = "I feel fantastic today!"
detect_emotion(text)
