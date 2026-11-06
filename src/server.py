from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Server:
    CAPACITY: ClassVar[int] = 200

    server_id:int
    name:str
    is_online: bool=True
    requests_handled:int=0
    def process_request(self,request):
        if not self.is_online or self.requests_handled >= self.CAPACITY:
            self.is_online = False
            return False
        self.requests_handled+=1
        if self.requests_handled >= self.CAPACITY:
            self.is_online = False
        return True


Servers = Server