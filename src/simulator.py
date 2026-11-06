import random

from src.server import Server
from src.request import Request
from src.load_balancer import LoadBalancer
from src.statistics import Statistics


def create_servers(number_of_servers):

    servers = []

    for i in range(1, number_of_servers + 1):

        server = Server(
            server_id=i,
            name=f"Server-{i}"
        )

        servers.append(server)

    return servers
#we define a function create_servers that takes the number of servers as an argument and creates a list of Server objects with unique server_id and name. The function returns the list of servers.

def generate_requests(number_of_requests):

    requests = []

    for i in range(1, number_of_requests + 1):

        request = Request(
            request_id=i,
            client_name=f"Client-{random.randint(1, 100)}"
        )

        requests.append(request)

    return requests


def run_simulation():

    number_of_servers = 10
    number_of_requests = 2000

    servers = create_servers(number_of_servers)

    load_balancer = LoadBalancer(servers)

    requests = generate_requests(number_of_requests)

    # Initialize statistics
    stats = Statistics()
    stats.distribution.update({server.name: 0 for server in servers})

    print("\nROUND ROBIN LOAD BALANCER SIMULATION")
    print("-----------------------------------")

    # Distribute requests
    for request in requests:

        server = load_balancer.get_next_server()

        if server:

            server.process_request(request)
#process_request is a method of the Server class that takes a Request object as an argument and processes it. If the server is online, it increments the requests_handled count and returns True. If the server is offline, it returns False.
            stats.record_request(server.name)
#record_request is a method of the Statistics class that takes a server name as an argument and increments the count of requests handled by that server in the distribution Counter object.
            print(
                f"Request {request.request_id} "
                f"from {request.client_name} "
                f"-> {server.name}"
            )

        else:
            print(f"Request {request.request_id}: No available server")

    # Display results
    stats.display_distribution()


if __name__ == "__main__":
    run_simulation()