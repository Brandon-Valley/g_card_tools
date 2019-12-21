import webbrowser
from googlesearch import search
import pyperclip
import os
from ctypes import windll
from tkinter import Tk
import time
import keyboard
from datetime import datetime

# https://www.reddit.com/r/excel/comments/4hgoky/how_to_save_csv_file_without_annoying_prompts/


import logger
import clipboard_tools as cb_tools
import hotkey_utils as hu
import str_utils


from humanfriendly.text import split

BLANK_FILE_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\make_blank_file\\blank_file.txt"
UNUSED_CODE_DIR_PATH = 'unused_codes' # eventually remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

WORKING_CSV_PARENT_DIR_PATH = ''
WORKING_CSV_FILE_NAME_HEADER = 'working__'



def copy_selection():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    
    while(True):
        print('trying...')
        try:
            keyboard.press_and_release('ctrl+a', 1)
            keyboard.press_and_release('ctrl+c', 1)
            clipboard = Tk().clipboard_get()
            return clipboard
        except:
            time.sleep(1)
            pass


    

# implemented

def func_not_implemented():
    raise Exception("ERROR:  This function has not yet been implemented")


def wait_for_user_action():
    while(not os.path.isfile(BLANK_FILE_PATH)):
#         print('waiting...')
        pass
    os.remove(BLANK_FILE_PATH)
    



class Store:
    def __init__(self):      
#         # required 
#         self.name = None
#         self.url  = None
#          
#         # optional
#         self.code_parse_dim_l = None
         
        # parent
        self.unused_codes_csv_path = UNUSED_CODE_DIR_PATH + '\\' + self.name + '__unused_codes.csv'
            
#         self.working_csv_path = WORKING_CSV_PATH_HEADER + self.name + '.csv'
#         print('in store: ', self.unused_codes_csv_path)#``````````````````````````````````````````````````````````



    def check_new_codes(self, code_str_l):
        def open_code_check_url():
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab(self.url)
            
        code_dl = self.parse_code_str_l(code_str_l)
        
        for code_d in code_dl:
            open_code_check_url()
            value_display_str = self.single_code_check(code_d)
            code_d['real_value'] = self.parse_value_display_str(value_display_str)
#             code_d['real_value'] = 30.0
            
#             print('about to log:  code_d:  ', code_d)#`````````````````````````````````````````````````````
            
            code_d['code'] = code_d['code'] + "'"
            code_d['last_confirmed'] = str(datetime.now()) + "'"
            print("code_d['last_confirmed']: ", code_d['last_confirmed'])#```````````````````````````````````````````````````````````````
#             logger.logSingle(code_d, self.working_csv_path, wantBackup = True, headerList = self.csv_header_l)
            print('code_d: ', code_d)#`````````````````````````````````````````````````````````````````````````````````````````
            print(self.csv_header_l)
            logger.logSingle(code_d, self.unused_codes_csv_path, wantBackup = True, headerList = self.csv_header_l)


    def parse_code_str_l_____default(self, code_str_l, mode_str = 'code_id_pin_val'):
        code_dl = []
        for code_str in code_str_l:
            code_d = {'og_code_str' : code_str,
                      'real_value'  : None}
                      
            split_code_l = str_utlis.multi_dim_split(self.code_parse_dim_l, code_str)
#             print('in store, split_code_l: ', split_code_l)#`````````````````````````````````````````````````````````````````
            try:
                if mode_str == 'code_id_pin_val':
                    code_d['code']      = split_code_l[0]
                    code_d['id']        = split_code_l[1]
                    code_d['pin']       = split_code_l[2]
                    code_d['adv_value'] = split_code_l[3]
                    
                elif mode_str == 'code_val':
                    code_d['code']      = split_code_l[0]
                    code_d['adv_value'] = split_code_l[1]
            except: 
                raise Exception("ERROR:  Could not split clipboard, probably dont hove codes in clipboard:  ", code_str_l)
            code_dl.append(code_d)
        return code_dl     
          
    
    
    # default for quick checks, puts values in order_l in clip board, 
    # returns clip board on last user action (user must manually copy value display
    def single_code_check_____clipboard_method(self, code_d, order_l = ['code', 'id', 'pin']):
#         print('in store: code_d: ', code_d)#``````````````````````````````````````````````````````````````````````````````````
        for str_num, str in enumerate(order_l):
#             print('in store: adding this to clipboard: ', code_d[order_l[str_num]])#``````````````````````````````````````````````````````````````````````````````````
#             print('in store: clipboard: ', cb_tools.get_clipboard())#``````````````````````````````````````````````````````````````````````````````````
                                                               
            cb_tools.copy_to_clipboard(code_d[order_l[str_num]])
#             hu.wait_for_hotkey_to_be_pressed('ctrl+v')
            wait_for_user_action()

#         hu.wait_for_hotkey_to_be_pressed('ctrl+c')
        clipboard = cb_tools.get_clipboard()
        keyboard.press_and_release('alt+tab', 1) # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
        return clipboard

if __name__ == '__main__':
    
    code_d = {'id': '66276', 'code': "6050110010041431467'", 'pin': '296', 'og_code_str': '6050110010041431467-66276:296 | $25.00',
                'real_value': 25.0, 'adv_value': '25.00'}
    code_d['last_confirmed'] = str(datetime.now()).split('.')[0]# + "'"
    print(code_d['last_confirmed'])
    
    header_l = ['og_code_str', 'code', 'pin', 'id', 'adv_value', 'real_value', 'last_confirmed']
#     header_l = ['og_code_str', 'code', 'pin', 'id', 'adv_value', 'real_value']
    unused_csv_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools\\code_check\\unused_codes\\jimmy_johns__unused_codes.csv"
    logger.logSingle(code_d, unused_csv_path, wantBackup = True, headerList = header_l)
    print('logged stuff in csv')
    
    
#     import code_check
#     code_check.main()
    
    
# 6050110010041431467-66276:296 | $25.00
    
    
    
    