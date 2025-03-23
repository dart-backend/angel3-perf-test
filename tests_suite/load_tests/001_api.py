import time
from locust import HttpUser, task
import os

class QuickstartUser(HttpUser):
    min_wait = 1000
    max_wait = 5000
        
    @task(1)
    def view_landing_page(self):
        self.client.get("/")

    @task(1)
    def view_landing_page(self):
        self.client.get("/plaintext")

    @task(1)
    def view_db_page(self):
        self.client.get("/db")

    @task(1)
    def view_fortunes_page(self):
        self.client.get("/fortunes")

#    def view_landing_page(self):
#        self.client.get("/queries")

#    def view_landing_page(self):
#        self.client.get("/update")

    def start(self):
        # self.client.post("/login", json={"username": "foo", "password": "bar"})
        self.client.get("/")
