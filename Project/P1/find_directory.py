##################################
# P1: find_directory.py
#
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
                if root not in cfiles_dir:
                    cfiles_dir.append(root)
            
    return cfiles_dir
   
############## Main #########

path = "testdir"
print(find_files("*.c", path))
#['/Users/ladyhypatia/Documents/School/Udacity/DSandA/Project/P1/testdir',
# '/Users/ladyhypatia/Documents/School/Udacity/DSandA/Project/P1/testdir/subdir1',
# '/Users/ladyhypatia/Documents/School/Udacity/DSandA/Project/P1/testdir/subdir3/subsubdir1',
# '/Users/ladyhypatia/Documents/School/Udacity/DSandA/Project/P1/testdir/subdir5']

path = "testdir/subdir3"
print(find_files("*.c", path))
#['/Users/ladyhypatia/Documents/School/Udacity/DSandA/Project/P1/testdir/subdir3/subsubdir1']

path = "testdir/subdir4"
print(find_files("*.c", path))
#[]
