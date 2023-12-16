import streamlit as st
import requests


# Function to upload file to endpoint
def upload_file_to_endpoint(file):
    # Add your file upload endpoint here
    # Example:
    upload_endpoint = "http://127.0.0.1:5000/upload"

    files = {'file': (file.name, file.getvalue(), 'multipart/form-data')}
    response = requests.post(upload_endpoint, files=files)
    return response


# Function to send user's question to another endpoint
def send_question_to_endpoint(question):
    # Add your question endpoint here
    # Example:
    try:
        question_endpoint = "http://127.0.0.1:5000/conversation"
        data = {'query': question}
        response = requests.post(question_endpoint, json=data)
    except Exception as e:
        st.error(f"Upload Error: {e}")
        return None

    return response.text


def main():
    st.title("File Upload and Question Sending App")

    # File Upload Section
    st.header("File Upload")
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'csv'])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.write("File Uploaded Successfully!")

        # Send uploaded file to an endpoint
        upload_response = upload_file_to_endpoint(uploaded_file)
        st.write("Upload Response:", upload_response.text)

    # Question Section
    st.header("Ask a Question")
    user_question = st.text_area("Enter your question here")
    if st.button("Send Question"):
        if user_question:
            # Send user's question to an endpoint
            question_response = send_question_to_endpoint(user_question)
            st.write("Response:", question_response)
        else:
            st.warning("Please enter a question")


if __name__ == "__main__":
    main()
