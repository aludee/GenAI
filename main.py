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