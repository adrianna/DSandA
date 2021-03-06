# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.paths = dict()
        self.is_handler = False

        
    def convertRootHandler(self,handler):
        if handler == "/":
            return "root handler"
        return handler

    
    def insert(self, handler):
        # Insert the node as before

        if self.paths.get(handler) is None:
            
            self.paths[handler] = RouteTrieNode()

            

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler
        
    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_path = self.root
        
        for p in path_list:
            current_path.insert(p)            
            current_path = current_path.paths[p]
            
        current_path.is_handler = True
        current_path.handler = handler
        
    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root
        
        if current_node.paths is None:
            return "No match"

        for p in path_list:
            if current_node.paths.get(p):
                current_node = current_node.paths[p]
            else:
                return None
        return current_node.handler
            
            
        
            
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler_list):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(handler_list)
        self.handler_list = handler_list
 

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        
        handler_list = self.split_path(path)
        current_path = self.routeTrie
        
        current_path.insert(handler_list, handler)
            

    def lookup(self, handler):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        current_path = self.routeTrie
        if handler == "/":
            return current_path.handler
        
        
        path_list = self.split_path(handler)
        
        found_handler = current_path.find(path_list)
        
        if found_handler:
            return found_handler

        return None
    
    def split_path(self, handler ):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here


        if handler:
            hlist = []            
            for item in handler.split("/"):
                if item:
                    hlist.append(item)
                        
            return hlist
        

        
# Here are some test cases and expected outputs you can use to test your implementation
        
# create the router and add a route
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

TC#1 - different handler added to tree
router.add_handler("/usr/bin", "bin handler")
print(router.lookup("/usr/bin"))

TC#2 - more handlers
router.add_handler("/usr/include", "include handler")
print(router.lookup("/usr/include"))

TC#3 - more handlers, same parent
router.add_handler("/usr/sbin", "sbin handler")
print(router.lookup("/usr/sbin"))



