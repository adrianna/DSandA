# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler_list):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.handler = handler
        self.root = None

        
        
    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        
        
        
        
    def find(self, final_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, child, handler):
        # Initialize the node with children as before, plus a handler
        self.child = None
        self.handler = handler
        self.is_handler = False
        
        
        
    def insert(self, child):
        # Insert the node as before

        if self.handler.get(child) is None:
            self.handler[child] = RouteTrieNode()
            
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, RouteTrie):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie()
        self.not_found = True

    def add_handler(self, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        
        for hdlr in self.routeTrie.child.keys():
            self.routeTrie.insert(hdlr)
            self.routeTrie = self.routeTrie[hdlr]

        self.routeTrie.is_handler = True

    def lookup(self, handler):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        self.split_path(handler)

    def split_path(self, handler ):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        hlist = split(handler, "/")
        print(hlist)

        return hlist
        
        

        
        # Here are some test cases and expected outputs you can use to test your implementation


        
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

/www.google.com/search



TrieNode1
www.google.com

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
