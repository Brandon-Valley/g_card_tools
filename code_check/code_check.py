import Store
import Skyzone
import Jimmy_Johns
import Jets_Pizza
import Mcalisters_Deli

import clipboard_tools as cb_tools

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
import file_system_utils as fsu




STORE_L = [Skyzone.Skyzone(),
           Jimmy_Johns.Jimmy_Johns(),
           Jets_Pizza.Jets_Pizza(),
           Mcalisters_Deli.Mcalisters_Deli()]


def get_code_str_l_from_clipboard():    
    cb = cb_tools.get_clipboard()
    split_cb = cb.split('\n')
    
    code_str_l = []
    for elm in split_cb:
        if elm != '':
            code_str_l.append(elm)
            
    return code_str_l


def get_store_from_user():
    for store_num, store in enumerate(STORE_L):
        print('      ' , str(store_num + 1) , '.  ' , store.name)
    input_num = input("  Enter the # of the store: ")
    return STORE_L[int(input_num) - 1] 
        
# returns name of store in working csv filename if exists, otherwise returns false
def get_working_store_name_if_exists():
#     print('in get_working_store_name')#``````````````````````````````````````````````````````````````````````````````````
#     working_csv_parent_dir_path = fsu.get_parent_dir_from_path(Store.WORKING_CSV_PARENT_DIR_PATH + '.csv')
#     
#     abs_working_csv_parent_dir_path = fsu.get_abs_path_from_rel_path(working_csv_parent_dir_path)
#     print('abs_working_csv_parent_dir_path: ', abs_working_csv_parent_dir_path)
#     file_abs_path_l = fsu.get_abs_path_l_of_all_object_type_in_dir(abs_working_csv_parent_dir_path, 'file')
#     print(file_abs_path_l)
    file_name_l = fsu.get_dir_content_l(Store.WORKING_CSV_PARENT_DIR_PATH, object_type = 'file', content_type = 'name')
    print('file_name_l: ', file_name_l)#``````````````````````````````````````````````````````````````````````````````````````````
    for file_name in file_name_l:
        if file_name.startswith(Store.WORKING_CSV_FILE_NAME_HEADER):
            return Store.multi_dim_split([Store.WORKING_CSV_FILE_NAME_HEADER, '.csv'], file_name)[1]
    return False
    

def main():
    # clear blank file fro "next" marker if one exists
    fsu.delete_if_exists(Store.BLANK_FILE_PATH)
    
    working_store_name = get_working_store_name_if_exists()
    print('working_store_name: ', working_store_name)
    
    print('  Current Clipboard: ')
    print('       ' + cb_tools.get_clipboard())
    # get store from user 
    print('  Codes for the store you select will be copied from your clipboard')
    store = get_store_from_user()
    
    # get codes from user's clipboard
    code_str_l = get_code_str_l_from_clipboard()
    
    # check the codes using the store's unique functions
    store.check_new_codes(code_str_l)
    
    print('done!')
    
#     skyzone_code_l = ['6050110010068393855-95704:679 | $30.00',
#                     '6050110010068394475-95704:630 | $60.00',
#                     '6050110010068396936-95704:513 | $53.17']
#     
#     code_str_l = skyzone_code_l
#     # code_str_l = get_code_str_l_from_clipboard()
#     print(code_str_l)
#     
#     
#     # print(clipboard.split())
#     # # print(clipboard)
#     # 
#     s = Skyzone.Skyzone()
#     s.check_new_codes(code_str_l)
#     print('done')
#     # s.parse_codes(clipboard)
#     # # print(s.code)
    
    
if __name__ == '__main__':
    main()