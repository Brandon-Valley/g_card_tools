import glob
import os
# from shutil import copyfile
import shutil
from distutils.dir_util import copy_tree
import ntpath
 
# VVVVV Internal VVVVV

 
# VVVVV External VVVVV

""" VVVVVVVVVV                             VVVVVVVVVV"""
""" VVVVVVVVVV get info about GIVEN object VVVVVVVVVV"""
""" VVVVVVVVVV                             VVVVVVVVVV"""

def is_dir(in_path):
    return os.path.isdir(in_path)

def is_file(in_path):
    return os.path.isfile(in_path)

# gets size of dir (and maybe file?) in bytes

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size



def get_file_extension(in_file_path):
    if not is_file(in_file_path):
        raise Exception("ERROR:  in_file_path must point to a file that exists")
    
    extension = os.path.splitext(in_file_path)[1]
    
    return extension

"""SHOULD PROBABLY RENAME
# !!!!! ONLY WAY TO USE THIS FUNC:  file_system_utils.get_path_to_current_file(__file__) !!!!!
# returns absolute path to the dir that contains the file that calls this function,
# NOT the current working directory
# the only reason this function is here is because I know that
# if it isn't, I wont be able to find it later"""
def get_path_to_current_file(file_obj):
    return os.path.dirname(os.path.abspath(file_obj))


def raise_exception_if_object_not_exist(obj_path, custom_msg = None):
    if not is_file(obj_path) and not is_dir(obj_path):
        if custom_msg == None:
            raise Exception("ERROR:  This thing does not exist: ", obj_path)
        else:
            raise Exception(custom_msg)
        
        



""" VVVVVVVVVV                                         VVVVVVVVVV"""
""" VVVVVVVVVV Get info about objects inside GIVEN DIR VVVVVVVVVV"""
""" VVVVVVVVVV                                         VVVVVVVVVV"""

""" returns names of all file and dirs in dir """
def get_objects_in_dir(in_dir_path):

    if is_dir(in_dir_path) != True:
        raise Exception("ERROR:  in_dir_path must point to dir")
    return os.listdir(in_dir_path)


def get_newest_file_path(dir_path):
    list_of_files = glob.glob(dir_path + '/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # print (latest_file)
    return latest_file

'''returns list'''
def get_relative_path_of_files_in_dir(dir_path, file_type):
    # Getting the current work directory (cwd)
    thisdir = os.getcwd()
    
    path_list = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(dir_path):
        for file in f:
            if file_type in file:
#                 print(os.path.join(r, file))
                path_list.append(os.path.join(r, file))
    return path_list



def get_abs_path_l_of_all_object_type_in_dir(in_dir_path, object_type = 'all'):
    
    obj_abs_path_l = []
    object_name_l = get_objects_in_dir(in_dir_path)
    
    for object_name in object_name_l:
        abs_obj_path = in_dir_path + '//' + object_name
        if object_type   == 'all':
            obj_abs_path_l.append(abs_obj_path)
        elif object_type == 'file' and is_file(abs_obj_path):
            obj_abs_path_l.append(abs_obj_path)
        elif object_type == 'dir'  and is_dir (abs_obj_path):
            obj_abs_path_l.append(abs_obj_path)
    return obj_abs_path_l




# in_dir_path - can be either abs or relative path
def get_dir_content_l(in_dir_path, object_type = 'all', content_type = 'abs_path'):
    if is_dir(in_dir_path) != True and in_dir_path != '':
        raise Exception("ERROR:  in_dir_path must point to dir")
    if object_type not in ['all', 'dir', 'file']:
        raise Exception("ERROR:  Invalid object_type: ", object_type, "  object_type must be one of:  ['all', 'dir', 'file']")
    if content_type not in ['abs_path', 'rel_path', 'name']:
        raise Exception("ERROR:  Invalid content_type: ", content_type, "  object_type must be one of:  ['abs_path', 'rel_path', 'name']")
    
    abs_in_dir_path = get_abs_path_from_rel_path(in_dir_path)
    print('in fsu, abs_in_dir_path: ', abs_in_dir_path)#`````````````````````````````````````````````````````````````````````
    object_name_l = os.listdir(abs_in_dir_path) # list of names of all dirs and files in dir
    
    if content_type == 'name' and object_type == 'all':
        return object_name_l
    
    # get header - str that will be added in front of obj name
    header = '' 
    if   content_type == 'abs_path':
        header = abs_in_dir_path + '//' 
    elif content_type == 'rel_path':
        raise Exception('ERROR: rel_path option not yet implemented')
    
    content_l = []
    
    # fill content_l
    for object_name in object_name_l:
        if object_type   == 'all':
            content_l.append(header + object_name)
        else:
            abs_obj_path = abs_in_dir_path + '//' + object_name
            
            if   object_type == 'file' and is_file(abs_obj_path):
                content_l.append(header + object_name)
            elif object_type == 'dir'  and is_dir (abs_obj_path):
                content_l.append(header + object_name)

    return content_l






"""returns oldest first, youngest last"""
def get_file_paths_in_dir_by_age(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    
    abs_path_l = []
    for rel_path in a:
        abs_path_l.append(dirpath + '/' + rel_path)
    return abs_path_l

# returns in alphabetical order
def get_names_of_files_in_dir(in_dir_path):
    file_name_l = []
    
    for r, d, f in os.walk(in_dir_path):
        for file in f:
            file_name_l.append(file)
    return file_name_l

"""VVVVVVVVVV                                   VVVVVVVVVV"""
"""VVVVVVVVVV  Operate on or move given OBJECT(s)  VVVVVVVVV"""
"""VVVVVVVVVV                                   VVVVVVVVVV"""


def copy_object_to_dest(in_path, dest_parent_dir_path):
    make_dir_if_not_exist(dest_parent_dir_path)

    if   os.path.isdir(in_path):
        copy_tree(in_path, dest_parent_dir_path)
    elif os.path.isfile(in_path):
        shutil.copy(in_path, dest_parent_dir_path)

def make_dir_if_not_exist(dir_path):
    abs_dir_path = get_abs_path_from_rel_path(dir_path)
    if not os.path.exists(abs_dir_path):
        os.makedirs(abs_dir_path)
        
        
def make_file_if_not_exist(file_path):
    parent_dir_path = get_parent_dir_from_path(file_path)
    make_dir_if_not_exist(parent_dir_path)
    if not is_file(file_path):
        file = open(file_path, "w") 
        file.close()
        
def delete_if_exists(path):
    if os.path.exists(path):
        if   os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        else:
            raise Exception('ERROR:  Gave something that is not a file or a dir, bad path: ', path)


''' will do nothing if src_file_path == dest_file_path '''
def rename_file_overwrite(src_file_path, dest_file_path):
    if not paths_equal(src_file_path, dest_file_path):        
        delete_if_exists(dest_file_path)
        os.rename(src_file_path, dest_file_path)

def copy_objects_to_dest(path_l, dest_parent_dir_path):
    make_dir_if_not_exist(dest_parent_dir_path)
    
    for path in path_l:
        if   os.path.isdir(path):
            copy_tree(path, dest_parent_dir_path)
        elif os.path.isfile(path):
            shutil.copy(path, dest_parent_dir_path)

def copy_files_to_dest(file_path_l, dest_dir_path): 
#     if os.path.isdir(dest_dir_path) == False:
#         os.mkdir(dest_dir_path)
    make_dir_if_not_exist(dest_dir_path)
               
    for file_path in file_path_l:
        shutil.copy(file_path, dest_dir_path )
        
'''copies then deletes'''
def move_files_to_dest(file_path_l, dest_dir_path): 
    copy_files_to_dest(file_path_l, dest_dir_path)
    
    for path in file_path_l:
        delete_if_exists(path)






"""VVVVVVVVVV                                                 VVVVVVVVVV"""
"""VVVVVVVVVV  Operate on or move given objects in GIVEN DIR  VVVVVVVVV"""
"""VVVVVVVVVV                                                 VVVVVVVVVV"""


def delete_all_files_in_dir(dir_path):
    for the_file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
def delete_all_dirs_in_dir_if_exists(dir_path):
    if os.path.exists(dir_path):
        for the_file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, the_file)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
    



            
            
# works for files and dirs



        
        
        
        
"""VVVVVVVVVV                              VVVVVVVVVV"""
"""VVVVVVVVVV Get info about or edit path  VVVVVVVVVV"""
"""VVVVVVVVVV                              VVVVVVVVVV"""


def is_path_creatable(pathname):
    '''
    `True` if the current user has sufficient permissions to create the passed
    pathname; `False` otherwise.
    '''
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)

# returns true if path could be created and ends with ext

def is_file_path_valid(path, extension = None):
    if not is_path_creatable(path):
        return False
    if extension != None and not path.endswith(extension):
        return False
    return True
    
""" returns given path with replaced extension: mp4, jpg, ect... """
def replace_extension(in_file_path, new_extension):  
    path_split = os.path.splitext(in_file_path)
    
    if len(path_split) < 2:
        raise Exception("ERROR:  in_file_path must contain at least 1 '.'")
    
    new_path = ''
    for str in path_split[0:-1]:
        new_path += str + '.'
    new_path += new_extension
    
    return new_path
        
''' returns T/F if 2 paths point to same place '''
def paths_equal(path_1, path_2):
    return os.path.abspath(path_1) == os.path.abspath(path_2)

def get_abs_path_from_rel_path(in_rel_path):
    return os.path.abspath(in_rel_path)
    
def get_basename_from_path(path):
    return ntpath.basename(path)

def get_parent_dir_from_path(path):
    return os.path.dirname(path)
    
"""VVVVVVVVVV WORKING VVVVVVVVV"""


 
if __name__ == '__main__':
    print(os.path.abspath(""))
#     print(get_names_of_files_in_dir("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data"))
    
#     print(glob.glob("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data" + '/*') )# * means all if need specific format then *.csv)
#     print(paths_equal('ptest.py', "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools\\ptest.py"))
#     print(rename_file_overwrite('ptest.py', "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools\\ptest.py"))
    
    
    
    
#     in_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids"
#     out_parent_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\out_dir"
#     aaa_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\out_dir\\test_vids\\aaa.sss"
#     mkv_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Screen_MAKE_SUERE_THIS_WORKS_WITH_SPACE.mkv"
#     l = ['.avi', '.mkv']
#     
#     print(replace_extension(mkv_path, 'mp4'))
#     
# #     print(get_file_extension(mkv_path) in l)
#     
#     
# #     print(get_file_extension(aaa_path))

