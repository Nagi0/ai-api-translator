import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv("./langchainTranslator/config/.env")
api_key = os.getenv("OPENAI_API_KEY")

messages = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Esse código é um teste do framework lang-chain."),
]
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

template_messages = ChatPromptTemplate(
    [("system", "Traduza o texto a seguir para {idioma}"), ("human", "{texto}")]
)

chain = template_messages | model | parser

chain_response = chain.invoke(
    {"idioma": "japonês", "texto": "Esse código é um teste do framework lang-chain."}
)
print(chain_response)
