import streamlit as st
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os, json
from dotenv import load_dotenv
from scrape_linkedin_profile import scrape_linkedin_profile
from serpapi_search_user import search_profile
import time
import re


load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

prompt_template = """You are an AI Assistant who is given the information about a person's Linkedin Profile scrapped.
You need to tell me following facts about the person which will help me in pitching the right sales pitch. the following material will be the ice breaker.

Given Informtaion: {profile_data}

Facts you need to tell me in json format:
Name:
Summary of working experience:
Industry:
Summary of education:
Location:
3 interesting facts:
Ice Breaker:
Profile Picture URL:

Do not assume anything on your own. Provide answers from the given information only.
"""
prompt = PromptTemplate(
    input_variables=["profile_data"], template=prompt_template
)

st.title("Ice Breaking Your Next Sale")
name = st.text_input("Enter the name of the person you want to Ice break with: ")
if st.button("Break the Ice"):
        try:
            with st.spinner("Let me search on the web.."):
                time.sleep(2)
                link = search_profile(name)
                if link == "No good search result found":
                    st.error("No good search result found")
                    st.stop()
            
            with st.spinner(f"I got profile for {name}, let me find relevant data..."):
                data = scrape_linkedin_profile(link)
            with st.spinner("Cool, I got the data, let me process it for your Sales needs..."):
                llm = LLMChain(llm=ChatOpenAI(model='gpt-4-1106-preview'), prompt=prompt)
            #st.spinner("Initializing LLMChain... Done!")
                res = llm.run({"profile_data":data})
            #st.write(res)
            #st.write(type(res))
            #st.write("chaning to dic")
            res = json.loads(str(res)[7:][:-3])
            #print(res)
            #st.write("chaning to dic done")
            #st.write(type(res))
            image_url = res["Profile Picture URL"]
            st.image(image_url, width=300)
            res.pop("Profile Picture URL")
            for key, value in res.items():
                st.write(f"**{key}**: {value}")

            #st.write(llm.run({"profile_data":data}))
        except Exception as e:
            st.error(e)
    

