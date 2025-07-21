import os
import sys
import httpx  # <-- Import the httpx library
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

from src.exception import CustomException
from src.logger import logging
from src.prompts.sys_prompt import REMEDY_PROMPT_TEMPLATE

load_dotenv()

def generate_remedy(disease_name: str) -> str:
    """
    Generates a detailed remedy plan for a given disease name using Groq LLM.
    """
    try:
        logging.info(f"Starting remedy generation for disease: {disease_name}")

        llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama3-8b-8192"
        )

        remedy_prompt = PromptTemplate(
            input_variables=["disease_name"],
            template=REMEDY_PROMPT_TEMPLATE
        )

        remedy_chain = LLMChain(llm=llm, prompt=remedy_prompt, output_key="remedy")

        logging.info("Invoking LLM chain to generate remedy.")
        result = remedy_chain.invoke({"disease_name": disease_name})

        logging.info("Successfully generated remedy.")
        return result['remedy']

    except Exception as e:
        raise CustomException(e, sys)
