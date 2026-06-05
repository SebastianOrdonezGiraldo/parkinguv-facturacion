from locust import HttpUser, between, events, task

P95_LIMIT_MS = 300


class BillingUser(HttpUser):
    wait_time = between(0.01, 0.05)

    @task
    def calculate_fee(self):
        self.client.get("/calculate", params={"minutes": 91, "vip": "true"})


@events.quitting.add_listener
def verify_p95(environment, **kwargs):
    stats = environment.stats.total
    p95 = stats.get_response_time_percentile(0.95)
    if stats.num_requests == 0 or p95 > P95_LIMIT_MS:
        environment.process_exit_code = 1
