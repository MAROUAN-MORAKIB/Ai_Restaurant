from langchain.chains import SequentialChain
from langchain.chains import  LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
import streamlit as st

# Assuming the token and endpoint are set in a previous cell

token = st.secrets["OPENAI_API_KEY"]
endpoint = st.secrets["OPENAI_BASE_URL"]


# Initialize Langchain's ChatOpenAI with custom base_url and api_key
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_base=endpoint,
    openai_api_key=token,
    temperature=0.7,
    max_tokens=200
)

def get_restaurant_name_items(cuisine):

    prompt_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Reply ONLY with one fancy name, nothing else."
    )
    chain_name = LLMChain(llm=llm, prompt=prompt_name, output_key ='restaurant_name')
    prompt_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for '{restaurant_name}'. Return it as comma separated."
    )
    chain_items = LLMChain(llm=llm, prompt=prompt_items, output_key = 'menu_items')

    chain = SequentialChain(
        chains=[chain_name, chain_items],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    return chain({"cuisine": cuisine})

