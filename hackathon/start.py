import os
import sys
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain import HuggingFaceHub
from getpass import getpass

repo_id = "tiiuae/falcon-7b"

"""
Hugging Face API config
"""

HUGGINGFACEHUB_API_TOKEN = 'your_hugging_face_key'

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# ovo je naš llm

falcon_llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.69, "max_length": 128}
)


documents = []

for file in os.listdir('docs'):
    if file.endswith('.pdf'):
        pdf_path = './docs/' + file
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

# we split the data into chunks of 1,000 characters, with an overlap
# of 200 characters between the chunks, which helps to give better results
# and contain the context of the information between chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(documents)

# we create our vectorDB, using the HuggingFaceEmbeddings tranformer to create
# embeddings from our text chunks. We set all the db information to be stored
# inside the ./data directory, so it doesn't clutter up our source files
vectordb = Chroma.from_documents(
  documents,
  embedding=HuggingFaceEmbeddings(),
  persist_directory='./data'
)
vectordb.persist()


# qa_chain = RetrievalQA.from_chain_type(
#     llm=falcon_llm,
#     retriever = vectordb.as_retriever(search_kwargs={'k': 20}),
#     return_source_documents=True
# )

document_qa = ConversationalRetrievalChain.from_llm(
     llm=falcon_llm,
     retriever = vectordb.as_retriever(search_kwargs={'k': 13}),
     return_source_documents=True,
     verbose=True
     )

"""
result = qa_chain({'query': 'What is True Positive score from January 2023. of our CNN?'})
print(result['result'])
 """

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"

chat_history = []
print(f"{yellow}---------------------------------------------------------------------------------")
print('Welcome to the DocBot. You are now ready to start interacting with your documents')
print('---------------------------------------------------------------------------------')
while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Exiting')
        sys.exit()
    if query == '':
        continue
    result = document_qa(
        {"question": query, "chat_history": chat_history})
    print(f"{white}Answer: " + result["answer"])
    print(f"{white}Query: " + result["question"])

    chat_history.append((query, result["answer"]))
