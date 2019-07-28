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

from helpers import Map, load_map, show_map
from student_code import shortest_path

import math
import heapq as h

map_10 = load_map('map-10.pickle')
show_map(map_10)

#map_10.intersections
#map_10.roads



## Find shortest path
def shortest_path(M,start,goal):
    
   # Initialize open and closed lists
   open_path = []
   closed_path = []

   initialize(g_score, M)
   initialize(f_score, M)

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
    if current_node = goal:
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
            cameFrom[neighbor] = current_node
            h_score[neighbor] = hScore(M.intersections[current_node], M.intersections[neighbor], "pythagorus")
            g_score[neighbor] = g_score_tmp[neighbor]
            f_score[neighbor] = g_score[neighbor] + h_score[neigbor]
            

            



   
    
#    print("shortest path called")
#    return



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
def initialize(cost_list, map):
    node_count = len(map.keys())

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
def fScore(gDist = 0, hDist):
    return gDist + hDist

def dist(xy_start, xy_end, cost_path):
    return hScore(xy_start, xy_end, cost_path)
    
# Pythagorus Method
def hypothenuse(x,y):
    return math.hypot(dx, dy)

# Manhattan Distance
def manhattan_distance(x,y):
    return x + y

    


        
