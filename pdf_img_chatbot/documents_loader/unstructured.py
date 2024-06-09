from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyPDFLoader

class UnstructuredDocumentLoader:
    def __init__(self, path):
        self.path = path
        self.loader = UnstructuredPDFLoader(path)



class PyPdfDocumentLoader:
    def __init__(self, path):
        self.path = path
        self.loader = PyPDFLoader(path)
