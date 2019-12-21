# from code_check import Store
from datetime import datetime


import Store
import Skyzone
import Jimmy_Johns
import Jets_Pizza
import Mcalisters_Deli

import clipboard_tools as cb_tools
import logger
import str_utils

# to import from parent dir
import sys, os
# from code_check.Store import UNUSED_CODE_DIR_PATH  # eventually move this to just this file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu
import project_vars as pv


MAX_CONFIRMED_CODE_AGE_DAYS = 0 # days

# TEMPORARY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
STORE_D = {'skyzone'         : Skyzone.Skyzone(),
           'jimmy_johns'     : Jimmy_Johns.Jimmy_Johns(),
           'jets_pizza'      : Jets_Pizza.Jets_Pizza(),
           'mcalisters_deli' : Mcalisters_Deli.Mcalisters_Deli()}

# will eventually remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
STORE_L = [Skyzone.Skyzone(),
           Jimmy_Johns.Jimmy_Johns(),
           Jets_Pizza.Jets_Pizza(),
           Mcalisters_Deli.Mcalisters_Deli()]


def get_code_str_l_from_clipboard():    
    cb = cb_tools.get_clipboard()
    split_cb = cb.split('\n')
    
    code_str_l = []
    for elm in split_cb:
        if elm != '':
            code_str_l.append(elm)
            
    return code_str_l


def get_store_from_user():
    for store_num, store in enumerate(STORE_L):
        print('      ' , str(store_num + 1) , '.  ' , store.name)
    input_num = input("  Enter the # of the store: ")
    return STORE_L[int(input_num) - 1] 
        
# returns name of store in working l filename if exists, otherwise returns false
def get_working_store_name_if_exists():
#     print('in get_working_store_name')#``````````````````````````````````````````````````````````````````````````````````
#     working_csv_parent_dir_path = fsu.get_parent_dir_from_path(Store.WORKING_CSV_PARENT_DIR_PATH + '.csv')
#     
#     abs_working_csv_parent_dir_path = fsu.get_abs_path_from_rel_path(working_csv_parent_dir_path)
#     print('abs_working_csv_parent_dir_path: ', abs_working_csv_parent_dir_path)
#     file_abs_path_l = fsu.get_abs_path_l_of_all_object_type_in_dir(abs_working_csv_parent_dir_path, 'file')
#     print(file_abs_path_l)
    file_name_l = fsu.get_dir_content_l(Store.WORKING_CSV_PARENT_DIR_PATH, object_type = 'file', content_type = 'name')
    print('file_name_l: ', file_name_l)#``````````````````````````````````````````````````````````````````````````````````````````
    for file_name in file_name_l:
        if file_name.startswith(Store.WORKING_CSV_FILE_NAME_HEADER):
            return str_utils.multi_dim_split([Store.WORKING_CSV_FILE_NAME_HEADER, '.csv'], file_name)[1]
    return False



def get__store_unused_codes_csv_path(store_name):  return pv.UNUSED_CODES_DIR_PATH + '\\' + store_name + '__unused_codes.csv'
def get__store_failed_codes_csv_path(store_name):  return pv.FAILED_CODES_DIR_PATH + '\\' + store_name + '__failed_codes.csv'


def get_confirmed_code_type_dl__and_is_complete(code_req_dl):
    # use oldest codes first, oldest codes should be at the top of the unused_codes csv
    def get_confirmed_code_dl(store_name, value, quantity):
        
        def get_datetime_from_dt_csv_str(datetime_csv_str):
            ss = str_utils.multi_dim_split(['-', ' ', ':'], datetime_csv_str)        
            return datetime(int(ss[0]), int(ss[1]), int(ss[2]), int(ss[3]), int(ss[4]), int(ss[5]))
        
        def add_to_code_d_if_exists_in_row_d(code_d, row_d, key_):
            if key_ in row_d.keys():
                code_d[key_] = row_d[key_]
            return code_d
        
        
        confirmed_code_dl = []
        
        unused_code_csv_path = get__store_unused_codes_csv_path(code_req_d['store_name'])
        print(unused_code_csv_path)#```````````````````````````````````````````````````````````````````````````````````````````````
        
        # return empty if code csv does not exist
        if not fsu.is_file(unused_code_csv_path):
            return confirmed_code_dl
        
        row_dl = logger.readCSV(unused_code_csv_path)
        store = STORE_D[store_name] # will eventually be replaced with Store(store_name) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        header_l = store.csv_header_l # will eventually get this from config !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         print(header_l)
        
        for row_num, row_d in enumerate(row_dl):
            print('row_num: ', row_num)#`````````````````````````````````````````````````````````````````````````````````````
            if float(row_d['adv_value']) == float(value):
                print(row_d['last_confirmed'])#````````````````````````````````````````````````````````````````````````````````````
                last_confirm_datetime = get_datetime_from_dt_csv_str(row_d['last_confirmed'])
#                 print(last_confirm_datetime)
                datetime_since_last_confirm = datetime.now() - last_confirm_datetime
                sec_since_last_confirm = datetime_since_last_confirm.total_seconds()
#                 print(sec_since_last_confirm)
#                 print(datetime_since_last_confirm)
            
                # if it has been too long since last check, re-check code
                if sec_since_last_confirm > MAX_CONFIRMED_CODE_AGE_DAYS * 3600:
                    # build code_d
                    code_d = {}
                    
                    header = 'main_code'
                    if header in row_d.keys():
                        code_d[header] = row_d[header][:-1]

                    code_d = add_to_code_d_if_exists_in_row_d(code_d, row_d, 'pin')
                    code_d = add_to_code_d_if_exists_in_row_d(code_d, row_d, 'biz_id')# eventually remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                     real_value = store.get_code_value(code_d) # put back !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    real_value = 12.34 # remove, just for testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    print('using ', real_value, ' as test #, should check code for real, PUT BACK' )#`````````````````````````````````````````

                    print(real_value)
                    
                    # if after checking, the real value is less than the  value, 
                    # remove the code from unused_codes and put it in failed_codes
                    if real_value < float(row_d['adv_value']):
                        logger.removeRowByRowNum(row_num, unused_code_csv_path)
                        
                        failed_codes_csv_path = get__store_failed_codes_csv_path(store_name)
                        logger.logList(row_dl, failed_codes_csv_path, wantBackup = True, headerList = header_l, overwriteAction = 'append')
                 
#                     print('here')
                
        
        
        
    
    while(len(code_req_dl) > 0):
        code_req_d = code_req_dl[0]
        confirmed_code_dl = get_confirmed_code_dl(code_req_d['store_name'], code_req_d['value'], code_req_d['quantity'])
        print(confirmed_code_dl)

    print('out')

    

def main():
    
    code_req_dl = [{'store_name' : 'jimmy_johns',
                    'value'      : 25,
                    'quantity'   : 2},
                   
                   {'store_name' : 'jets_pizza',
                    'value'      : 25,
                    'quantity'   : 2},
                   
                   {'store_name' : 'jets_pizza',
                    'value'      : 50,
                    'quantity'   : 1}
                   ]
    
    
    print(fsu.is_file(get__store_unused_codes_csv_path('jimmy_johns')))#````````````````````````````````````````````````````````````
#     print(logger.readCSV(get__store_unused_codes_csv_path('jimmy_johns')))
     
    
    confirmed_code_type_dl, is_complete = get_confirmed_code_type_dl__and_is_complete(code_req_dl)
    print('confirmed_code_type_dl: ', confirmed_code_type_dl)###########``````````````````````````````````````````````````````````````````````````
    print('is_complete: ', is_complete)#```````````````````````````````````````````````````````````````````````````````````````````````````
     
    
    
    
## DONT DELETE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     
#     # clear blank file for "next" marker if one exists
#     fsu.delete_if_exists(Store.BLANK_FILE_PATH)
#         
#     working_store_name = get_working_store_name_if_exists()
#     print('working_store_name: ', working_store_name)
#         
#     print('  Current Clipboard: ')
#     print('       ' + cb_tools.get_clipboard())
#     # get store from user 
#     print('  Codes for the store you select will be copied from your clipboard')
#     store = get_store_from_user()
#         
#     # get codes from user's clipboard
#     code_str_l = get_code_str_l_from_clipboard()
#         
#     # check the codes using the store's unique functions
#     store.check_new_codes(code_str_l)
#         
#     print('done!')
#     
#     
# #     skyzone_code_l = ['6050110010068393855-95704:679 | $30.00',
# #                     '6050110010068394475-95704:630 | $60.00',
# #                     '6050110010068396936-95704:513 | $53.17']
# #     
# #     code_str_l = skyzone_code_l
# #     # code_str_l = get_code_str_l_from_clipboard()
# #     print(code_str_l)
# #     
# #     
# #     # print(clipboard.split())
# #     # # print(clipboard)
# #     # 
# #     s = Skyzone.Skyzone()
# #     s.check_new_codes(code_str_l)
# #     print('done')
# #     # s.parse_codes(clipboard)
# #     # # print(s.code)
#     
    
if __name__ == '__main__':
    main()