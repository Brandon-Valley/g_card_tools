import Store

import keyboard
import time
import clipboard_tools as cb_tools


# 6006491646202732118 | $45.50,
class Mcalisters_Deli(Store.Store):

    
    def __init__(self):
        
        # required 
        self.name = 'Mcalisters_Deli'
        self.url  = 'https://wwws-usa1.givex.com/merchant_balcheck/6522_en/'
        self.csv_header_l = ['og_code_str', 'code', 'adv_value', 'real_value']

        
        # optional
        self.code_parse_dim_l = [' | $', ',']

        # parent init
        super(Mcalisters_Deli, self).__init__()
    
    def parse_code_str_l(self, code_str_l):
        return self.parse_code_str_l_____code_id_pin_val(code_str_l, 'code_val')
    
    # what to do after url is opened
    # always do manual work first
    # returns clip board of value display screen 
    def single_code_check(self, code_d):
        return self.single_code_check_____clipboard_method(code_d, ['code'])

  
    # parse the string that results from pressing ctrl+a and copying
    # on the value display screen at the end of single_code_check()
    def parse_value_display_str(self, value_display_str, test_mode = False):
        
        if test_mode:  print([value_display_str])
        
        split_value_display_str = Store.multi_dim_split(['is:\n\n$', '\n\nView transaction history'], value_display_str)
        
        if test_mode:  print('split_value_display_str: ', split_value_display_str)
        
        value_str = split_value_display_str[1]
        
        if test_mode:  print('value_str: ', value_str)
        return float(value_str)
    
    def test_parse_value_display_str(self):
        cb = cb_tools.get_clipboard()
        print('value: ', self.parse_value_display_str(cb, test_mode = True))
        
        

        
if __name__ == '__main__':
#     import code_check
#     code_check.main()
    
    jj = Mcalisters_Deli()
    jj.test_parse_value_display_str()
#     cb = cb_tools.get_clipboard()
#     print(jj.parse_value_display_str(cb))

    
    


