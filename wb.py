import pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.embeddings import OllamaEmbeddings

def embed_func():
    embedding = OllamaEmbeddings(model='llama3.1')
    return embedding


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


loader = PyPDFLoader('purchase.pdf')
purchase_page = loader.load()
loader_1 = PyPDFLoader('remdemption.pdf')
redemption_page = loader_1.load()
