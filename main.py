import json
import re
import time
import requests
from gemini_client import get_rca_response
from email_sender import send_email
from hardcoded_alert_handler import test_alert_parsing_and_send_to_gemini
from config import HARDCODED_ALERT
import time

PROMETHEUS_URL = "http://localhost:9090"
PROM_QUERY = test_alert_parsing_and_send_to_gemini()
STEP = 30  # in seconds
ABC = int(time.time())
DEF = ABC - 600




def query_prometheus(query, start, end, step=STEP):
    
    url = f"http://localhost:9090/api/v1/query_range?query={PROM_QUERY}&start={DEF}&end={ABC}&step={STEP}"
    print(url)
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return response.json()
        
    else:
        raise Exception(f"Prometheus query failed: {response.status_code} {response.text}")

def start_time():
    for alert in HARDCODED_ALERT:
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})

        time = {
            "start_time": alert.get("startsAt")
        }
        time["start_time"]=int(time.time()) - 600
        print(time["start_time"])
        return time["start_time"]

def end_time():
    for alert in HARDCODED_ALERT:
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})

        time = {
            "end_time": alert.get("endsAt")
        }
        time["end_time"] = int(time.time())
        print(time["end_time"])
        return time["end_time"]


def main():
    # Load alert
    with open("sample_alert.json", "r") as f:
        alert = json.load(f)[0]

    # Time range for Prometheus query (last 10 minutes)
    end_time = int(time.time())
    start_time = end_time - 600

    # Fetch metrics from Prometheus
    try:
        prometheus_response = query_prometheus(PROM_QUERY, start_time, end_time)
        print("Prometheus Response")
        print(prometheus_response)
        metrics = prometheus_response.get("data", {}).get("result", [])
    except Exception as e:
        print("Error fetching metrics:", e)
        metrics = []

    # Load logs (with safety)
    try:
        with open("sample_logs.json", "r") as f:
            logs = json.load(f)
    except Exception as e:
        print("Error reading logs:", e)
        logs = []

    # Generate RCA response
    formatted_response = get_rca_response(
        alert=json.dumps(alert, indent=2),
        logs_json=json.dumps(logs, indent=2),
        metrics_json=json.dumps(metrics, indent=2)
    )
    print(formatted_response)

    # Send RCA summary via email
    send_email(subject="🛠 RCA Bot Report – Service Alert", body=formatted_response)

if __name__ == "__main__":
    main()
