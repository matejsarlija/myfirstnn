import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# https://www.kaggle.com/datasets/akash14/news-category-dataset
# Kategorije :
# 0 - Politics
# 1 - Technology
# 2 - Entertainment
# 3 - Business

# Vektoriziraj ulazne podatke i istreniraj mrežu, testiraj na validacijskom setu

news = pd.read_csv('Data_Train.csv',encoding='ISO-8859-1')