from locust import HttpLocust, TaskSet, task


# I have HTTP_PROXY set which causes 403 errors, so these need to be set
proxies = {
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080',
}


class UserTasks(TaskSet):

    @task
    def get_homepage(self):
        self.client.get("/", proxies=proxies)

    @task
    def get_health(self):
        self.client.get("/health", proxies=proxies)

    @task
    def get_info(self):
        self.client.get("/info", proxies=proxies)


class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://localhost:8080"
    min_wait = 10
    max_wait = 1000
    task_set = UserTasks
