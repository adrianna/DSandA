#from helpers import Map, load_map, show_map
#from student_code import shortest_path

import math
import heapq as h
import pdb

#map_10 = load_map('map-10.pickle')
#show_map(map_10)



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

class GraphNode(object):
    def __init__(g, h, f):
        self.g = 0
        self.h = 0
        self.f = 0

        
    
## Find shortest path
def shortest_path(M,start,goal):
    
   # Initialize open and closed lists,and f,g,h scores
   open_path = []
   closed_path = []
   came_from = []
   
   g_score = [ math.inf for i in M.intersections().keys() ]
   f_score = [ math.inf for i in M.intersections().keys() ]
   h_score = [ 0 for i in M.intersections().keys() ]
   
   
   g_score[start] = 0
   # Calculate heuristic distance of start vertex to destination (h)
   h_score[start] = hScore(M.intersections()[start], M.intersections()[goal], "pythagorus")
   
   # Calculate f value for start vertex (f= g+h, where g= 0)
   f_score[start] = fScore(g_score[start], h_score[start])
   
   open_path.append((f_score[start], start))
   
   while open_path:
       
       # Take node from lowest path
       _ , current_node  = min(open_path)
       if current_node == goal:
           print("Found!")
           return reconstruct_path(closed_path, current_node);
       
       open_path.remove((f_score[current_node], current_node))
       closed_path.append(current_node)
       
       pdb.set_trace()
       for neighbor in M.roads()[current_node]:

           if neighbor in closed_path:
               print("neighbor ({}) in closed_path {}".format(neighbor, closed_path))
               continue

           # Calculate g_score 'gtmp' for neighbor at current node position
           gtmp = g_score[current_node] + dist(M.intersections()[current_node], M.intersections()[neighbor], "pythagorus")
           f_score[neighbor] = gtmp + h_score[neighbor]
           #if neighbor not in open_path:
           # open_path.append((f_score[neighbor], neighbor))
           # came_from.append(current_node)
           if neighbor in open_path:
               # Neighbor is found in open_path, therefore, revaluate current g_score < gtmp
               if gtmp > g_score[neighbor]:
                   continue
               
               # Append 
               h_score[neighbor] = hScore(M.intersections[current_node], M.intersections[neighbor], "pythagorus")
               g_score[neighbor] = gtmp
               f_score[neighbor] = g_score[neighbor] + h_score[neigbor]
               
           open_path.append((f_score[neighbor], neighbor))    
               
   return False




## Calculate Path Cost
def calculatePathCost(f, road_list):
    pass


## Reconstruct Path
def reconstruct_path(cameFrom, current):
    total_path = current
    while current in cameFrom.keys:
        current = cameFrom[current]
        total_path.prepend(current)

    return total_path

## Cost Path Calculation
# h() Estimated Cost Path
def dist(xy_start, xy_end, cost_path):
    start_x = xy_start[0]
    start_y = xy_start[1]

    end_x = xy_end[0]
    end_y = xy_end[1]

    dx = end_x - start_x
    dy = end_y - start_y
    
    if cost_path == "manhattan":
        return manhattan_distance(dx,dy)
    
    else: # "pythagoras"
        return hypothenuse(dx,dy) 

   
# f() Total Cost Path    
def fScore(hDist, gDist = 0):
    return gDist + hDist

def hScore(xy_start, xy_end, cost_path):
    return dist(xy_start, xy_end, cost_path)
    
# Pythagorus Method
def hypothenuse(x,y):
    return math.hypot(x, y)

# Manhattan Distance
def manhattan_distance(x,y):
    return x + y

           

#### MAIN ####
print("executing shortest path from Node 0 to Node 2")
map = map_10()
shortest_path(map, 0, 2) 

    
