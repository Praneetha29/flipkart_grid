from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate

from langchain.vectorstores import Chroma
from src.constants import CHROMA_SETTINGS, EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY


embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME)


db = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings,
    client_settings=CHROMA_SETTINGS,
)
retriever = db.as_retriever()

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer,\
just say that you don't know, don't try to make up an answer.

{context}

{history}
Question: {question}
Helpful Answer:"""

prompt = PromptTemplate(input_variables=["history", "context", "question"], template=template)

llm = OpenAI()

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt},
)

query = input()

res = qa(query)
answer= res["result"]
print(answer)