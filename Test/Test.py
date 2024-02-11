from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

# Step 1: Sample Data
emails = [
    "Win a free vacation now!",  # Spam
    "Important meeting tomorrow",  # Not Spam
    "Claim your free trial of our product",  # Spam
    "Project update: please send the slides",  # Not Spam
    "Congratulations, you've won a prize",  # Spam
    "Weekly report attached",  # Not Spam
    "Get your dream job today",  # Spam
    "Meeting minutes attached for review"  # Not Spam
]
labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1 for Spam, 0 for Not Spam

# Step 2 & 3: Preprocessing and Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vect = vectorizer.fit_transform(emails)

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vect, labels, test_size=0.25, random_state=42)

# Step 4: Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Step 5: Predict and Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
