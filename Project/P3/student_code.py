#from helpers import Map, load_map, show_map
#from student_code import shortest_path

#map_10 = load_map('map-10.pickle')
#show_map(map_10)


import math
import heapq as h
import pdb

## MAP of 10 Nodes ##

class map_10(object):
    def __init__(self):
        self.intersections = { 0: [0.7798606835438107, 0.6922727646627362],
                               1: [0.7647837074641568, 0.3252670836724646],
                               2: [0.7155217893995438, 0.20026498027300055],
                               3: [0.7076566826610747, 0.3278339270610988],
                               4: [0.8325506249953353, 0.02310946309985762],
                               5: [0.49016747075266875, 0.5464878695400415],
                               6: [0.8820353070895344, 0.6791919587749445],
                               7: [0.46247219371675075, 0.6258061621642713],
                               8: [0.11622158839385677, 0.11236327488812581],
                               9: [0.1285377678230034, 0.3285840695698353] }
        self.roads = [[7, 6, 5],
                      [4, 3, 2],
                      [4, 3, 1],
                      [5, 4, 1, 2],
                      [1, 2, 3],
                      [7, 0, 3],
                      [0],
                      [0, 5],
                      [9],
                      [8]]

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
   
   while current_node != goal:
       
       # Take node from lowest path
       _ , current_node  = min(open_path)
       if current_node == goal:
           print("Found!")
           return reconstruct_path(closed_path, current_node);
       
       open_path.remove((f_score[current_node], current_node))
       closed_path.append(current_node)
       
#       pdb.set_trace()
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

    
print(a_star_search(graph, 5, 34))
# Answer: [5, 16, 37, 12, 34]

print(a_star_search(graph, 5, 5))
# Answer: [5]

print(a_star_search(graph, 8, 24))
# Answer: [8, 14, 16, 37, 12, 17, 10, 24]








#########################################################################################
#########################################################################################
# MAP of 40 nodes
class map_40(object):
    def __init__(self):
        self.coordinates = {}
        self.neighbors = []

    def intersections(self):
        self.coordinates = { 0: [0.7801603911549438, 0.49474860768712914],
                             1: [0.5249831588690298, 0.14953665513987202],
                             2: [0.8085335344099086, 0.7696330846542071],
                             3: [0.2599134798656856, 0.14485659826020547],
                             4: [0.7353838928272886, 0.8089961609345658],
                             5: [0.09088671576431506, 0.7222846879290787],
                             6: [0.313999018186756, 0.01876171413125327],
                             7: [0.6824813442515916, 0.8016111783687677],
                             8: [0.20128789391122526, 0.43196344222361227],
                             9: [0.8551947714242674, 0.9011339078096633],
                             10: [0.7581736589784409, 0.24026772497187532],
                             11: [0.25311953895059136, 0.10321622277398101],
                             12: [0.4813859169876731, 0.5006237737207431],
                             13: [0.9112422509614865, 0.1839028760606296],
                             14: [0.04580558670435442, 0.5886703168399895],
                             15: [0.4582523173083307, 0.1735506267461867],
                             16: [0.12939557977525573, 0.690016328140396],
                             17: [0.607698913404794, 0.362322730884702],
                             18: [0.719569201584275, 0.13985272363426526],
                             19: [0.8860336256842246, 0.891868301175821],
                             20: [0.4238357358399233, 0.026771817842421997],
                             21: [0.8252497121120052, 0.9532681441921305],
                             22: [0.47415009287034726, 0.7353428557575755],
                             23: [0.26253385360950576, 0.9768234503830939],
                             24: [0.9363713903322148, 0.13022993020357043],
                             25: [0.6243437191127235, 0.21665962402659544],
                             26: [0.5572917679006295, 0.2083567880838434],
                             27: [0.7482655725962591, 0.12631654071213483],
                             28: [0.6435799740880603, 0.5488515965193208],
                             29: [0.34509802713919313, 0.8800306496459869],
                             30: [0.021423673670808885, 0.4666482714834408],
                             31: [0.640952694324525, 0.3232711412508066],
                             32: [0.17440205342790494, 0.9528527425842739],
                             33: [0.1332965908314021, 0.3996510641743197],
                             34: [0.583993110207876, 0.42704536740474663],
                             35: [0.3073865727705063, 0.09186645974288632],
                             36: [0.740625863119245, 0.68128520136847],
                             37: [0.3345284735051981, 0.6569436279895382],
                             38: [0.17972981733780147, 0.999395685828547],
                             39: [0.6315322816286787, 0.7311657634689946]}
        
        return self.coordinates
    
    def roads(self):
        self.neighbors = [[35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
                          [39, 36, 21, 19, 9, 7, 4],
                          [35, 20, 15, 11, 6],
                          [39, 36, 21, 19, 9, 7, 2],
                          [32, 16, 14],
                          [35, 20, 15, 11, 1, 3],
                          [39, 36, 22, 21, 19, 9, 2, 4],
                          [33, 30, 14],
                          [36, 21, 19, 2, 4, 7],
                          [31, 27, 26, 25, 24, 18, 17, 13],
                          [35, 20, 15, 3, 6],
                          [37, 34, 31, 28, 22, 17],
                          [27, 24, 18, 10],
                          [33, 30, 16, 5, 8],
                          [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
                          [37, 30, 5, 14],
                          [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
                          [31, 27, 26, 25, 24, 1, 10, 13, 17],
                          [21, 2, 4, 7, 9],
                          [35, 26, 1, 3, 6, 11, 15],
                          [2, 4, 7, 9, 19],
                          [39, 37, 29, 7, 12],
                          [38, 32, 29],
                          [27, 10, 13, 18],
                          [34, 31, 27, 26, 1, 10, 15, 17, 18],
                          [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
                          [31, 1, 10, 13, 18, 24, 25, 26],
                          [39, 36, 34, 31, 0, 12, 17],
                          [38, 37, 32, 22, 23],
                          [33, 8, 14, 16],
                          [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
                          [38, 5, 23, 29],
                          [8, 14, 30],
                          [0, 12, 17, 25, 26, 28, 31],
                          [1, 3, 6, 11, 15, 20],
                          [39, 0, 2, 4, 7, 9, 28],
                          [12, 16, 22, 29],
                          [23, 29, 32],
                          [2, 4, 7, 22, 28, 36]]
        
        return self.neighbors

    def cost(self, x, y):

        return heuristic(self.intersections()[x], self.intersections()[y])
