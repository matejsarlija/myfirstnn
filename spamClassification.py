import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

# Vektoriziraj ulazne podatke i istreniraj mrežu, testiraj na validacijskom setu

spam = pd.read_csv('data/spam.csv',encoding='ISO-8859-1')

print(spam)

# TfidfVectorizer je higher-level od TfidfTransformera
