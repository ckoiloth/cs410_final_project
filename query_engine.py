from langchain.chat_models import ChatOpenAI
from langchain import hub

import keys
import langchain_faiss as db

prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=keys.openaiKey)

## This function will concatenate all the fetched documents into one string
## which will be fed into the RAG prompt.
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

## This function kicks off the query flow
def queryFirst(query: str):
    docs = db.vectorStoreRetriever.get_relevant_documents(query)
    print(docs)
    return queryWithDocs(query, docs)


def queryWithDocs(query: str, relevant_docs):
    promptHydrated = prompt.invoke({"context": format_docs(relevant_docs), "question": query}).to_string()
    print(promptHydrated)
    return llm.invoke(promptHydrated).content
