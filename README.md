# PDF and Image Chatbot (Local inference with Llama3, Llava, and Qdrant)

## Overview

The PDF and Image Chatbot is a Retrieval-Augmented Generation (RAG) chatbot that allows users to interact with PDF documents and images locally. The entire application, including the language models and vector database, runs locally on your machine. This chatbot leverages the following models and frameworks:
- **Chat Model:** Llama3
- **Image Model:** Llava
- **Embeddings:** mxbai-embed-large
- **Vector Database:** Qdrant

The application provides a Streamlit-based user interface where users can upload PDF documents and images, ask questions about the uploaded content, and receive detailed responses. 

## Features
- **Chat with PDF:** Upload a PDF document and ask questions about its content.
- **Image Description:** Upload an image and get a detailed description of it.
- **Local Processing:** All data processing, model inference, and vector searches are performed locally.
![image](https://github.com/0aaryan/pdf-img-chatbot/assets/73797587/d3643cc6-08ac-47c1-9b44-8aac6f8c423e)

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- Poetry (a dependency management tool for Python)
- Ollama (a tool for managing and running large language models locally)

### Installation Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/0aaryan/pdf-img-chatbot/
   ```

2. **Navigate to the project directory**
   ```sh
   cd pdf-img-chatbot
   ```

3. **Set up a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install Poetry**
   ```sh
   pip install poetry
   ```

5. **Install project dependencies**
   ```sh
   poetry install
   ```

6. **Pull required models using Ollama**
   ```sh
   ollama pull mxbai-embed-large
   ollama pull llava
   ollama pull llama3
   ```

### Running the Application

To start the Streamlit user interface, run:
```sh
poetry run streamlit run app/main.py
```

This command will launch the Streamlit application in your default web browser. You will be greeted with an interface to upload your PDF documents and images.

## Usage

### Uploading a PDF Document

1. **Open the application in your web browser.**
   
   ![image](https://github.com/0aaryan/pdf-img-chatbot/assets/73797587/481dc670-679a-4511-9925-37aa6e2e9f9d)

   
2. **Upload a PDF Document:**
   - Click on "Choose a file" under the "Upload File" section in the sidebar.
   - Select your PDF document.
   - Click "Upload and chat."

3. **Start Chatting:**
   - Once the PDF is uploaded, you can type your questions in the chat input field and interact with the content of the PDF.
   
   ![image](https://github.com/0aaryan/pdf-img-chatbot/assets/73797587/d6a18f16-4d97-4803-940e-7685d92e0ac3)


### Uploading an Image

1. **Open the application in your web browser.**
   
2. **Upload an Image:**
   - Click on "Choose an image" under the "Upload File" section in the sidebar.
   - Select your image file.
   - The image will be displayed with its description generated by the chatbot.

3. **Interacting with the Image:**
   - You can also ask questions about the uploaded image in the chat input field.

   ![image](https://github.com/0aaryan/pdf-img-chatbot/assets/73797587/72756393-2571-4857-9078-e665732fe2bc)


### Clearing the Chat

- To clear the chat history and start a new session, click the "Clear chat" button in the sidebar.

## Walkthrough Video

For a comprehensive walkthrough, please refer to this [video tutorial](#) which covers the entire setup and usage process step-by-step.

## Project Structure

```
├── app
│   ├── main.py
├── pdf_img_chatbot
│   ├── chatbot.py
│   ├── documents_loader
│   │   ├── __pycache__
│   │   │   └── unstructured.cpython-312.pyc
│   │   └── unstructured.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── olllama.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-312.pyc
│   │       └── olllama.cpython-312.pyc
│   ├── prompts
│   │   ├── __pycache__
│   │   │   └── rag.cpython-312.pyc
│   │   └── rag.py
│   ├── __pycache__
│   │   ├── chatbot.cpython-312.pyc
│   │   └── __init__.cpython-312.pyc
│   └── vector_db
│       ├── __pycache__
│       │   └── qdrant.cpython-312.pyc
│       └── qdrant.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```

## Additional Notes

- Ensure that your system has sufficient resources (CPU, RAM) to handle the large models being used.
- For optimal performance, it's recommended to run the application on a machine with a dedicated GPU.
- If you encounter any issues, please refer to the official documentation of the respective tools and frameworks being used.
