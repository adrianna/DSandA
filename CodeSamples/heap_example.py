import heapq
class PQNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    # compares the second value
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str("{} : {}".format(self.key, self.value))

input = [PQNode(1, 4), PQNode(7, 4), PQNode(6, 9), PQNode(2, 5)]
hinput = []
for item in input:
    heapq.heappush(hinput, item)

while (hinput):
    print (heapq.heappop(hinput))

    
