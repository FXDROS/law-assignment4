import json
from locust import HttpUser, task, between


class AppUser(HttpUser):
    wait_time = between(2, 5)

    # normal request
    @ task
    def getMahasiswa(self):
        self.client.get("/read/1906349773")

    # idempotent
    @ task
    def getMahasiswa(self):
        self.client.get("/read/1906349773/9")
