import json_logger
import pil_utils as pu
import barcode_utils  

# to import from parent dir 
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) 
# from parent dir
import file_system_utils as fsu
import project_vars as pv

# FONT_NAME = 'SourceCodePro-Semibold'
# FONT_NAME = 'SourceCodePro-Bold'#
# FONT_NAME = 'Consolas'#
# FONT_NAME = 'cour'
# FONT_NAME = 'Everson Mono Bold'
# FONT_NAME = 'Everson Mono'
# FONT_NAME = 'LiberationMono-Bold'#
# FONT_NAME = ''
# FONT_PATH = pv.FONTS_DIR_PATH + '\\' + FONT_NAME + '.ttf'

BACKGROUND_COLOR = (255, 255, 255)
COLOR_NORMILIZATION_FACTOR = 10
TEMPLATE_BOX_COORDS_JSON_PATH = 'template_box_coords.json'

# to get, make img in power point, open in paint, use eye drop tool, click edit colors
TEMPLATE_COLORS_DD = {
                        'g_card_pin_biz_id': {
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
                                                'value'     : (255, 0, 0)
                                              }
                     }

CT_BLACK_LBL_PARAM_D = {      'color'             : (0, 0, 0),
                              'font_name'         : 'LiberationMono-Bold',
                              'txt_box_horz_align': 'centered',
                              'txt_box_vert_align': 'top',
                              'txt_horz_align'    : 'centered',
                            }

CC_BLACK_LBL_PARAM_D = {      'color'             : (0, 0, 0),
                              'font_name'         : 'LiberationMono-Bold',
                              'txt_box_horz_align': 'centered',
                              'txt_box_vert_align': 'centered',
                              'txt_horz_align'    : 'centered',
                            }

INSTRUC_PARAM_D            = {'color'             : (101, 101, 101), # grey
                              'font_name'         : 'Consolas',
                              'txt_box_horz_align': 'centered',
                              'txt_box_vert_align': 'centered',
                              'txt_horz_align'    : 'centered',
                             }

BLANK_TEMPLATE_LBL_D = {'pin_lbl'   : {'txt_lines' : ['  Pin:  '],
                                       'param_d'   : CT_BLACK_LBL_PARAM_D},
                        'biz_id_lbl': {'txt_lines' : ['Business', 'ID:'],
                                       'param_d'   : CT_BLACK_LBL_PARAM_D}}





TEMPLATE_DIMS = (492, 1091)
TEMPLATE_DIMS_STR = str(TEMPLATE_DIMS[0]) + 'x' + str(TEMPLATE_DIMS[1])
TEMPLATE_DIMS_DIR_PATH = pv.CODE_CARDS_DIR_PATH + '\\' + TEMPLATE_DIMS_STR
    

def get__color_template_img_path(template_type):            return TEMPLATE_DIMS_DIR_PATH + '\\color_template__'             + template_type + '.png'
def get__normalized_color_template_img_path(template_type): return TEMPLATE_DIMS_DIR_PATH + '\\color_template__normalized__' + template_type + '.png'
def get__blank_template_img_path(template_type):            return TEMPLATE_DIMS_DIR_PATH + '\\blank_template__'             + template_type + '.png'
def get__blank_store_template_img_path(store_name):         return TEMPLATE_DIMS_DIR_PATH + '\\blank_store_template__'       + store_name    + '.png'

def get__test_mode_blank_template_img_path(template_type):    return TEMPLATE_DIMS_DIR_PATH + '\\blank_template_TEST_MODE__'       + template_type + '.png'
def get__test_mode_blank_store_template_img_path(store_name): return TEMPLATE_DIMS_DIR_PATH + '\\blank_store_template_TEST_MODE__' + store_name    + '.png'

    
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
    
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
            img = pu.open_img(color_template_img_path)
            # power point likes to add new colors to images so first, need to normalize all colors by dominant - 
            # meaning that if you have 100 (255, 255, 255) pixels and 50 (255, 255, 254) pixels, replace all with (255, 255, 255)
            print('    Normalizing colors of original color_template_img by dominant...')
            img = pu.normalize_colors__by_dominant(img, COLOR_NORMILIZATION_FACTOR)
            
            # sometimes the new colors added by power point out-number the original colors, so use same method to normalize
            # all colors in img to the list of box colors
            box_color_l = TEMPLATE_COLORS_DD[template_type].values()
            print('    Normalizing those colors by list...')
            img = pu.normalize_colors__by_l(img, box_color_l, COLOR_NORMILIZATION_FACTOR)
            
            print('    Saving new normalized_color_template_img at ', normalized_color_template_img_path, '...')
            img.save(normalized_color_template_img_path)
        
        # get box coords from normalized_color_template_img
        normalized_color_template_img = pu.open_img(normalized_color_template_img_path)
        print('  Getting box coords from normalized_color_template_img...')
        box_coords = pu.get_box_coords_d(normalized_color_template_img, TEMPLATE_COLORS_DD[template_type])
#         print(box_coords)#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
        
        dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type] = box_coords
        json_logger.write(dim_template_box_coords_ddd, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    return dim_template_box_coords_ddd[TEMPLATE_DIMS_STR][template_type]




def write_txt_d_to_img_in_box_coords(img, box_title, txt_d, box_coords):
    txt_param_d = txt_d['param_d']
#         print('in write_txt_d_to_img, txt_d: ', txt_d)#``````````````````````````````````````````````````````````````````````````````````
    print(box_title)#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#     print('box_coords[box_title]: ', box_coords[box_title])#``````````````````````````````````````````````````````````
    img = pu.write_txt_on_img_in_box_coords(img,                                                           
                                            box_coords_tup  = box_coords[box_title], 
                                            lines           = txt_d['txt_lines'],
                                            txt_color       = txt_param_d['color'],
                                            font_path       = pv.FONTS_DIR_PATH + '\\' + txt_param_d['font_name'] + '.ttf',
                                            txt_box_h_align = txt_param_d['txt_box_horz_align'],
                                            txt_box_v_align = txt_param_d['txt_box_vert_align'],
                                            txt_h_align     = txt_param_d['txt_horz_align'],
                                            )
    return img


def write_txt_dd_to_img(img, txt_dd, template_type_box_coords):
    for box_title, txt_d in txt_dd.items():
        img = write_txt_d_to_img_in_box_coords(img, box_title, txt_d, template_type_box_coords)
    return img



def make_new_blank_store_template(kwargs, box_coords, test_mode):
    store_name    = kwargs['store_name']
    template_type = kwargs['template_type']
    
    normalized_color_template_img_path = get__normalized_color_template_img_path(template_type)
    
    if test_mode:
        blank_template_img_path            = get__test_mode_blank_template_img_path(template_type)
        blank_store_template_img_path      = get__test_mode_blank_store_template_img_path(store_name)
    else:
        blank_template_img_path            = get__blank_template_img_path(template_type)
        blank_store_template_img_path      = get__blank_store_template_img_path(store_name)
    
    
    # after getting the box coords from the color_template_img, replace all color boxes with background color to make
    # blank template that will be used to make blank store templates
    def make_new_blank_template(template_type):
        img = pu.open_img(normalized_color_template_img_path)
        box_color_l = TEMPLATE_COLORS_DD[template_type].values()

        # now that all the boxes should be all 1 color and match the defined box_colors, replace all color boxes with
        # background color to make blank template that will be used to make blank store templates
        if not test_mode:
            img = pu.replace_colors(img, box_color_l, BACKGROUND_COLOR)
        
        # add blank template labels
        box_title_l = TEMPLATE_COLORS_DD[template_type].keys()
        

        print('        Writing labels to blank_template_img...')
        for box_title in box_title_l:
            if box_title in BLANK_TEMPLATE_LBL_D.keys():
                img = write_txt_d_to_img_in_box_coords(img, box_title, BLANK_TEMPLATE_LBL_D[box_title], box_coords)
                                                
        img.save(blank_template_img_path)
        
        
    def build_txt_dd(kwargs, box_coords):    
        txt_dd = {}
       
        # add instruc
        if 'instruc_type' in kwargs.keys() and 'instruc' in box_coords.keys():
            instruc_path = pv.INSTRUC_TXT_DIR_PATH + '\\' + kwargs['instruc_type'] + '.txt'
            fsu.raise_exception_if_object_not_exist(instruc_path, "ERROR:  No txt file exists for instruc_type: " + kwargs['instruc_type'] + 'at ' + instruc_path)
            
            txt_dd['instruc'] = {'txt_lines' : read_text_file(instruc_path),
                                 'param_d'   : INSTRUC_PARAM_D}

        # biz_id
        box_title = 'biz_id' 
        if str_in_keys_of_all(box_title, [kwargs, box_coords]):
            txt_dd[box_title] = {'txt_lines' : [kwargs['biz_id']],
                                 'param_d'   : CC_BLACK_LBL_PARAM_D}
    
        return txt_dd


    
    if not fsu.is_file(blank_template_img_path):
        print('      Blank_template_img does not already exist, creating it now...')
        make_new_blank_template(template_type)
    
    # make blank_store_template_img
    img = pu.open_img(blank_template_img_path)
    
    # write txt to img
    txt_dd = build_txt_dd(kwargs, box_coords)
    img = write_txt_dd_to_img(img, txt_dd, box_coords)
    
        
    # add images        
    if 'logo' in TEMPLATE_COLORS_DD[template_type]:
        # if trimmed logo does not exist, make it by trimming original logo img
        trimmed_logo_img_path = pv.TRIMMED_LOGOS_DIR_PATH + '\\' + store_name + '__trimmed_logo.jpg'
         
        if not fsu.is_file(trimmed_logo_img_path):
            print('      Trimmed_logo_img does not exist, trimming border of og_logo_img...')
            og_logo_img_path = pv.OG_LOGOS_DIR_PATH + '\\' + store_name + '__og_logo.jpg'
            fsu.raise_exception_if_object_not_exist(og_logo_img_path, 'ERROR:  Logo img for ' + store_name + ' does not exist at ' + og_logo_img_path)
             
            logo_img = pu.open_img(og_logo_img_path)
            logo_img = pu.trim_border(logo_img)
            logo_img.save(trimmed_logo_img_path)
         
        trimmed_logo_img = pu.open_img(trimmed_logo_img_path)
             
        pu.paste_nicely_in_box_coords(trimmed_logo_img, img, box_coords['logo'], 'centered', 'centered')
    
    #             img = pu.open_img("C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\color_template__normalized__g_card.png")
    #             pu.paste_nicely_in_box_coords(logo_img, img, box_coords['logo'], 'centered', 'centered')
    img.save(blank_store_template_img_path)
     
def str_in_keys_of_all(str_to_check, dict_list):
    for d in dict_list:
        if str_to_check not in d.keys():
            return False
    return True
        
def make_new_code_card(kwargs, box_coords, blank_store_template_img):
    def build_txt_dd(kwargs):
        txt_dd = {}
        
        default_txt_d_setup_box_title_l = ['main_code', 'pin']
        for box_title in default_txt_d_setup_box_title_l:
            if str_in_keys_of_all(box_title, [kwargs, box_coords]):
                txt_dd[box_title] = {'txt_lines' : [kwargs[box_title]],
                                     'param_d'   : CC_BLACK_LBL_PARAM_D}
            
        box_title = 'value'
        if str_in_keys_of_all(box_title, [kwargs, box_coords]):
            txt_dd[box_title] = {'txt_lines' : ['Value: $' + kwargs[box_title]],
                                 'param_d'   : CC_BLACK_LBL_PARAM_D}
        
        return txt_dd
        
    def build_img_dd(kwargs):
        img_dd = {}
        
        if 'main_code' in kwargs.keys():
            img_dd['barcode'] = {'img' : barcode_utils.get_barcode_img(kwargs['main_code']),
                                 'horz_align' : 'centered',
                                 'vert_align' : 'centered'}
        return img_dd
            
                
    img = blank_store_template_img
        
    # write txt to img
    txt_dd = build_txt_dd(kwargs)
    print('in make_code_card, txt_dd: ', txt_dd)#```````````````````````````````````````````````````````````````````````````````
    write_txt_dd_to_img(img, txt_dd, box_coords)

        
    # paste imgs to img
    img_dd = build_img_dd(kwargs)
    for box_title, img_d in img_dd.items():
        img = pu.paste_nicely_in_box_coords(img_d['img'], img, box_coords[box_title], img_d['horz_align'], img_d['vert_align'])
        
#     img = pu.paste_nicely_in_box_coords(top_img, background_img, box_coords, horz_align, vert_align)
        
    return img


    
    
def make_code_card(kwargs, test_mode):
    template_type = kwargs['template_type']
    store_name = kwargs['store_name']
        
    img_paths_to_delete_l = [get__test_mode_blank_store_template_img_path(store_name),
                             get__test_mode_blank_template_img_path(template_type)]
    if test_mode:
        # remove the needed box coords from the json file if it exists
        if fsu.is_file(TEMPLATE_BOX_COORDS_JSON_PATH):
            dim_template_box_coords_ddd = json_logger.read(TEMPLATE_BOX_COORDS_JSON_PATH)
    
            if TEMPLATE_DIMS_STR in dim_template_box_coords_ddd:
                dim_template_box_coords_ddd.pop(TEMPLATE_DIMS_STR)
            
                json_logger.write(dim_template_box_coords_ddd, TEMPLATE_BOX_COORDS_JSON_PATH)
                
        # remove imgs so they get re-made
#         img_paths_to_delete_l = [get__normalized_color_template_img_path(template_type),
#                                  get__blank_template_img_path(template_type),
#                                  get__blank_store_template_img_path(store_name)]
        img_paths_to_delete_l.append(get__normalized_color_template_img_path(template_type))
        img_paths_to_delete_l.append(get__blank_template_img_path(template_type))
        img_paths_to_delete_l.append(get__blank_store_template_img_path(store_name))

    
    img_paths_to_delete_l.append(get__test_mode_blank_store_template_img_path(store_name))
    img_paths_to_delete_l.append(get__test_mode_blank_template_img_path(template_type))
                                 
            
    for img_path in img_paths_to_delete_l:
        fsu.delete_if_exists(img_path)
            
    
    # get template_type_box_coords from json file
        # if the json file does not exist, it will be created
        # if the box_coords are not in the json file, they will be loaded from the normalized_color_template_img
            # if the normalized_color_template_img does not exist, it will be created from the user-made color_template_img
    print('  Getting template_type_box_coords...')
    template_type_box_coords = get_template_type_box_coords(template_type)
    
    for box_title, box_coords in template_type_box_coords.items():
        print(box_title + ' : ' + str(box_coords))
    
     
    # get blank_store_template_img from path
        # if blank_store_template image does not exist, make it
            # if blank_template_img does not already exist, it will be created in the process
    print('  Getting blank_store_template_img...')
    if test_mode:
        blank_store_template_img_path = get__test_mode_blank_store_template_img_path(store_name)
    else:
        blank_store_template_img_path = get__blank_store_template_img_path(store_name)
        
    print('blank_store_template_img_path: ', blank_store_template_img_path)#```````````````````````````````````````````````````````````
    
     
    if not fsu.is_file(blank_store_template_img_path):
        print('    Blank_store_template_img does not exist, creating it now...')
        make_new_blank_store_template(kwargs, template_type_box_coords, test_mode)
#     else:
    blank_store_template_img = pu.open_img(blank_store_template_img_path)
#     blank_store_template_img.show()
    
    print('  Making new code_card_img...')
    return make_new_code_card(kwargs, template_type_box_coords, blank_store_template_img)
    
    
    

    
def main():
    TEST_MODE = False
    
    kwargs = {'store_name'    : 'jimmy_johns',
              'main_code'     : '6050110010041436106',
              'pin'           : '953',
              'biz_id'        : '66276',
              'value'         : '25',
              'bonus'         : False,
              'template_type' : 'g_card_pin_biz_id',
              'instruc_type'  : 'add_code_or_receipt'
              }
    
    code_card_img = make_code_card(kwargs, TEST_MODE)
    code_card_img.show()
#     code_card_img.save(pv.CODE_CARDS_DIR_PATH + '\\blank_store_template__'       + store_name    + '.png')
     
     
     
#     print(box_coords)
     
#     make_new_store_code_card_template('jimmy_johns', 'g_card', [None], instruc_path = 'app_or_recipt')
     
     
    
if __name__ == '__main__':
    main()
    
#     test_d = {'492x1091': {'g_card': {'logo': (5,6,7,8),
#                                       'barcode' : (6,7,8,9)}}}
#     json_logger.write(test_d, TEMPLATE_BOX_COORDS_JSON_PATH)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    