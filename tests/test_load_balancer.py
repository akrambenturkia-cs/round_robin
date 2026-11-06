import unittest

from src.server import Server
from src.load_balancer import LoadBalancer
from src.request import Request
from src.statistics import Statistics


class TestLoadBalancer(unittest.TestCase):

    def setUp(self):

        self.servers = [
            Server(i, f"Server-{i}")
            for i in range(1, 4)
        ]

        self.balancer = LoadBalancer(self.servers)

    def test_redirects_to_next_server_at_80_percent(self):
        results = []

        for request_id in range(1, self.balancer.REDIRECT_THRESHOLD + 2):
            server = self.balancer.get_next_server()
            self.assertIsNotNone(server)
            self.assertTrue(server.process_request(Request(request_id, "Client")))
            results.append(server.name)

        self.assertEqual(
            results[:-1],
            ["Server-1"] * self.balancer.REDIRECT_THRESHOLD,
        )
        self.assertEqual(results[-1], "Server-2")
        self.assertTrue(self.servers[0].is_online)

    def test_skip_offline_server(self):
        self.servers[1].is_online = False
        results = []
        for request_id in range(1, self.balancer.REDIRECT_THRESHOLD + 2):
            server = self.balancer.get_next_server()
            self.assertIsNotNone(server)
            self.assertTrue(server.process_request(Request(request_id, "Client")))
            results.append(server.name)
        self.assertEqual(
            results[:-1],
            ["Server-1"] * self.balancer.REDIRECT_THRESHOLD,
        )
        self.assertEqual(results[-1], "Server-3")

    def test_stop_when_last_server_reaches_capacity(self):
        stats = Statistics()
        last_server = self.servers[-1]
        request_id = 1

        while (
            stats.distribution[last_server.name]
            < self.balancer.REDIRECT_THRESHOLD
        ):
            server = self.balancer.get_next_server()
            self.assertIsNotNone(server)

            request = Request(request_id, f"Client-{request_id}")
            self.assertTrue(server.process_request(request))
            stats.record_request(server.name)
            request_id += 1

        self.assertEqual(
            stats.distribution[last_server.name],
            self.balancer.REDIRECT_THRESHOLD,
        )
        self.assertIsNone(self.balancer.get_next_server())
        self.assertTrue(all(server.is_online for server in self.servers))

    def test_routes_requests_after_first_server_reaches_capacity(self):
        stats = Statistics()
        routed_servers = []
        request_count = self.balancer.REDIRECT_THRESHOLD + 1

        for request_id in range(1, request_count + 1):
            server = self.balancer.get_next_server()
            self.assertIsNotNone(server)

            request = Request(request_id, f"Client-{request_id}")
            self.assertTrue(server.process_request(request))
            stats.record_request(server.name)
            routed_servers.append(server.name)

        self.assertEqual(
            stats.distribution["Server-1"],
            self.balancer.REDIRECT_THRESHOLD,
        )
        self.assertEqual(stats.distribution["Server-2"], 1)
        self.assertEqual(
            routed_servers[-2:],
            ["Server-1", "Server-2"],
        )
        self.assertTrue(self.servers[0].is_online)


if __name__ == "__main__":
    unittest.main()