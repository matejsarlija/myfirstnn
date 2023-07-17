import pandas as pd
import numpy as np
import nltk, string
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

sentiment_df = pd.read_csv("data/dataset.txt", delimiter=";", names=["text", "label"])

print(sentiment_df)

def obrada_teksta(poruke):
    removed_punct = [znak for znak in poruke if znak not in string.punctuation]
    removed_punct = "".join(removed_punct)

    removed_stop_w = [word for word in removed_punct.split() if word.lower() not in stopwords.words("english")]
    return removed_stop_w



X_train, X_test, y_train, y_test = train_test_split(sentiment_df['text'], sentiment_df['label'],test_size=0.25)

# Pipeline za tranformaciju tekst
pipeline = Pipeline([
    ('bow_vectorizer', CountVectorizer(analyzer = obrada_teksta, binary = True)),
    ('tfidf', TfidfTransformer()),
    ('classifier', SGDClassifier(loss='hinge',
                                 penalty='l2',
                                 alpha=1e-3,
                                 random_state=42,
                                 max_iter=5,
                                 tol=None))
])

pipeline.fit(X_train, y_train)
y_preds = pipeline.predict(X_test)


print(classification_report(y_test, y_preds))

x_test = ["i am feeling bad"]
#y_pred_test = pipeline.predict()

#x_test = pipeline.transform(x_test)
y_pred_test = pipeline.predict(x_test)
print(y_pred_test)
