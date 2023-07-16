import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# https://www.kaggle.com/datasets/akash14/news-category-dataset
# Kategorije :
# 0 - Politics
# 1 - Technology
# 2 - Entertainment
# 3 - Business

# Vektoriziraj ulazne podatke i istreniraj mrežu, testiraj na validacijskom setu

# predict kategorija je isto CLASSIFIER in all actuality

news = pd.read_csv('news/Data_Train.csv',encoding='ISO-8859-1')

print(news)

X_train, X_test, y_train, y_test = train_test_split(news["STORY"], news["SECTION"], test_size=0.2, random_state=1)

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)

#print(vectorizer.vocabulary_)
print(y_train)

X_test_tfidf = vectorizer.transform(X_test)

classifier = SVC()

classifier.fit(X_train_tfidf, y_train)

y_pred = classifier.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print(accuracy)

print("y_test - {}".format(y_test.shape))
print("y_pred - {}".format(y_pred.shape))

# score 0.9692005242463958
# todo je i preprocessirati text unutar kolumni pa vidjeti kako će to utjecati na rezultate
# istražiti i druge metrike
