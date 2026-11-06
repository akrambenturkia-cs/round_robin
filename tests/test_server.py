import unittest

from src.server import Server
from src.request import Request


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = Server(1, "Server-1")
        self.request = Request(1, "Client-1")

    def test_server_is_online(self):
        self.assertTrue(self.server.is_online)
#assertTrue is a method of the unittest.TestCase class that checks if the given expression is True. In this case, it checks if the server is online.
    def test_process_request(self):

        result = self.server.process_request(self.request)

        self.assertTrue(result)
        self.assertEqual(self.server.requests_handled, 1)

    def test_offline_server(self):

        self.server.is_online = False

        result = self.server.process_request(self.request)

        self.assertFalse(result)
        self.assertEqual(self.server.requests_handled, 0)


if __name__ == "__main__":
    unittest.main()