import logging
from locust import HttpUser, between, task

class HelloWordPref(HttpUser):
    # wait_time = between(1, 2)  # Users wait between 1 and 2.5 seconds between tasks
    # wait_time = constant(0) 
        
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

    def on_start(self):
        logging.info("Start running basic peformance tests...")

        # self.login()

    def on_stop(self):
        logging.info("Stopping basic performance tests.")    

    def login(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})