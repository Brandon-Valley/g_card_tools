import Store

import keyboard
import time


class Jets_Pizza(Store.Store):

    
    def __init__(self):
        
        # required 
        self.name = 'Jets_Pizza'
        self.url  = 'https://www.mercury-gift.com/'
        self.csv_header_l = ['og_code_str', 'code', 'pin', 'id', 'adv_value', 'real_value', 'last_confirmed']

        
        # optional
        self.code_parse_dim_l = ['-', ':', ' | $']

        # parent init
        super(Jets_Pizza, self).__init__()
    
    def parse_code_str_l(self, code_str_l):
        return self.parse_code_str_l_____default(code_str_l)
    
    # what to do after url is opened
    # always do manual work first
    # returns clip board of value display screen 
    def single_code_check(self, code_d):
        return self.single_code_check_____clipboard_method(code_d, ['code', 'id', 'pin'])

  
    # parse the string that results from pressing ctrl+a and copying
    # on the value display screen at the end of single_code_check()
    def parse_value_display_str(self, value_display_str):
        print(value_display_str)
        split_value_display_str = Store.multi_dim_split(['Current Balance: $ ', '   View Details'], value_display_str)
        print('split_value_display_str: ', split_value_display_str)
        value_str = split_value_display_str[1]
        print('value_str: ', value_str)
        return float(value_str)
        
        

        
if __name__ == '__main__':
    import code_check
    code_check.main()
#     
#     import clipboard_tools as cb_tools
#     jj = Jimmy_Johns()
#     cb = cb_tools.get_clipboard()
#     print(jj.parse_value_display_str(cb))
    
    
    
    
    
    
    


