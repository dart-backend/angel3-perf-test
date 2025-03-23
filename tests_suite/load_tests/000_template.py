import time
from locust import HttpUser, task
import os

class QuickstartUser(HttpUser):
    min_wait = 1000
    max_wait = 5000
        
    @task(1)
    def view_landing_page(self):
        self.client.get("/")

    def start(self):
        # self.client.post("/login", json={"username": "foo", "password": "bar"})
        self.client.get("/")
