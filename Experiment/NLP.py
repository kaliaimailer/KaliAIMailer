import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if you haven't already
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# User input for text
text = input("Enter the text to analyze: ")

# Get the polarity scores of the text
scores = sid.polarity_scores(text)

# Determine the sentiment based on the compound score
if scores['compound'] >= 0.05:
    sentiment = "Positive 😊"
elif scores['compound'] <= -0.05:
    sentiment = "Negative 😔"
else:
    sentiment = "Neutral 🙂"


# Print the sentiment and scores
print("\nSentiment:", sentiment)
print("Positive:", scores['pos'])
print("Negative:", scores['neg'])
print("Neutral:", scores['neu'])
print("Compound:", scores['compound'])
