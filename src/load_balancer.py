from typing import List, Optional
from src.server import Server
#we import typing to use List and Optional for type hinting. We also import the Servers class from the server module.
#typing is a library that provides support for type hints in Python. 
#hint is a way to indicate the expected data types of variables, function parameters, and return values.
class LoadBalancer:
    SERVER_CAPACITY = Server.CAPACITY
    REDIRECT_THRESHOLD_PERCENT = 80
    REDIRECT_THRESHOLD = SERVER_CAPACITY * REDIRECT_THRESHOLD_PERCENT // 100

    def __init__(self, servers: List[Server]):
        #we use dictionary comprehension to create a dictionary of servers with their server_id as the key and the server object as the value.
        self.servers = servers
        self.current_index = 0
    def get_next_server(self) -> Optional[Server]:
        while self.current_index < len(self.servers):
            server=self.servers[self.current_index]
            if (
                server.is_online
                and server.requests_handled < self.REDIRECT_THRESHOLD
            ):
                return server
            if server.requests_handled >= self.SERVER_CAPACITY:
                server.is_online = False
            self.current_index += 1
        return None     