from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------- TRAINING DATA ----------------
sentences = [
    "He deposited money in the bank",
    "She withdrew cash from the bank",
    "The river overflowed the bank",
    "He sat on the river bank",
    "They opened a new bank account",
    "The bank of the river is steep"
]

labels = [
    "finance",
    "finance",
    "river",
    "river",
    "finance",
    "river"
]

# ---------------- FEATURE EXTRACTION ----------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# ---------------- TRAIN MODEL ----------------
model = MultinomialNB()
model.fit(X, labels)

# ---------------- USER INPUT ----------------
test_sentence = input("Enter a sentence: ")

# Convert input sentence to feature vector
X_test = vectorizer.transform([test_sentence])

# ---------------- PREDICTION ----------------
prediction = model.predict(X_test)

# ---------------- OUTPUT ----------------
print("\nSentence:", test_sentence)
print("Predicted Sense:", prediction[0])
