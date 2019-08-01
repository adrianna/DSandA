import math
import heapq as h
import pdb

class map_10(object):
    def __init__(self):
        self.coordinates = {}
        self.neighbors = []

    def intersections(self):
        self.coordinates = { 0: [0.7798606835438107, 0.6922727646627362],
                             1: [0.7647837074641568, 0.3252670836724646],
                             2: [0.7155217893995438, 0.20026498027300055],
                             3: [0.7076566826610747, 0.3278339270610988],
                             4: [0.8325506249953353, 0.02310946309985762],
                             5: [0.49016747075266875, 0.5464878695400415],
                             6: [0.8820353070895344, 0.6791919587749445],
                             7: [0.46247219371675075, 0.6258061621642713],
                             8: [0.11622158839385677, 0.11236327488812581],
                             9: [0.1285377678230034, 0.3285840695698353] }
        
        return self.coordinates
    def roads(self):
        self.neighbors = [[7, 6, 5],
                          [4, 3, 2],
                          [4, 3, 1],
                          [5, 4, 1, 2],
                          [1, 2, 3],
                          [7, 0, 3],
                          [0],
                          [0, 5],
                          [9],
                          [8]]
        return self.neighbors

    
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far



graph = map_10()
print("testing a_star_search...")

a_star_search(graph, 0, 2)



#def a_star_search(graph, start, goal):
#    frontier = PriorityQueue()
#    frontier.put(start, 0)
#    came_from = {}
#    cost_so_far = {}
#    came_from[start] = None
#    cost_so_far[start] = 0
#    
#    while not frontier.empty():
#        current = frontier.get()
#        
#        if current == goal:
#            break
#        
#        for next in graph.neighbors(current):
#            new_cost = cost_so_far[current] + graph.cost(current, next)
#            if next not in cost_so_far or new_cost < cost_so_far[next]:
#                cost_so_far[next] = new_cost
#                priority = new_cost + heuristic(goal, next)
#                frontier.put(next, priority)
#                came_from[next] = current
#    
#    return came_from, cost_so_far

