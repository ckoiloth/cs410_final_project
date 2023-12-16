import tempfile

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import langchain_faiss as db
import query_engine as q

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, Flask!'

# This function is meant to upload documents
@app.route('/upload', methods=['POST'])
def upload_pdf():
    for _, file in request.files.items():
        print(file)
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            # Save the uploaded PDF file to a temporary location
            temp_dir = tempfile.gettempdir()
            pdf_path = os.path.join(temp_dir, file.filename)
            file.save(pdf_path)
            # Save this pdf in faiss in dex
            db.saveDocument(pdf_path)
            return jsonify({'message': 'file uploaded successfully'})
        else:
            return jsonify({'error': 'Failed to upload file'})
    return jsonify({"error": None})

# This is a test endpoint to upload text only documents
@app.route("/upload-txt", methods=['POST'])
def upload_textfile():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded PDF file to a temporary location
        temp_dir = tempfile.gettempdir()
        pdf_path = os.path.join(temp_dir, file.filename)
        file.save(pdf_path)
        print(f"PDF file saved to {pdf_path}")
        # Save this pdf in faiss in dex
        db.saveDocument(pdf_path)
        return jsonify({'message': 'PDF file uploaded successfully'})
    else:
        return jsonify({'error': 'Failed to upload PDF file'})

@app.route("/conversation", methods=['POST'])
def query_based_conversation():
    return q.queryFirst(request.json.get('query'))


if __name__ == '__main__':
    app.run(debug=True)
