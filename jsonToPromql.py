import os
from dotenv import load_dotenv
import google.generativeai as genai

print("hi in the jsonToPromql")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
genai.configure(api_key=api_key)

for model in genai.list_models():
    print(model.name)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_solution_from_alert(alert):
    prompt = f"""
You are a DevOps troubleshooting assistant.

A critical alert has been triggered from Prometheus Alertmanager.

Here are the alert details in JSON:

{alert}

Based on this information, analyze and provide:
1. promql query with relevant metrics for the alert provided. 

Also make sure that you provide us the exact metrics that are required not any other explaination please.
    """.strip()

    try:
        response = model.generate_content(prompt)
        print(response)
        return response.text
    except Exception as e:
        return f"Error: {e}"
