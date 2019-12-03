# PID or PI on final
# block reduction 



import Store
# 6050110010020386261-304480:12 | $25.00
# 6050110010020383210-304480:97 | $25.00

# 6050110010068394475-95704:630 | $60.00



# 6050110010068396936-95704:513 | $53.17 
class Skyzone(Store.Store):

    
    def __init__(self):
        self.name = 'skyzone'
        self.url = 'https://sztallahassee.cardfoundry.com/giftcards.php?action=card_balance'
        
#         
#         self.code = None
#         self.pin  = None
#         self.id   = None
#         
        
    def parse_codes(self, clipboard):
        print(clipboard)
        for code_str in clipboard:
            print('dddd' + code_str)
        
        

# 
# 
# 
# s = Skyzone()
# s.open_code_check_url()
# s.parse_codes()

