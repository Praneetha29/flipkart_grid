from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

import os
from dotenv import load_dotenv, find_dotenv
import openai

from langchain.vectorstores import Chroma
from constants import CHROMA_SETTINGS, EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY


embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME)

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

db = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings,
    client_settings=CHROMA_SETTINGS,
)
retriever = db.as_retriever()

template = """
You are an helpful AI model that checks for user compliance, system privileges and rule violation in audit logs.You are given rules and context. Go through the context to see if any part violets the rules
IMPORTANT DO NOT ANSWER WITH "As an AI model..." anytime 
IMPORTANT if you do not find any violations mention that 
IMPORTANT when you find a violation, quote it and tell how it can be fixed 
Use the following context (delimited by <ctx></ctx>), rules (delimited by <rule></rule>) the chat history (delimited by <hs></hs>):
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
<rule>
{question}
</rule>
Violations:
"""
prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=1),
    chain_type='stuff',
    retriever=retriever,
    verbose=True,
    chain_type_kwargs={
        "verbose": True,
        "prompt": prompt,
        "memory": ConversationBufferMemory(
            memory_key="history",
            input_key="question"),
    }
)

res = qa.run("how many people have the role of editor")
print(res)
