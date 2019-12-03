# PID or PI on final
# block reduction 



import Store
import re

# 6050110010020386261-304480:12 | $25.00
# 6050110010020383210-304480:97 | $25.00

# 6050110010068394475-95704:630 | $60.00



# 6050110010068396936-95704:513 | $53.17 
class Skyzone(Store.Store):

    
    def __init__(self):
        # required 
        self.name = 'skyzone'
        self.url = 'https://sztallahassee.cardfoundry.com/giftcards.php?action=card_balance'
        
        # optional
        self.code_parse_dim_l = ['-', ':', ' | $']
#         
#         self.code = None
#         self.pin  = None
#         self.id   = None
#         
        
    
    def parse_code_str_l(self, code_str_l):
        return self.parse_code_str_l_____code_id_pin_val(code_str_l)
        
        
#         code_d = {}
#         for code_str in code_str_l:
#             split_code_l = Store.multi_dim_split(['-', ':', ' | $'], code_str)
#             print(split_code_l)
# # #             s_code_str = code_str.split('-', ':' )
# #             s_code_str = re.split('-|:| ', code_str).split
# #             print('s_code_str: ' ,s_code_str )#`````````````````````````````````````````````````````
# #         
        

        
if __name__ == '__main__':
    import code_check
    code_check.main()

