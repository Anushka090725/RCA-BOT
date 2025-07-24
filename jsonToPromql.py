import os
from dotenv import load_dotenv
import google.generativeai as genai

print("hi in the jsonToPromql")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_solution_from_alert(alert):
    prompt = f"""
Here is an alert in JSON:
{alert}

Reply ONLY with the PromQL query to diagnose the issue. Do NOT include any explanation, intro, or emojis.
Provide the exact promql query on the basis of attributes given in the alert such as instance,pod, service, job.
 
Only valid output format:
container_cpu_usage_seconds_total{{instance="...", service="..."}} 
""".strip()
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
