import pandas as pd
import numpy as np
import nltk, string
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

### Vektoriziraj ulazne podatke i istreniraj mrežu, testiraj na validacijskom setu
## Hrvojev zadatak (hrvoje_classifier_spam_4.ipnyb) riješen kroz .py file


#nltk.download("stopwords")

spam_df = pd.read_csv('data/spam.csv',encoding='ISO-8859-1')

#print(spam_df)

# TfidfVectorizer je higher-level od TfidfTransformera

# preprocessing

def obrada_teksta(poruke):
    removed_punct = [znak for znak in poruke if znak not in string.punctuation]
    removed_punct = "".join(removed_punct)

    removed_stop_w = [word for word in removed_punct.split() if word.lower() not in stopwords.words("english")]
    return removed_stop_w


spam_df = spam_df[["v1", "v2"]]

# preimenujemo kolumne - it really is that simple
spam_df.columns = ["klasa", "poruke"]

print(spam_df)

X_train, X_test, y_train, y_test = train_test_split(spam_df['poruke'], spam_df['klasa'],test_size=0.25)

# Pipeline za tranformaciju tekst
pipeline = Pipeline([
    ('bow_vectorizer', CountVectorizer(analyzer=obrada_teksta)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(X_train, y_train)
y_preds = pipeline.predict(X_test)

print(classification_report(y_test, y_preds))

