'''
from utils import getClient

import pandas as pd
import uuid
import os

df = pd.read_csv("resouces/my_portfolio.csv")

docs = []
metadatas = []
ids = []
for _, row in df.iterrows():
    docs.append(row["Techstack"])
    metadatas.append({"links": row["Links"]})
    ids.append(str(uuid.uuid4()))

print(docs)
print(metadatas)

'''
import os
from dotenv import load_dotenv
load_dotenv("E:\\GenAI_projects\\CEGT_git\\GenAI-1\\.env")


# 1. Check input company name is valid or not


from app.llm_calls import Chain
chain = Chain()

def isCompanyNameValid(company_name):
    if not company_name or company_name.isspace():
        return False
    if not company_name.isalnum() and not all(char.isspace() for char in company_name):
        return False
    if not chain.checkCompany(company_name):
        return False
    return True



company_name = input("Enter the company name: ")

if not isCompanyNameValid(company_name):
    print("Invalid company name. Please enter a valid name.")
    exit(1)



# 2. Check one engg related job posting in that company
from langchain_community.tools.tavily_search import TavilySearchResults

tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY is not set in the .env file")

tavily_search = TavilySearchResults(max_results = 1)
query = "Software Engineer related to AI or backend related jobs at" + company_name
_the_job = tavily_search.invoke(query)
_the_link = _the_job[0]["url"]
print(_the_link)