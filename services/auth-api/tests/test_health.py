from django.test import SimpleTestCase


class HealthEndpointTests(SimpleTestCase):
    def test_health_returns_service_status(self):
        response = self.client.get("/api/v1/auth/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "service": "auth-api",
                "endpoint": "health",
                "input": "",
                "output": "OK",
                "status": 200,
            },
        )
