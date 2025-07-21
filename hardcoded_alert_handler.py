# from config import HARDCODED_ALERT
# from pprint import pprint

# def extract_keywords(alert):
#     # print(alert)
#     labels = alert.get("labels", {})
#     # print(labels)
#     annotations = alert.get("annotations", {})
#     # print(annotations)

#     keywords = {
#         "alertname": labels.get("alertname"),
#         "severity": labels.get("severity"),
#         "instance": labels.get("instance"),
#         "application": labels.get("application"),
#         "summary": annotations.get("summary"),
#         "description": annotations.get("description"),
#         "start_time": alert.get("startsAt"),
#         "end_time": alert.get("endsAt")
#     }
#     # pprint(keywords)

#     return keywords

# def test_alert_parsing():
#     for alert in HARDCODED_ALERT:
#         extracted = extract_keywords(alert)
#         print("🔍 Extracted Alert Data:")
#         for key, value in extracted.items():
#             # print(f"{key}: {value}")
#             print(f"{value}")# this will go into the input for fetching data from monitoring tools.

# if __name__ == "__main__":
#     test_alert_parsing()


# GET /api/v1/query_range?query=<promql_query>&start=<start>&end=<end>&step=<resolution>

from config import HARDCODED_ALERT
from jsonToPromql import get_solution_from_alert  # this is your Gemini file

print("hi in the hardcoded file")

def extract_keywords(alert):
    labels = alert.get("labels", {})
    annotations = alert.get("annotations", {})

    keywords = {
        "alertname": labels.get("alertname"),
        "severity": labels.get("severity"),
        "instance": labels.get("instance"),
        "application": labels.get("application"),
        "summary": annotations.get("summary"),
        "description": annotations.get("description"),
        "start_time": alert.get("startsAt"),
        "end_time": alert.get("endsAt")
    }
    print("in the extract_keywords")
    print(keywords)
    return keywords

def test_alert_parsing_and_send_to_gemini():
    for alert in HARDCODED_ALERT:
        print("test_alert_parsing_and_sned_to_gemini")
        print(alert)
        extracted = extract_keywords(alert)
        
        # You can pass either full extracted dict or convert to JSON string
        gemini_response = get_solution_from_alert(extracted)
        
        print("\n📡 Gemini Suggested PromQL Query:")
        print(gemini_response)

if __name__ == "__main__":
    test_alert_parsing_and_send_to_gemini()
