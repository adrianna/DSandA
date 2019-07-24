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


# Route Planner

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


## Create Graph Tree

# These Map objects have two properties you will want to use to implement
# A* search: intersections and roads

# Intersections

# The intersections are represented as a dictionary.

# In this example, there are 10 intersections, each identified by an x,y
# coordinate. The coordinates are listed below. You can hover over each dot
# in the map above to see the intersection number.

## Find shortest path
def shortest_path(M,start,goal):

    
    print("shortest path called")
    return
