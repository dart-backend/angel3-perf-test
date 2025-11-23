import logging
from locust import HttpUser, between, task

class TempletePref(HttpUser):

    # wait_time = between(1, 2)  # Users wait between 1 and 2.5 seconds between tasks
    # wait_time = constant(0) 
        
    @task(1)
    def view_landing_page(self):
        self.client.get("/")

    def on_start(self):
        logging.info("Start running peformance tests...")

        # self.login()

    def on_stop(self):
        logging.info("Stopping performance tests.")    
    
    def login(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})