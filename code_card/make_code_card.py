import json_logger
import pil_utils

# to import from parent dir 
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu
import project_vars as pv

BACKGROUND_COLOR = (255, 255, 255)
COLOR_NORMILIZATION_FACTOR = 10
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


def make_new_store_code_card_template(store_name, template_type, options_l, instruc_type = None, ):
    blank_store_template_img_path      = TEMPLATE_DIMS_DIR_PATH + '\\blank_store_template__'       + store_name    + '.png'
    color_template_img_path            = TEMPLATE_DIMS_DIR_PATH + '\\color_template__'             + template_type + '.png'
    normalized_color_template_img_path = TEMPLATE_DIMS_DIR_PATH + '\\color_template__normalized__' + template_type + '.png'
    blank_template_img_path            = TEMPLATE_DIMS_DIR_PATH + '\\blank_template__'             + template_type + '.png'
    
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
                
            # normalize the colors of the original color_template_img if not already done
            if not fsu.is_file(normalized_color_template_img_path):
                print('  Normalized_color_template_img does not exist, creating it now...')
                img = pil_utils.open_img(color_template_img_path)
                # power point likes to add new colors to images so first, need to normalize all colors by dominant - 
                # meaning that if you have 100 (255, 255, 255) pixels and 50 (255, 255, 254) pixels, replace all with (255, 255, 255)
                print('    Normalizing colors of original color_template_img by dominant...')
                img = pil_utils.normalize_colors__by_dominant(img, COLOR_NORMILIZATION_FACTOR)
                
                # sometimes the new colors added by power point out-number the original colors, so use same method to normalize
                # all colors in img to the list of box colors
                box_color_l = TEMPLATE_COLORS_DD[template_type].values()
                print('    Normalizing those colors by list...')
                img = pil_utils.normalize_colors__by_l(img, box_color_l, COLOR_NORMILIZATION_FACTOR)
                
                print('    Saving new normalized_color_template_img at ', normalized_color_template_img_path, '...')
                img.save(normalized_color_template_img_path)
            
            # get box coords from normalized_color_template_img
            normalized_color_template_img = pil_utils.open_img(normalized_color_template_img_path)
            print('  Getting box coords from normalized_color_template_img...')
            box_coords = pil_utils.get_box_coords_d(normalized_color_template_img, TEMPLATE_COLORS_DD[template_type])
            
            dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = box_coords
            json_logger.write(dim_template_box_coords_ddd, TEMPLATE_BOX_COORDS_JSON_PATH)
        
        return dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type]

    def make_new_blank_store_template(box_coords, store_name, template_type, instruc_type):
        # after getting the box coords from the color_template_img, replace all color boxes with background color to make
        # blank template that will be used to make blank store templates
        def make_new_blank_template(template_type):
            print('  Making new blank_template_img for type: ', template_type, '...')
            img = pil_utils.open_img(normalized_color_template_img_path)
            box_color_l = TEMPLATE_COLORS_DD[template_type].values()

            # now that all the boxes should be all 1 color and match the defined box_colors, replace all color boxes with
            # background color to make blank template that will be used to make blank store templates
            print('    Replacing box colors with background color, ', BACKGROUND_COLOR, '...')
            img = pil_utils.replace_colors(img, box_color_l, BACKGROUND_COLOR)
            
            print('    Saving new blank_template_img...')
            img.save(blank_template_img_path)
            img.show()

        
        if not fsu.is_file(blank_template_img_path):
            print('  Blank template does not already exist, making one now...')
            make_new_blank_template(template_type)
        
        raise Exception('blank template already made, work on this part now')
        
        
        
        
        
    print('  Getting box_coords for template type: ', template_type, ' of size: ', TEMPLATE_DIMS_STR, '...')
    box_coords = get_template_type_box_coords(template_type)
    
    if not fsu.is_file(blank_store_template_img_path):
        print('  Blank_store_template_img does not exist, making it now...')
        make_new_blank_store_template(box_coords, store_name, template_type, instruc_type)
    
    
    
    

def get__blank_store_template_img_path(store_name):         return TEMPLATE_DIMS_DIR_PATH + '\\blank_store_template__'       + store_name    + '.png'
def get__color_template_img_path(template_type):            return TEMPLATE_DIMS_DIR_PATH + '\\color_template__'             + template_type + '.png'
def get__normalized_color_template_img_path(template_type): return TEMPLATE_DIMS_DIR_PATH + '\\color_template__normalized__' + template_type + '.png'
def get__blank_template_img_path(template_type):            return TEMPLATE_DIMS_DIR_PATH + '\\blank_template__'             + template_type + '.png'
    
    
    
    
def get_template_type_box_coords(template_type):
    color_template_img_path            = get__color_template_img_path(template_type)
    normalized_color_template_img_path = get__normalized_color_template_img_path(template_type)
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
            
        # normalize the colors of the original color_template_img if not already done
        if not fsu.is_file(normalized_color_template_img_path):
            print('  Normalized_color_template_img does not exist, creating it now...')
            img = pil_utils.open_img(color_template_img_path)
            # power point likes to add new colors to images so first, need to normalize all colors by dominant - 
            # meaning that if you have 100 (255, 255, 255) pixels and 50 (255, 255, 254) pixels, replace all with (255, 255, 255)
            print('    Normalizing colors of original color_template_img by dominant...')
            img = pil_utils.normalize_colors__by_dominant(img, COLOR_NORMILIZATION_FACTOR)
            
            # sometimes the new colors added by power point out-number the original colors, so use same method to normalize
            # all colors in img to the list of box colors
            box_color_l = TEMPLATE_COLORS_DD[template_type].values()
            print('    Normalizing those colors by list...')
            img = pil_utils.normalize_colors__by_l(img, box_color_l, COLOR_NORMILIZATION_FACTOR)
            
            print('    Saving new normalized_color_template_img at ', normalized_color_template_img_path, '...')
            img.save(normalized_color_template_img_path)
        
        # get box coords from normalized_color_template_img
        normalized_color_template_img = pil_utils.open_img(normalized_color_template_img_path)
        print('  Getting box coords from normalized_color_template_img...')
        box_coords = pil_utils.get_box_coords_d(normalized_color_template_img, TEMPLATE_COLORS_DD[template_type])
        
        dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = box_coords
        json_logger.write(dim_template_box_coords_ddd, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    return dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type]





def make_new_blank_store_template(box_coords, store_name, template_type, instruc_type):
    normalized_color_template_img_path = get__normalized_color_template_img_path(template_type)
    blank_template_img_path = get__blank_template_img_path(template_type)
    
    # after getting the box coords from the color_template_img, replace all color boxes with background color to make
    # blank template that will be used to make blank store templates
    def make_new_blank_template(template_type):
        print('  Making new blank_template_img for type: ', template_type, '...')
        img = pil_utils.open_img(normalized_color_template_img_path)
        box_color_l = TEMPLATE_COLORS_DD[template_type].values()

        # now that all the boxes should be all 1 color and match the defined box_colors, replace all color boxes with
        # background color to make blank template that will be used to make blank store templates
        print('    Replacing box colors with background color, ', BACKGROUND_COLOR, '...')
        img = pil_utils.replace_colors(img, box_color_l, BACKGROUND_COLOR)
        
        print('    Saving new blank_template_img...')
        img.save(blank_template_img_path)
        img.show()

    
    if not fsu.is_file(blank_template_img_path):
        print('  Blank template does not already exist, making one now...')
        make_new_blank_template(template_type)
    
    raise Exception('blank template already made, work on this part now')

    
def main():
    store_name = 'jimmey_johns'
    main_code_str = '6050110010041436106' 
    pin_str = '953'
    value = 25.0
    bonus = False 
    template_type = 'g_card'
    instruc_type = 'app_or_recipt'
    
    # get template_type_box_coords from json file
        # if the json file does not exist, it will be created
        # if the box_coords are not in the json file, they will be loaded from the normalized_color_template_img
            # if the normalized_color_template_img does not exist, it will be created from the user-made color_template_img
    print('  Getting template_type_box_coords...')
    template_type_box_coords = get_template_type_box_coords(template_type)
    
    # if blank_store_template image does not exist, make it
        # if blank_template_img does not already exist, it will be created in the process
    print('  Getting blank_store_template_img...')
    blank_store_template_img_path = get__blank_store_template_img_path(store_name)
    if not fsu.is_file(blank_store_template_img_path):
        print('    Blank_store_template_img does not exist, creating it now...')
        make_new_blank_store_template(template_type_box_coords, store_name, template_type, instruc_type)
    blank_store_template_img = pil_utils.open_img(blank_store_template_img_path)
    
    
    blank_store_template_img.show()
        
    
    
    
#     print(box_coords)
    
#     make_new_store_code_card_template('jimmy_johns', 'g_card', [None], instruc_type = 'app_or_recipt')
    
    
    
if __name__ == '__main__':
    main()
    
#     test_d = {'492x1091': {'g_card': {'logo': (5,6,7,8),
#                                       'barcode' : (6,7,8,9)}}}
#     json_logger.write(test_d, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    