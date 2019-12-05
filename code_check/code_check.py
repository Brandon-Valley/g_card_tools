from tkinter import Tk

import Skyzone
import Store

import file_system_utils as fsu

STORE_L = [Skyzone.Skyzone()]


def get_code_str_l_from_clipboard():    
    def get_clipboard():
        return(Tk().clipboard_get())
    
    cb = get_clipboard()
    split_cb = cb.split('\n')
    
    code_str_l = []
    for elm in split_cb:
        if elm != '':
            code_str_l.append(elm)
            
    return code_str_l


def get_store_from_user():
    for store_num, store in enumerate(STORE_L):
        print('    ' , str(store_num + 1) , '.  ' , store.name)
    input_num = input("Enter the # of the store: ")
    return STORE_L[int(input_num) - 1] 
        
    
    

def main():
    # clear blank file fro "next" marker if one exists
    fsu.delete_if_exists(Store.BLANK_FILE_PATH)
    
    # get store from user 
    print('codes for the store you select will be copied from your clipboard')
    store = get_store_from_user()
    
    # get codes from user's clipboard
    code_str_l = get_code_str_l_from_clipboard()
    
    # check the codes using the store's unique functions
    store.check_new_codes(code_str_l)
    
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