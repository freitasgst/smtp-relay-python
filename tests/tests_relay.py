import unittest
from relay import (
    relayer_setup,
    body_composer,
    make_requests
)


class TestChecker(unittest.TestCase):
    def test_relayer_setup(self):
        secrets_file = "api.sample.txt"
        result = relayer_setup(secrets_file)
        self.assertEqual(result, "https://chat.googleapis.com/v1/spaces/AAAAA")
    
    def test_body_composer(self):
        message = "Hello, Python"
        result = body_composer(message)
        self.assertEqual(result, {"text": "Hello, Python"})
    
    def test_make_requests(self):
        url_api = "https://chat.googleapis.com/v1/spaces/AAAAA"
        body_json = {"text": "Hello, Python"}
        result = make_requests(url_api, body_json)
        self.assertEqual(result, 404)
