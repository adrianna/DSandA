##################################
# P1: find_directory.py
#
#  Issue: See comments where I have issues with the recursion
#
####### Old Submission
# A reviewer advised me to use os.walk(), but I was wondering if I could
# write my own recursion. Why doesn't it work? Do I need a tail recursion?
# Sometimes I start with base case, but it seems given the programming call
# stack nature, storing the intermediate values might be overwritten if
# I have in the parent function, and initialize list() or dict().
# Subsequent calls to the stack would reset these list/dict creations.
# So I have seen some recursion solutions have a helper function. I was
# if I needed this for this problem. And How can I implement it? 
#
# Additionally, I'm trying to find a balance between using the python libraries
# or creating my own. Since this is a DSA class, I am under the impression
# of creating my libraries. Is this expected?
#
#
##################################


import os, fnmatch


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    cfiles_dir = []
    path = os.getcwd() + "/" + path
    # If path does not exist, return False

    if not os.path.exists(path):
        print("Returning... from find_files, dir {}".format(os.getcwd())) 
        return None 

    for root, dirs, files in os.walk(path):
        for file_name in files:
            if fnmatch.fnmatch(file_name, suffix):
                fileos.path(join(root
            
            for dir_name in dirs:
                print(os.path.join(root, dir_name)) 

    

   
############## Main #########

path = "testdir"
print(find_files(".c", path))
