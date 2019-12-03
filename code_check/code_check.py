from tkinter import Tk

import stores
import Store

import file_system_utils as fsu

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
    
    
#     print(cb.split('\n'))

def main():
    fsu.delete_if_exists(Store.BLANK_FILE_PATH)
    skyzone_code_l = ['6050110010068393855-95704:679 | $30.00',
                      '6050110010068394475-95704:630 | $60.00',
                      '6050110010068396936-95704:513 | $53.17']
    
    code_str_l = skyzone_code_l
    # code_str_l = get_code_str_l_from_clipboard()
    print(code_str_l)
    
    
    # print(clipboard.split())
    # # print(clipboard)
    # 
    s = stores.Skyzone()
    s.check_new_codes(code_str_l)
    # s.parse_codes(clipboard)
    # # print(s.code)
    
    
if __name__ == '__main__':
    main()