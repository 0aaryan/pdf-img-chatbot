from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

class OllamaModel:
    def __init__(
            self,
            chat_model : str = "llama3",
            img_model : str = "llava",
            embeddings_model : str = "mxbai-embed-large"
    ):
        self.chat_model = Ollama(model = chat_model)
        self.img_model = Ollama(model = img_model)
        self.embeddings_model = OllamaEmbeddings(model = embeddings_model)


