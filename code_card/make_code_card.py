import json_logger
import pil_utils

# to import from parent dir 
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu
import project_vars as pv

TEMPLATE_BOX_COORDS_JSON_PATH = 'template_box_coords.json'

# to get, make img in power point, open in paint, use eye drop tool, click edit colors
TEMPLATE_COLORS_DD = {
                        'g_card': {
                                   'logo'      : (90, 155, 213),
                                   'barcode'   : (69, 234, 113),
                                    'main_code' : (243, 62, 203),
                                    'instruc'   : (237, 224, 68),
                                    'pin_lbl'   : (56, 79, 247),
                                    'biz_id_lbl': (181, 163, 123),
                                    'pin'       : (53, 212, 251),
                                    'biz_id'    : (167, 88, 216),
                                    'bonus_msg' : (111, 193, 121),
                                    'extra'     : (219, 107, 83),
                                    'value'     : (149, 155, 155)
                                  }
                     }

TEMPLATE_DIMS = (492, 1091)
TEMPLATE_DIMS_STR = str(TEMPLATE_DIMS[0]) + 'x' + str(TEMPLATE_DIMS[1])
TEMPLATE_DIMS_DIR_PATH = pv.CODE_CARDS_DIR_PATH + '\\' + TEMPLATE_DIMS_STR


 

# def make_code_card(store_name, template_type, main_code, pin):


def make_new_store_code_card_template(store_name, template_type, options_l, instruc_type):
    blank_store_template_img_path = TEMPLATE_DIMS_DIR_PATH + '\\blank_store_template__' + store_name    + '.jpg'
    color_template_img_path       = TEMPLATE_DIMS_DIR_PATH + '\\color_template__'       + template_type + '.JPG'
    blank_template_img_path       = TEMPLATE_DIMS_DIR_PATH + '\\blank_template__'       + template_type + '.JPG'
    
    def get_template_type_box_coords(template_type):
        # read in data from json file if it exists
        if fsu.is_file(TEMPLATE_BOX_COORDS_JSON_PATH):
            dim_template_box_coords_ddd = json_logger.read(TEMPLATE_BOX_COORDS_JSON_PATH)
        else:
            dim_template_box_coords_ddd = {}
        
        # add template dims to ddd if not already exist 
        if TEMPLATE_DIMS_STR not in dim_template_box_coords_ddd:
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR] = {}
            
#         template_box_coords_dd = dim_template_box_coords_ddd[TEMPLATE_DIMS_STR]
        
        # add template_type if needed
        if template_type not in dim_template_box_coords_ddd[TEMPLATE_DIMS_STR]:
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = {}
            
        # if box coords don't already exist for template type, get them from image, also log in json file
        if dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] == {}:
#             color_template_img_path = TEMPLATE_DIMS_DIR_PATH + '\\color_template__' + template_type + '.JPG'
            
            # raise exception if color template img does not exist
            if not fsu.is_file(color_template_img_path):
                raise Exception('ERROR:  color_template_img_path does not exist: ', color_template_img_path, 
                                '/ncannot get box_coords, maybe add a good way of adding new color templates here')
                
            print('  in get_template_type_box_coords(), getting box coords from color template img...')
            color_template_img = pil_utils.open_img(color_template_img_path)
            box_coords = pil_utils.get_box_coords_d(color_template_img, TEMPLATE_COLORS_DD[template_type])
            
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = box_coords
            json_logger.write(dim_template_box_coords_ddd, TEMPLATE_BOX_COORDS_JSON_PATH)
        
        return dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type]





    def make_new_blank_store_template(box_coords, store_name, template_type, instruc_type):
        
        def make_new_blank_template(template_type):
            color_template_img = pil_utils.open_img(color_template_img_path)
            
            # replace all box colors with white
#             replaced_color_img = pil_utils.replace_colors(color_template_img, TEMPLATE_COLORS_DD[template_type].values(), (255, 255, 255)) # his does not work!!!!!!!!!!!!!!!!!!!!

            replaced_color_img = pil_utils.replace_all_colors_except(color_template_img, [(0,0,0)], (255,255,255))
            replaced_color_img.show()
            
            
        
        if not fsu.is_file(blank_template_img_path):
            make_new_blank_template(template_type)
        
        
        
        
        
    box_coords = get_template_type_box_coords(template_type)
    print(box_coords)
    
    
    if not fsu.is_file(blank_store_template_img_path):
        make_new_blank_store_template(box_coords, store_name, template_type, instruc_type)
    
    
    
    
    
    
    
    
    
    
def main():
    make_new_store_code_card_template('jimmy_johns', 'g_card', [None], instruc_type = 'app_or_recipt')
    
    
    
if __name__ == '__main__':
    main()
    
#     test_d = {'492x1091': {'g_card': {'logo': (5,6,7,8),
#                                       'barcode' : (6,7,8,9)}}}
#     json_logger.write(test_d, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    