"""
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain.vectorstores.chroma import Chroma ##


def get_embedding_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us-east-1"
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings



embedding_function = get_embedding_function()
CHROMA_PATH = "chroma"
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
"""
from langchain_community.embeddings import OpenAIEmbeddings
openai = OpenAIEmbeddings(openai_api_key="my-api-key")


def get_embedding_function():
    embeddings = OpenAIEmbeddings()
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
