##################################
# P1: active_directory.py
#
# Issue: Another recursion. Having issue with getting access to groups list
#   
# Questions:
#    1. Getting access to group lists on Line 49
#
#
##################################


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []      # class Groups
        self.users = []       # user: class Group

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self,user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    
def is_user_in_group(user, group):
    # check is user is in the group's user list
    # traverse string user list of group
    # if not found, traverse groups' group list
    # recursive search
    # if found, return True
     

    group_groups = group.get_groups()

    
    user_name = user.get_name()
    group_users = group.get_users()
    for usr in group_users:
        if usr.get_name() == user_name:
            return True
        else:
            
            #if len(group_groups) == 0:
            #    print("group_groups not empty")
            
            #    for grp in range(len(group.get_groups())):
            #        grp_name = group.get_groups()[grp]
            #        print(grp_name)
            return is_user_in_group(user, grp_name)
        #else:
        #                return False
    return False    

    
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"  
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

is_user_in_group(child, parent)


#print "parent groups"
#print(parent.get_groups())
#print
#print "child groups"
#print(child.get_groups())
#print
#print "sub child groups"
#print(sub_child.get_groups())
#print
#print "length of sub_child.groups()"
#print(len(sub_child.get_groups()))
#print "length of child.groups()"
#print(len(child.get_groups()))
#print "child subgroup name"
#print(child.get_groups()[0].name)
#print
#print "parent subgroup name"
#print(parent.get_groups()[0].name)
#print "parent sub - sub groups name"
#print(parent.get_groups()[0].get_groups()[0].name)

#print "parent sub groups"
#print(parent.get_groups()[0])
#print
#print
#print "len of parent sub-sub  groups"
#print(parent.get_groups()[0].get_groups()[0].name)

#for usr in range(len(parent.get_groups())):
#    print("user: {}".format(usr))


# Questions
# 1. Can users be in multiple groups?
#   a. Is data structure a strict heirarchy?
# 2. How is subchild group linked to child? Or is it?
#   Do we append subchild into child's subchild group?


