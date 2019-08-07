import math
from queue import PriorityQueue


## Collections
from collections import namedtuple

#from collections import namedtuple
# namedtuple('Node', 'f g n')
#node <class '__main__.Node'
#node.g <property object at 0x7f1831c00ea8
#>>> n = node(10, 20, 1) 
#  Node(f=10, g=20, n=1) 
#>> n.f
# 10



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



class Node:
  def __init__(self, value, g=0):
    self.g = g
    self.h = 0
    self.f = g+h
    self.parent = None
    self.val = value


def dist_between(start:list(), end:list()):
  x1, y1 = start
  x2, y2 = end

  x = math.pow((x2-x1),2)
  y = math.pow((y2-y1),2)
  
  return math.sqrt(x+y)


  
def shortest_path(graph, start, goal):

  open_path = []
  closed_path = {}
  open_path = 'node1':
             'node2': PriorityQueue()
             ]
  


  current = start

  while open_path:

    # current = Pop from open_list heap to retrieve lowest f-score node
    # Append to neighbor to closed path (?)     

    
    for neighbor in graph.roads[current]:
      
      if neighbor not in open_path:
        # calculate f,g,h score of neighbor
        g_score = dist_between(graph.intersections[current], graph.intersections[neighbor])
        h_score = dist_between(graph.intersections[neighbor], graph.intersections[goal])
        f_score = g_score + h_score

      elif neighbor in open_path:
        # compare the g-value recently computed against the existing
        if g_score <= g(neighbor):
          g(neighbor) = g_score
          f(neighbor) = f_score
          neighbor.parent = current


          #   #   # Append to neighbor to closed path (?)

  if current = goal
  return path

 return "Not found!"















###############################################################################################################



      
      
      if closed_path.get(neighbor) is None:
        
        # calculate f score of neighbor

        
        #open_path.append(neighbor)
        open_path.put((f_score, g_score, neighbor))
        
    # for loop is done, compare f score against neighbor's f_score
    f_min, g_min, neighbor = open_path.get()

    # create new Node = neighbor with f_min

    # advance current to neighbor with f_min
    # track the neighbor.parent = current
    # (g_score) path_cost = g_min
    
    # store current (neighbor with fmin) into closed_path
    
    
    # if current == goal
    #  return path_traveled 
    
  
