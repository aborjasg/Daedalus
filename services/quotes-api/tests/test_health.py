from django.test import SimpleTestCase


class HealthEndpointTests(SimpleTestCase):
    def test_health_returns_service_status(self):
        response = self.client.get("/api/v1/quotes/health")

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertSetEqual(
            set(body), {"success", "data", "errors", "correlationId"}
        )
        self.assertIs(body["success"], True)
        self.assertEqual(body["data"], {"service": "quotes-api", "status": "ok"})
        self.assertEqual(body["errors"], [])
        self.assertIsInstance(body["correlationId"], str)
        self.assertTrue(body["correlationId"])

    def test_health_rejects_non_get_requests(self):
        response = self.client.post("/api/v1/quotes/health")

        self.assertEqual(response.status_code, 405)
