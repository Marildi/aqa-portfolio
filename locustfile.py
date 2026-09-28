# locustfile.py
from locust import HttpUser, between, task


class ApiUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)  # each simulated user waits 1-3 seconds between actions

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_single_post(self):
        self.client.get("/posts/1")
