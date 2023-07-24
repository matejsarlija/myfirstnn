from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)').read()

# Make a soup
soup = BeautifulSoup(source, 'lxml')

# Extract the plain text content from paragraphs and links
documents = {}
doc_num = 1

for paragraph in soup.find_all('p'):
    documents[doc_num] = str(paragraph.text)
    doc_num += 1

for link in soup.find_all('a', href=True):
    try:
        link_source = urlopen(link['href']).read()
        link_soup = BeautifulSoup(link_source, 'lxml')
        for paragraph in link_soup.find_all('p'):
            documents[doc_num] = str(paragraph.text)
            doc_num += 1
    except:
        # If the link cannot be accessed or there is an error, skip it
        pass

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    documents[doc_num] = str(head.text)
    doc_num += 1

# Drop footnote superscripts in brackets
for doc_num, text in documents.items():
    documents[doc_num] = re.sub(r"\[.*?\]+", '', text)

# Save the documents as a JSON file
with open('documents.json', 'w', encoding='utf-8') as json_file:
    json.dump(documents, json_file, ensure_ascii=False, indent=4)

print("Text from all the links and paragraphs is saved in 'documents.json'.")
