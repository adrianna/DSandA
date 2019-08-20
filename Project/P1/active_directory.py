##################################
# P1: active_directory.py
#
# Issue: See comment below at line #83
#
#
##################################

debug = 0
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []      # list of class Groups
        self.users = []       # list of string user

    def add_group(self, group):
        if debug: print("[[add_group]]: {}".format(group))
        self.groups.append(group)

    def add_user(self,user):
        if debug: print("[[add_user]]: {}".format(user))
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    
def is_user_in_group(user, group, grp_queue = None):

    group_queue = []

    # Match user to group's name
    if user == group.get_name():
        # print("user matches group name")
        return True
    
    # Match user to get_users
    elif user in group.get_users():
        # print("user is in group's user list")
        return True
    
    # if Group's group list not empty, recurse 
    if len(group.get_groups()) == 0:
        # print("group's group list is empty, return False")
        return False
    
    else:
        
        # print("group.name = {}".format(group.get_name()))
        # print("Descend into Group's group at a time, group_list: {}".format(group.get_groups()))
        if grp_queue is None:
            grp_queue = group.get_groups()
            return is_user_in_group(user, group, grp_queue)

        else:
            grp_queue += group.get_groups()  
            return is_user_in_group(user, grp_queue.pop(0), grp_queue)

                  
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

print("Creating Group Tree")
sub_child_user = "sub_child_user"
print(" * Adding user _sub_child_user_ to sub_child")
sub_child.add_user(sub_child_user)

print(" * Adding group __sub_child__ to child")
child.add_group(sub_child)

print(" * Adding group __child__ to parent")
parent.add_group(child)

#print("parent's groups: {}".format(parent.get_groups()))
#print("child's name = {}".format(child.get_name()))

# TEST CASE 1
print("Is child in group parent? {}".format(is_user_in_group("child", parent)))


# TEST CASE 2
print("Is subchild in group parent? {}".format(is_user_in_group("subchild", parent)))

# TEST CASE 3
print("Is subchild in group child? {}".format(is_user_in_group("subchild", child)))


# TEST CASE 4
step_parent = Group("step_parent")
step_parent.add_group(child)

print("Is child in group step parent? {}".format(is_user_in_group("child", step_parent)))
