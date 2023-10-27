# Project Proposal

Project Group : Chiranjeevi Koiloth (koiloth2)

# What is the Free Topic?

## System Description

The system I intend to develop is a conversational chatbot that leverages a Large Language Model (LLM), such as Falcon or LLama, for natural language understanding and generation. It will also incorporate a Retrieval-Augmented Generation (RAG) component to query a closed-source document database, allowing users to upload documents and interact with the chatbot through a user-friendly interface.

## Planned Approach and Technologies To Implement

1. **Large Language Model (LLM):**
    - Falcon or LLama, will serve as the conversational core of the chatbot. These models can understand and generate human-like text, making interactions with the chatbot more natural and engaging.
2. **Document Database:**
    - Set up a secure, closed-source document database that contains the documents users can query. Ensure the database is well-structured, with appropriate indexing for efficient retrieval.
3. **RAG System:**
    - Implement the Retrieval-Augmented Generation (RAG) system. This component combines the capabilities of the LLM with document retrieval. It allows the chatbot to search and extract information from the document database, providing relevant responses to user queries.
4. **User Interface (UI):**
    - Create a user-friendly web-based UI where users can interact with the chatbot. The UI should provide a conversational interface that mimics a chat-like experience. Users should be able to input queries and receive responses as if they were conversing with a human.
5. **Document Upload Functionality:**
    - Implement a feature that enables users to upload documents to the closed-source database. Ensure that the system can handle various document formats, such as PDFs, Word documents, or text files. Properly categorize and index these documents

The expected outcome is that we have the end to end ability to query a chatbot for answers over our closed source knowledge database. 

## Programming Languages to Use

- Python for the backend
- Typescript/React for the front end

## Hourly Estimates

The labels correspond to the planned approach above : 

1. 4 hours for selecting and deploying a chatbot 
2. 3 hours Using a cloud document database should take 
3. 8 hours to implement RAG backend server using Hugging Face
4. 4 hours to implement the UI 
5. 2 hours to implement doc upload functionality and indexing 

## Evaluation

For evaluating this functionality I will, use my personal document collection and upload it to the closed source knowledge base. I will then run through a pre-set queries and run manual tests to see if the chatbot is able to answer the questions correctly. 

I will use explicit feedback mechanisms to test the accuracy of the chatbot.