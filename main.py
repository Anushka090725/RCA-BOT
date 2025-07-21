import json
from gemini_client import get_rca_response
from email_sender import send_email

def main():
    # Simulated inputs
    with open("sample_alert.json", "r") as f:
        alert = json.load(f)[0]

    with open("sample_metrics.json", "r") as f:
        metrics = json.load(f)

    with open("sample_logs.json", "r") as f:
        logs = json.load(f)

    # Format the RCA response
    formatted_response = get_rca_response(
        alert=json.dumps(alert, indent=2),
        logs_json=json.dumps(logs, indent=2),
        metrics_json=json.dumps(metrics, indent=2)
    )
    print(formatted_response)
    # Send as email
    send_email(subject="🛠 RCA Bot Report – Service Alert", body=formatted_response)

if __name__ == "__main__":
    main()
