# Python imports
import json
from unittest import TestCase

# Local imports
from app import app as flask_app


class TestEmployees(TestCase):
    def test_employees(self):
        with flask_app.test_request_context(), flask_app.test_client() as client:
            # Test GET request
            assert client.get("/").status == "200 OK"

            # Test POST request
            post_request = client.post("/?first_name=Jane&last_name=Doe")
            json_data = post_request.get_json()
            assert json_data["message"] == "Employee Jane Doe has been added."

            response = client.get("/")
            json_data = response.get_json()
            assert len(json_data["employees"]) == 1

            # Test DELETE request
            client.delete("/")
            response = client.get("/")
            json_data = response.get_json()
            assert len(json_data["employees"]) == 0
