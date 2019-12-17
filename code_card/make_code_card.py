import json_logger
import pil_utils

# to import from parent dir
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu
import project_vars as pv

TEMPLATE_BOX_COORDS_JSON_PATH = 'template_box_coords.json'


TEMPLATE_COLORS_D = {
                        'g_card': {
                                   'logo'      : (91, 155, 213),
                                   'barcode'   : (69, 235, 112),
                                   'main_code' : (242, 62, 203),
                                   'instruc'   : (236, 224, 68),
                                   'pin_lbl'   : (56, 79, 248),
                                   'pin'       : (53, 213, 251),
                                   'biz_id'    : (167, 88, 216),
                                   'bonus_msg' : (111, 193, 121),
                                   'extra'     : (220, 107, 84),
                                   'value'     : (149, 155, 155)
                                  }
                     }

TEMPLATE_DIMS = (492, 1091)
TEMPLATE_DIMS_STR = str(TEMPLATE_DIMS[0]) + 'x' + str(TEMPLATE_DIMS[1])
TEMPLATE_DIMS_DIR_PATH = pv.CODE_CARDS_DIR_PATH + '\\' + TEMPLATE_DIMS_STR

 

# def make_code_card(store_name, template_type, main_code, pin):


def make_new_store_code_card_template(store_name, template_type, options_l, instruc_type):
    def get_template_type_box_coords(template_type):
        # make json file if it doesn't already exist
        fsu.make_file_if_not_exist(TEMPLATE_BOX_COORDS_JSON_PATH)
        
        # read in data from json file
        dim_template_box_coords_ddd = json_logger.read(TEMPLATE_BOX_COORDS_JSON_PATH)
        
        # add template dims to ddd if not already exist
        if TEMPLATE_DIMS_STR not in dim_template_box_coords_ddd:
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR] = {}
            
#         template_box_coords_dd = dim_template_box_coords_ddd[TEMPLATE_DIMS_STR]
        
        # add template_type if needed
        if template_type not in dim_template_box_coords_ddd[TEMPLATE_DIMS_STR]:
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = {}
            
        if dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] == {}:
            box_coords = pil_utils.get_box_coords_d()
            
        
        
        
#         try:
#             template_box_coords = json_logger.read(TEMPLATE_BOX_COORDS_JSON_PATH)
#             print('MORE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#             
#         # if json file does not exist, 
#         except(FileNotFoundError):
#             
#             pil_utils.get_box_coords_d()
        
        
    box_coords = get_template_type_box_coords(template_type)
    print(box_coords)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    
#     test_d = {'492x1091': {'g_card': {'logo': (5,6,7,8),
#                                       'barcode' : (6,7,8,9)}}}
#     json_logger.write(test_d, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    
    make_new_store_code_card_template('jimmy_johns', 'g_card', [None], instruc_type = 'app_or_recipt')
    
    
    
    
    
    
    
    
    
    
    
    