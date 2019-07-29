#from helpers import Map, load_map, show_map
#from student_code import shortest_path

import math
import heapq as h

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
    
## Find shortest path
def shortest_path(M,start,goal):
    
   # Initialize open and closed lists
   open_path = []
   closed_path = []

   g_score = []
   f_score = []
   h_score = []
   
   initialize(g_score, M)
   initialize(f_score, M)

   print(g_score)
   print(f_score)
   
   # Make the start vertex current
   current_node = start
   open_path.append(current_node)
    
   
   # Calculate heuristic distance of start vertex to destination (h)
   h_score[start] = hScore(M.intersections[start], M.intersections[goal])
   
   # Calculate f value for start vertex (f= g+h, where g= 0)
   f_score[start] = fScore(h_score[start])

   frontier = []
   h.heapify(frontier, (current_node, f_score[start]))
   
   while open_path:

       # Take node from lowest path
       current_node = h.pop()
       if current_node == goal:
           return reconstruct_path(cameFrom, current_node);
       
       calculatePathCost(frontier, M.roads[current_node])
       
       open_path.remove(current_node)
       closed_path.append(current_node)
       
       for neighbor in M.roads[current_node]:
           if neighbor in closed_path:
               g_score_tmp[neighbor] = g_score[current_node] + dist(M.intersections[current_node], M.intersections[neighbor])
           if neighbor not in open_path:
               open_path.append(neighbor)
           elif g_score_tmp[neighbor] > g_score[neighbor]:
               continue
           else:
               cameFrom[neighbor] = current_node
               h_score[neighbor] = hScore(M.intersections[current_node], M.intersections[neighbor], "pythagorus")
               g_score[neighbor] = g_score_tmp[neighbor]
               f_score[neighbor] = g_score[neighbor] + h_score[neigbor]
               
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

## Initalize Scores
def initialize(cost_list, m):
    node_count = len(m.intersections().keys())

    for idx in range(node_count):
        cost_list[idx] = math.inf

        

## Cost Path Calculation

# h() Estimated Cost Path
def hScore(xy_start, xy_end, cost_path):
    start_x = start_xy[0]
    start_y = start_xy[1]

    end_x = goal_xy[0]
    end_y = goal_xy[1]

    dx = end_x - start_x
    dy = end_y - start_y
    
    if cost_path == "manhattan":
        return manhattan_distance(dx,dy)
    
    else: # "pythagoras"
        return hypothenuse(dx,dy)
   
# f() Total Cost Path    
def fScore(hDist, gDist = 0):
    return gDist + hDist

def dist(xy_start, xy_end, cost_path):
    return hScore(xy_start, xy_end, cost_path)
    
# Pythagorus Method
def hypothenuse(x,y):
    return math.hypot(dx, dy)

# Manhattan Distance
def manhattan_distance(x,y):
    return x + y

           

#### MAIN ####
print("executing shortest path from Node 0 to Node 2")
map = map_10()
shortest_path(map, 0, 2) 

    


        
######################
## A* Search
##
## Notes:
##  f = g + h
##  Path	   Path Cost (g)  Est. Distance (h)	Total (f)
##  Arad >> Zerind	75	      374                 449
##  Arad >> Sibiu	140	      253                 393 **
##  Arad >> Timisoara	118	      329                 447
##
##  ** Expand here
##
##
##  Path	       Path Cost (g)  Est. Distance (h)	Total (f)
##  Arad >> Zerind   	  75	            374	         449
##  Arad > S >> Oradea	  291	            380	         671
##  Arad > S >> Fagaras	  239	            176          415
##  Arad > S >> RVilcea	  220	            193	         413 **
##  Arad >> Timisoara	  118	            329          447
##
## ** Expand here
## Repeat!


# These Map objects have two properties you will want to use to implement
# A* search: intersections and roads

# Intersections
# The intersections are represented as a dictionary.

# In this example, there are 10 intersections, each identified by an x,y
# coordinate. The coordinates are listed below. You can hover over each dot
# in the map above to see the intersection number.
