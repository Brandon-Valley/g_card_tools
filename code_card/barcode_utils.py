


from PIL import Image
from numpy import array, delete
from copy import deepcopy
 
import barcode
from barcode.writer import ImageWriter


import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
import file_system_utils as fsu
import pil_utils as pu


TEMP_BARCODE_PATH_NO_EXT = 'temp'
TEMP_BARCODE_PATH = TEMP_BARCODE_PATH_NO_EXT + '.png'
   

def get_barcode_img(code):
    # make initial bar code
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(code, writer=ImageWriter())
    # save temp barcode img, will always add .png to out_file_path_no_ext
    fullname = ean.save(TEMP_BARCODE_PATH_NO_EXT)
   
   
    # cut down bar code to make it look better
    def make_barcode_pretty(in_img_path):
        def img_to_mat(img):
            return array(img)
         
        def mat_to_img(mat, encoding='RGB'):
            """
            input: zeros((h, w, 3), dtype=uint8)
            return: img
            """
            return Image.fromarray(mat, encoding)
         
        def cut(img, h1, h2):
            """ cut lines from h1 to h2 of img """
            mat = deepcopy(img_to_mat(img))
         
            for i in range(h2 - h1):
                mat = delete(mat, h1, axis=0)
         
            return mat_to_img(mat)
         
         
        # Load image
    #     path = 'barcode.png'
        Im = Image.open(in_img_path)
         
        # cut from up to down
        Im = cut(Im, 170, 280)
#         Im = cut(Im, 50, 170)

        Im = pu.trim_border(Im)
         
#         Im.show()
#         Im.save(out_img_path)
        
        # delete temporary bar code
        fsu.delete_if_exists(TEMP_BARCODE_PATH)
        
        return Im
        
        
    return make_barcode_pretty(TEMP_BARCODE_PATH)
    # Im.show()
    
    
#     523x280
    
    
if __name__ == '__main__':
    img = get_barcode_img('6050110010041430273')
    img.show()
    
    
    
    
    
    
