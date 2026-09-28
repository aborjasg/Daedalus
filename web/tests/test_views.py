from django.test import SimpleTestCase


class IndexViewTests(SimpleTestCase):
    def test_index_returns_control_panel(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Daedalus-Control Panel")
