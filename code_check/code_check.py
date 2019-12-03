from tkinter import Tk

import stores

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





code_str_l = get_code_str_l_from_clipboard()
print(code_str_l)


# print(clipboard.split())
# # print(clipboard)
# 
# s = stores.Skyzone()
# s.parse_codes(clipboard)
# # print(s.code)