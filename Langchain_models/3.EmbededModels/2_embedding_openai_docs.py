from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Ranchi is the capital of Jharkhand",
    "Tokyo is the capital of Japan"
]

result = embedding.embed_documents(documents)

print (str(result))
