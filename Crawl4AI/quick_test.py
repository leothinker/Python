import requests

# Submit a crawl job
response = requests.post(
    "http://localhost:11235/crawl", json={"urls": "https://example.com", "priority": 10}
)
task_id = response.json()["task_id"]

# Continue polling until the task is complete (status="completed")
result = requests.get(f"http://localhost:11235/task/{task_id}")
