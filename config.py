PROMETHEUS_ALERT_API = "http://<alertmanager-url>/api/v2/alerts"
PROMETHEUS_QUERY_API = "http://<prometheus-url>/api/v1/query"
ELASTICSEARCH_API = "http://<elasticsearch-url>:9200/_search"
DEV_EMAILS = ["dev1@example.com", "dev2@example.com"]
EMAIL_SENDER = "anushkaarorabusinessnext090725@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_PASSWORD = "vkfk kdbx ztwy yqln"
HARDCODED_ALERT= [
  {
    "status": "firing",
    "labels": {
      "alertname": "KubeletHighCPUUsage",
      "severity": "critical",
      "instance": "192.168.49.2:10250",
      "service": "prometheus-kube-prometheus-kubelet"
    },
    "annotations": {
      "summary": "Instance 10.0.1.24 CPU usage is above 90%",
      "description": "CPU usage is over 90% for the last 5 minutes."
    },
    "startsAt": "2025-07-24T09:37:14.144Z",
    "endsAt": "0001-01-01T00:00:00Z"
    # "generatorURL": "http://prometheus:9090/graph?g0.expr=100+-+avg+by(instance)(irate(node_cpu_seconds_total%7Bmode%3D%22idle%22%7D%5B5m%5D))+*+100&g0.tab=1"
  }
]
