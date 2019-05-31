from DataStructures import *
import DataStructures.s as ds
import os


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
    cfile_dir = []
    if not os.path.exists(path):
        print("Returning... from find_files, dir {}".format(os.getcwd())) 
        return None 
    else:
        cfdir = _find_files(suffix,path)
        print("cfd_list: {}".format(cfdir))
        return cfdir

def _find_files(suffix,path):
    print("Calling _find_files({},{})".format(suffix, path))
    dlist = os.listdir(path)
#    print(dlist)
    for file in dlist:
        print("\tFor each file: {}".format(file))
        if os.path.exists(path):
            print("\tPath: {} exists".format(path))
            if file.endswith(suffix):
                print("\t{} has .c suffix".format(file))
                return path
            if os.path.isdir(file):
                os.chdir(file)
                print("\t{} is a directory".format(file))
                _find_files(suffix, file)
        else:
            os.chdir("../")
            return None     
            

############## Main #########

path = "testdir"
print(find_files(".c", path))
