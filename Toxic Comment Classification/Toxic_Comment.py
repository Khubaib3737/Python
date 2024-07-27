
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
dataset = pd.read_csv("train.csv")

# Combine all the toxic labels into a single target variable
dataset['toxic_label'] = dataset[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].max(axis=1)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(dataset['comment_text'], dataset['toxic_label'], test_size=0.3, random_state=42)

# Preprocess the text data using TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: ", accuracy)
print("Confusion Matrix: ")
print(conf_matrix)
print("Classification Report: ")
print(class_report)
