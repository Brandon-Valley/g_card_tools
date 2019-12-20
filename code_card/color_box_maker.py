import pil_utils
import project_vars as pv


#                                    'logo'      : (90, 155, 213),
#                                    'barcode'   : (69, 234, 113),
#                                     'main_code' : (243, 62, 203),
#                                     'instruc'   : (237, 224, 68),
#                                     'pin_lbl'   : (56, 79, 247),
#                                     'biz_id_lbl': (181, 163, 123),
#                                     'pin'       : (53, 212, 251),
#                                     'biz_id'    : (167, 88, 216),
#                                     'bonus_msg' : (111, 193, 121),
#                                     'extra'     : (219, 107, 83),
#                                     'value'     : (149, 155, 155)


w = 300
h = 50


fill_color = (255, 0, 0)
border_color = None#(0,0,0)
border_width = 10

img_save_path = pv.COLOR_BOXES_DIR_PATH + '\\' + str(fill_color) + '__' + str(border_color) + str(w) + 'x' + str(h) + '.jpg'

img = pil_utils.make_solid_color_img((w,h), fill_color)

if border_color != None:
    img = pil_utils.add_border(img, border_width, border_color)
    
img.show()
img.save(img_save_path)
print('img saved to ', img_save_path)
    
    
    
    
    
    

