import keyboard
# import time
import os
import shutil
 
import psutil


 
def wait_for_hotkey_to_be_pressed(hotkey):
    def is_file(in_path):
        return os.path.isfile(in_path)
    
    def delete_if_exists(path):
        while(True):
            print('in del_if_exists')#1``````````````````````````````````````````````````````````````
            try:
                if os.path.exists(path):
                    if   os.path.isdir(path):
                        shutil.rmtree(path)
                    elif os.path.isfile(path):
                        os.remove(path)
                    else:
                        raise Exception('ERROR:  Gave something that is not a file or a dir, bad path: ', path)
            except(PermissionError):
                print('failed to del file')
            
    def get_names_of_files_in_dir(in_dir_path):
        file_name_l = []
        
        for r, d, f in os.walk(in_dir_path):
            for file in f:
                file_name_l.append(file)
        return file_name_l
    
    def has_handle(fpath):
        for proc in psutil.process_iter():
            try:
                for item in proc.open_files():
                    if fpath == item.path:
                        return True
            except Exception:
                pass
    
        return False
    
    
    def pressed():
        print('in hotkey_utils, hotkey pressed!')
        while(True):
#             try:
            open(file_path, 'a').close()
            return
#             except(PermissionError):
#                 pass
        
    def get_file_path():
        file_num = 0
        
        file_path = 'zzz_waiting_file__' + str(file_num) + '.txt'
        while(is_file(file_path)):
            file_num += 1
            
        return file_path

        
#     file_path = get_file_path()
    file_path = 'file.txt'
    print('in hotkey utils, file_path: ', file_path)#```````````````````````````````````````````
    
#     while(has_handle(file_path)):
#         print('has handle')
#         pass
    
    delete_if_exists(file_path)
        
    keyboard.add_hotkey(hotkey, pressed)
    
    while(True):
#         print('checking if file exists')
        if is_file(file_path):
            delete_if_exists(file_path)
            return
        
        
if __name__ == '__main__':
    wait_for_hotkey_to_be_pressed('ctrl+v')
    print('passed hotkey press')
    wait_for_hotkey_to_be_pressed('ctrl+v')
    print('passed hotkey press')
    wait_for_hotkey_to_be_pressed('ctrl+v')
    print('passed hotkey press')
    wait_for_hotkey_to_be_pressed('ctrl+v')
    print('passed hotkey press')

    

    
    
    
    
    
    
    
    
    
