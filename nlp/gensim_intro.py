from collections import defaultdict
import pprint
import gensim
from gensim import corpora

text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]


# create a list of stopwords
stoplist = set('for a of the and to in'.split(' '))

# preprocessing by splitting on whitespace, lowercasing and filtering stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]


# for text in texts:
#     print(text)


# count word freqs
frequency = defaultdict(int)

for text in texts:
    for token in text:
        frequency[token] += 1

# only keeping the words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

# pprint.pprint(processed_corpus)

dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

pprint.pprint(dictionary.token2id)
