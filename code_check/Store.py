import webbrowser
from googlesearch import search
import pyperclip
import os
import logger

BLANK_FILE_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\make_blank_file\\blank_file.txt"
UNUSED_CODE_DIR_PATH = 'unused_codes'


def multi_dim_split(dim_l, str):
    s_l = [str]
    for dim in dim_l:
        new_s_l = []
        for str in s_l:
            split_str_l = str.split(dim)
            for split_str in split_str_l:
                new_s_l.append(split_str)
        s_l = new_s_l
    return s_l
    

# implemented

def func_not_implemented():
    raise Exception("ERROR:  This function has not yet been implemented")


def wait_for_user_action():
    while(not os.path.isfile(BLANK_FILE_PATH)):
        print('waiting...')
        pass
    os.remove(BLANK_FILE_PATH)
    



class Store:
    def __init__(self):      
        # required 
        self.name = None
        self.url  = None
        
        # optional
        self.code_parse_dim_l = None
        
        # parent
        self.unused_codes_csv_path = UNUSED_CODE_DIR_PATH + '\\' + name + '__unused_codes.csv'



    def check_new_codes(self, code_str_l):
        def open_code_check_url():
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab(self.url)
            
        code_dl = self.parse_code_str_l(code_str_l)
        
        for code_d in code_dl:
            open_code_check_url()
            value_display_str = self.single_code_check(code_d)
            code_d['real_value'] = self.parse_value_display_str(value_display_str)
            logSingle(code_d, self.unused_codes_csv_path, wantBackup = True, headerList = self.csv_header_l)


    def parse_code_str_l_____code_id_pin_val(self, code_str_l):
        code_dl = []
        for code_str in code_str_l:
            code_d = {}
            split_code_l = multi_dim_split(self.code_parse_dim_l, code_str)
            code_d = {'code'        :       split_code_l[0],
                      'id'          :       split_code_l[1],
                      'pin'         :       split_code_l[2],
                      'adv_value'   : float(split_code_l[3]),
                      'og_code_str' : code_str,
                      'real_value'  : None}
            code_dl.append(code_d)
        return code_dl            
            
            

if __name__ == '__main__':
    import code_check
    code_check.main()
    
    
    
    
    
    
    