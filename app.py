

import streamlit as st
import requests
import subprocess

st.title("Agentic Based game generator")

prompt=st.text_area("AI-Powered Web App/Game Generator Using Streamlit and n8n")

if st.button("Generate"):
    if prompt:
        response=requests.post(url="https://patilpatil.app.n8n.cloud/webhook/cfac4c88-fed9-4a08-9d3c-80b79a1794e6",json={"prompt":prompt})
        if response.status_code==200:
            st.write("Code Generated Successfully")

            with open("app1.py","w")as file:
                file.write(response.json()["output"].strip("```python"))

            subprocess.run(["python","app1.py"])