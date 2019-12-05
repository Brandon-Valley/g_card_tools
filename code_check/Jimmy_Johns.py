import Store

import keyboard
import time


class Jimmy_Johns(Store.Store):

    
    def __init__(self):
        
        # required 
        self.name = 'jimmy_johns'
        self.url  = 'https://www.mercury-gift.com/JimmyJohns/CheckBalance?Length=151'
        self.csv_header_l = ['og_code_str', 'code', 'pin', 'id', 'adv_value', 'real_value']

        
        # optional
        self.code_parse_dim_l = ['-', ':', ' | $']

        # parent init
        super(Jimmy_Johns, self).__init__()
    
    def parse_code_str_l(self, code_str_l):
        return self.parse_code_str_l_____code_id_pin_val(code_str_l)
    
    # what to do after url is opened
    # always do manual work first
    # returns clip board of value display screen 
    def single_code_check(self, code_d):
        return self.single_code_check_____clipboard_method(code_d, ['code', 'id', 'pin'])

  
    # parse the string that results from pressing ctrl+a and copying
    # on the value display screen at the end of single_code_check()
    def parse_value_display_str(self, value_display_str):
#         print(value_display_str)
        split_value_display_str = Store.multi_dim_split(['CURRENT BALANCE:\n$', '\nTRANSACTION DETAILS'], value_display_str)
#         print(split_value_display_str)
        return float(split_value_display_str[1])
        
        

        
if __name__ == '__main__':
    import code_check
    code_check.main()
#     
#     import clipboard_tools as cb_tools
#     jj = Jimmy_Johns()
#     cb = cb_tools.get_clipboard()
#     print(jj.parse_value_display_str(cb))
    
    
    
    
    
    
    


