from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# Example dataset
texts = ["This product is great", "Worst service ever", "I love this", "Not what I expected", "Could be better", "I'm so happy with this purchase"]
sentiments = [1, 0, 1, 0, 0, 1]  # 1 for positive, 0 for negative

# Splitting dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(texts, sentiments, test_size=0.2, random_state=42)

# Creating a machine learning pipeline
pipeline = make_pipeline(TfidfVectorizer(), LinearSVC())

# Training the model
pipeline.fit(X_train, y_train)

# Evaluating the model
predictions = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

# Example of interpreting a new text
new_texts = ["I'm not satisfied with the product", "This is the best experience I've had"]
new_predictions = pipeline.predict(new_texts)
interpreted_sentiments = ["Positive" if pred == 1 else "Negative" for pred in new_predictions]
for text, sentiment in zip(new_texts, interpreted_sentiments):
    print(f"'{text}' -> {sentiment}")
