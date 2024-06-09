from pdf_img_chatbot.models.olllama import OllamaModel
from pdf_img_chatbot.prompts.rag import RAG_PROMPT_1
from pdf_img_chatbot.vector_db.qdrant import QdrantDB
from pdf_img_chatbot.documents_loader.unstructured import UnstructuredDocumentLoader,PyPdfDocumentLoader
from langchain.prompts import PromptTemplate

import base64
from io import BytesIO
from PIL import Image


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


class ChatBot:
    def __init__(self):
        self.db = None
        self.prompt = PromptTemplate.from_template(RAG_PROMPT_1)
        self.model = OllamaModel()
        self.chatbot = self.prompt | self.model.chat_model 

    def upload_file(self, file):
        print(f'file: {file}')
        self.file = file
        self.docs = PyPdfDocumentLoader(file).loader.load_and_split()
        self.embeddings = self.model.embeddings_model
        self.db = QdrantDB(
            collection_name="pdf_img_chatbot",
            embeddings=self.embeddings,
            docs=self.docs
        ).db
        print("File uploaded successfully")
        print(f"number of documents: {len(self.docs)}")

    def get_content(self, user_input):
        if self.db is None:
            return "Please upload a file first"

        content = self.db.similarity_search(
            user_input,
            k=2
        )
        print(f"content used for this chat: {content}\n-------------------")
        return content
    
    def get_image_description(self, image_path , image_question = "Describe the image in a very detailed way"):
        pil_image = Image.open(image_path)
        img_base64 = convert_to_base64(pil_image)
        image_model = self.model.img_model.bind(images = [img_base64])
        return image_model.invoke(image_question)

    def chat(self, user_input , chat_history , content):

        response = self.chatbot.invoke(
            input = {
                "content": content,
                "chat_history": chat_history,
                "question": user_input
            }
        )


        return response
    
