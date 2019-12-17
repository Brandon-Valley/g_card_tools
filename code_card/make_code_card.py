import json_logger
import pil_utils

# to import from parent dir
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu

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


 

# def make_code_card(store_name, template_type, main_code, pin):


def make_new_store_code_card_template(store_name, template_type, options_l, instruc_type):
    def get_template_type_box_coords(template_type):
        # make json file if it doesn't already exist
        fsu.make_file_if_not_exist(TEMPLATE_BOX_COORDS_JSON_PATH)
        
        
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
    make_new_store_code_card_template('jimmy_johns', 'g_card', [None], instruc_type = 'app_or_recipt')
    
    
    
    
    
    
    
    
    
    
    
    