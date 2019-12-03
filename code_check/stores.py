# PID or PI on final
# block reduction 



import Store

import re
import keyboard
from tkinter import Tk
import time





# 6050110010020386261-304480:12 | $25.00
# 6050110010020383210-304480:97 | $25.00

# 6050110010068394475-95704:630 | $60.00



# 6050110010068396936-95704:513 | $53.17 
class Skyzone(Store.Store):

    
    def __init__(self):
        # required 
        self.name = 'skyzone'
        self.url  = 'https://sztallahassee.cardfoundry.com/giftcards.php?action=card_balance'
        self.csv_header_l = ['og_code_str', 'code', 'pin', 'id', 'adv_value', 'real_value']

        
        # optional
        self.code_parse_dim_l = ['-', ':', ' | $']


    def parse_code_str_l(self, code_str_l):
        return self.parse_code_str_l_____code_id_pin_val(code_str_l)
    
    # what to do after url is opened
    # always do manual work first
    # returns clip board of value display screen 
    def single_code_check(self, code_d):
        Store.wait_for_user_action()
        keyboard.press_and_release('tab', 5)
        keyboard.press_and_release('tab', .1)
        keyboard.write(code_d['code'], .1)
        keyboard.press_and_release('tab', .1)
        keyboard.write(code_d['pin'], .1)
        keyboard.press_and_release('tab', .1)
        keyboard.press_and_release('enter', .1)
        
        keyboard.press_and_release('ctrl+a', 1)
        
        # wait for value to display
        Store.wait_for_user_action()
        time.sleep(3)
        keyboard.press_and_release('ctrl+a', 1)
        keyboard.press_and_release('ctrl+a', 1)
#         Store.wait_for_user_action()
        keyboard.press_and_release('ctrl+c', 1)
#         keyboard.press_and_release('ctrl+w', .1) # close tab
        keyboard.press_and_release('alt+tab', 1) # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        return Tk().clipboard_get()
  
    # parse the string that results from pressing ctrl+a and copying
    # on the value display screen at the end of single_code_check()
    def parse_value_display_str(self, value_display_str):
        split_value_display_str = value_display_str.split('$')
        return float(split_value_display_str[-1])
        
        
#         Store.wait_for_user_action()
#         typewrite('quick brown fox')
        
                    
                    
                    
                    


        
if __name__ == '__main__':

#             # wait for value to display
#         Store.wait_for_user_action()
#         time.sleep(1)
#         keyboard.press_and_release('ctrl+a', .1)
# #         Store.wait_for_user_action()
#         keyboard.press_and_release('ctrl+c', .1)
# #         keyboard.press_and_release('ctrl+w', .1) # close tab
#         keyboard.press_and_release('alt+tab', .1) # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#         

#     keyboard.press_and_release('ctrl+a', 1)
    import code_check
    code_check.main()

