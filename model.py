import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from preprocessing import clean_text

# Load original + scraped data
df1 = pd.read_csv("spam dataset.csv")[['Category', 'Message']]
df1 = df1.rename(columns={'Category': 'label', 'Message': 'message'})

try:
    df2 = pd.read_csv("scraped_emails.csv")
except FileNotFoundError:
    df2 = pd.DataFrame(columns=['label', 'message'])

df = pd.concat([df1, df2], ignore_index=True)

# Clean text
df['message'] = df['message'].astype(str).apply(clean_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Build model
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print(classification_report(y_test, preds))

# Save
joblib.dump(model, "spam_classifier.pkl")
print("Model saved to spam_classifier.pkl")
