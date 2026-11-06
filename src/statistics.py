from collections import Counter
from src.server import Server
#collection is lib wher we can use counter to count the number of occurences of each element in a list
#occurerence is the number of times an event happens or a value appears in a dataset.
class Statistics:
    def __init__(self):
        self.distribution = Counter()


    def record_request(self, server_name):
        self.distribution[server_name] += 1
    def display_distribution(self):
        print("======== Load Balancer Statistics ========")
        for server_name, count in self.distribution.items():
            percentage=min((count/Server.CAPACITY)*100, 100)
            print(f"Server: {server_name}, Requests Handled: {count}, Percentage: {percentage:.2f}%")  
            #distrbution.values() returns a view of the counts of each element in the counter object.
            #distribution.items() returns a view of the (element, count) pairs in the counter object.