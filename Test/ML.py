from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load a sample dataset
categories = ['talk.politics.misc', 'rec.sport.hockey', 'comp.graphics', 'sci.space']
data = fetch_20newsgroups(subset='all', categories=categories)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42)

# Create a pipeline for TF-IDF vectorization followed by a MultinomialNB classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
predicted_categories = model.predict(X_test)
print(classification_report(y_test, predicted_categories, target_names=data.target_names))

