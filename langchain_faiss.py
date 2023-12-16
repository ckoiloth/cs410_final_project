from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader, PDFPlumberLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os

local_location = 'faiss.index'
# Load FAISS if the local location exists

## This function will initialize the FAISS vector store by looking to see if there is already a local
## location for the FAISS index. If not, it will create a new FAISS index.
## It will also save the vector store to a local location.
## The local location is 'faiss.index'.

faiss: FAISS | None = None
embeddings = HuggingFaceEmbeddings()

if os.path.exists(local_location):
    print('Loading FAISS from local location')
    faiss = FAISS.load_local(local_location, embeddings)
else:
    faiss = FAISS.from_texts(["FAISS is an important library"], embeddings)
    print('Creating FAISS index')
    faiss.save_local(local_location)


vectorStoreRetriever = faiss.as_retriever(search_type="similarity", search_kwargs={"k": 2})
# This is a vector store retriever that is able to use a similarity function based on the query


## This function will save uploaded documents by first vectorizing them
## and then adding them to the vector store.
## It will also save the vector store to a local location.
## The local location is 'faiss.index'.
def saveDocument(filepath: str):
    loader = None
    if not filepath.endswith(".pdf") and not filepath.endswith("txt"):
        raise ValueError("File type not supported. Only PDF and TXT files are supported.")

    if filepath.endswith(".txt"):
        loader = TextLoader(filepath)
    else:
        loader = PDFPlumberLoader(filepath)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(docs)
    print(docs)
    docs = [doc.page_content for doc in docs]
    faiss.add_texts(docs)
    faiss.save_local(local_location)
