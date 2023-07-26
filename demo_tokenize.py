import json
import numpy as np
import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

with open('scrubbed_wiki_data.json', 'r', encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

print(type(json_data))



for k, v in json_data.items():
    doc = nlp(v)
    sentences = list(doc.sents)

    vectors = []
    for sent in doc.sents:
        s = []
        for token in sent:
            if token.is_oov:
                #print(token.text)
                token.vector == np.ones((300,), dtype=np.float32)
            vector = token.vector
            s.append(vector)
        vectors.append(s)

wiki_df = pd.read_csv("scrubbed_wiki_data.json")
wiki_df['vectors'] = vectors

wiki_df.to_csv('wiki_vec_df.csv')
