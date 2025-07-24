import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_rca_response(alert, logs_json, metrics_json):
    prompt = f"""
You are an SRE assistant.

Here is the alert:
{alert}

Here are the logs from EFK in JSON:
{logs_json}

Based on the above information, generate a report with the following structure:

---
Service: <service-name>
Endpoint: <endpoint>
Time: <timestamp>

Detected: <summary of what failed>
Categorized as: <application/infrastructure/network/...>

Gpt Root Cause Summary:
- <summary points>

Suggested Fix:
- <fix suggestions>

Dashboard & Logs:
- Grafana: http://grafana.local
- Kafka: http://kafka.local
- APM: http://apm.local

Notified To:
- devops@example.com
- dev-teams@example.com
---
    """.strip()

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error from Gemini: {e}"
