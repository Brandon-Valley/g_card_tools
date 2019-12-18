from PIL import Image
from PIL import ImageDraw

import PIL.ImageFont
import PIL.ImageOps 

import numpy as np
# from fontTools.cffLib.width import font








''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Uses Direct PIL import                                                                       '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''

def open_img(path):
    return Image.open(path).convert('RGB')

# dims: (left, top, right, bottom)
# dims are the dims needed to make the box to cut out of og img, not how much to trim from each side
def crop_img(img, dims):
    return img.crop(dims)

# dims: (left, top, right, bottom)
# cuts dim amount off of og img from each side
def crop_from_each_side(img, dims):
    width, height = img.size
    return img.crop((dims[0], dims[1], width - dims[2], height - dims[3]))
    

def show_img_from_path(img_path):
    img = open_img(img_path)
    img.show()
    
    
# dims: like (5185, 4000)    

    
    
  
def invert_colors(img):
    return PIL.ImageOps.invert(img)

''' shrinks image to fit in dims, keeps aspect ratio '''
def shrink_img_to_fit_dims(img, width, height):
    img.thumbnail([width, height],Image.ANTIALIAS)
    return img

''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Non-PIL Import Tools                                                                         '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''

# does not check bounds
def rgb_tup_to_hex_str(rgb_tup):
    return '%02x%02x%02x' % (rgb_tup[0], rgb_tup[1], rgb_tup[2])

# does not check bounds
def rgb_hex_str_to_tup(rgb_hex):
    return tuple(int(rgb_hex[i:i+2], 16) for i in (0, 2, 4))

''' returns color as rgb_tup wether it is hex str or already rgb_tup '''
def color_to_rgb_tup(rgb_tup_or_hex_str):
    if isinstance(rgb_tup_or_hex_str, str):
        return rgb_hex_str_to_tup(rgb_tup_or_hex_str)
    return rgb_tup_or_hex_str

''' returns width, height of given box_coords: (top_right, top_left, bottom_right, bottom_left) '''
def get_box_coord_dims(box_coords_tup):
    width  = box_coords_tup[1][1] - box_coords_tup[0][1] 
    height = box_coords_tup[2][0] - box_coords_tup[0][0]
    return width, height 



''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Font Utils                                                                                   '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
    
def load_font(font_path = None, size = 40):
    try:
        font = PIL.ImageFont.truetype(font_path, size)
    except (IOError, AttributeError):
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')
    return font


def get_aspect_ratio_monospace(font_pth):
    dummy_font = load_font(font_pth)
    
    #the font dimensions you get from this should be the same for any single character as long as you are using a mono-spaced font
    font_dims       = dummy_font.getsize("a")
    font_width      = font_dims[0]
    font_height     = font_dims[1]
    aspect_ratio    = font_width / font_height
    return aspect_ratio


# this seems really dumb
def load_font_of_height(font_path, font_height):
    font_size = font_height
    
    while(True):
        font = load_font(font_path, font_size)
        draw = ImageDraw.Draw(img)
        char_w, char_h = draw.textsize("A", font)
        
        if char_h == font_height:
            return font
        
        font_size += 1

    
    
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Pixel Color Grid Tools                                                                       '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
    
def get_pixel_color_grid_from_path(input_img_path):
    img = open_img(input_img_path)
    return get_pixel_color_grid(img)
    
# returns a list of lists showing the rgb value of every pixel in an image
# not very efficient
def get_pixel_color_grid(input_img):
    in_img_w, in_img_h = input_img.size
    
    pixel_color_grid = []
    for y in range(in_img_h):
        row_l = []
        for x in range(in_img_w):
            rgb = input_img.getpixel((x,y))  #  <--- this is probably not efficient
            row_l.append(rgb)
        pixel_color_grid.append(row_l)
        
    return pixel_color_grid




def make_img_from_pixel_color_grid(pixel_color_grid):
    w = len(pixel_color_grid)
    h = len(pixel_color_grid[0])
    dims = (w, h)
    img = Image.new('RGB', dims, 'white')
    
    for x in range(w):
        for y in range(h):
#             print(x, y)#`````````````````````````````````````````````````````````````````````````````
            try:
                img.putpixel((x,y), pixel_color_grid[y][x])
            except(IndexError):
                img.putpixel((x,y), (255, 255, 255))
    return img
    
def show_pixel_color_grid_as_img(pixel_color_grid):
    make_img_from_pixel_color_grid(pixel_color_grid).show()
    


# scans pixel_color_grid from top and returns row num of first row to contain a pixel that 
# is different from dont_care_color color
def get_row_num_of_first_color_diff(pixle_color_grid, dont_care_color):
    for row_num, row_l in enumerate(pixle_color_grid):
        for rgb in row_l:
            if rgb != dont_care_color:
                return row_num
    raise Exception('ERROR:  image is all one color')
        


# degrees must be 90, 180, or 270
def rotate_pixel_color_grid(in_grid, degrees):
    grid_to_rotate = in_grid
    np_grid = np.rot90(grid_to_rotate, k = 4 - (degrees / 90))  
    
    new_pcg = []
    for row_l in np_grid:
        new_pcg_row_l = []
        for rgb in row_l:
            new_pcg_row_l.append(tuple(rgb))
        new_pcg.append(new_pcg_row_l)
    return new_pcg
    
def get_color_occurrence_d_from_pixel_color_grid(pcg):
    c_occ_d = {}
    
    for row in pcg:
        for pixel_color in row:
            if pixel_color in c_occ_d:
                c_occ_d[pixel_color] += 1
            else:
                c_occ_d[pixel_color] = 1
    return c_occ_d
    
# def normalize_pixel_color_grid__by_dominant(pcg, norm_factor = 100):
#     def colors_within_normilization_factior(c1, c2):
#         if abs(c1[0] - c2[0]) <= norm_factor and \
#            abs(c1[1] - c2[1]) <= norm_factor and \
#            abs(c1[2] - c2[2]) <= norm_factor and \
#            c1 != c2:
#             return True
#         return False
#      
#     clr_occ_d = get_color_occurrence_d_from_pixel_color_grid(pcg)
#  
#     sorted_clr_occ_d = sorted(clr_occ_d.items(), key=lambda clr_occ_d: clr_occ_d[1], reverse = True)
#     print(sorted_clr_occ_d)
#      
#      
#     for cur_clr_occ_tup in sorted_clr_occ_d:
#         for clr_occ_tup_num, clr_occ_tup in enumerate(sorted_clr_occ_d):
# #             print(cur_clr_occ_tup, clr_occ_tup)#``````````````````````````````````````````````````````````````````````````````
#             if colors_within_normilization_factior(cur_clr_occ_tup[0], clr_occ_tup[0]):
#                 sorted_clr_occ_d.pop(clr_occ_tup_num)
#      
#     print(sorted_clr_occ_d)    
#     print(len(sorted_clr_occ_d))    
            

''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Simple Tools                                                                                 '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''


def make_solid_color_img(dims, color, out_file_path = None):
    img = Image.new('RGB', dims, color)
    if out_file_path != None:
        img.save(out_file_path)
    return img

def pixel_color(img, x, y):
    pcg = get_pixel_color_grid(img)
    return pcg[y][x]

# border can be an int (for adding same border to all sides) or tuple (left, top, right, bottom)
def add_border(img, border, color=0):
    if isinstance(border, int) or isinstance(border, tuple):
        return PIL.ImageOps.expand(img, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')


''' returns row_offset, col_offset needed to paste given img into given dims with given alignment types '''
def get_align_paste_offset(img_w, img_h, fit_width, fit_height, horz_align = 'centered', vert_align = 'centered'):
    if  horz_align == 'left':
        col_offset = 0
    elif horz_align == 'right':
        col_offset = fit_width - img_w
    elif horz_align == 'centered':
        col_offset = (fit_width / 2) - (img_w / 2)
        
    if  vert_align == 'top':
        row_offset = 0
    elif vert_align == 'bottom':
        row_offset = fit_height - img_h
    elif vert_align == 'centered':
        row_offset = (fit_height / 2) - (img_h / 2)
        
    return int(row_offset), int(col_offset)

def get_list_of_colors_in_image(img):
    color_list = []
    pcg = get_pixel_color_grid(img)
    for row in pcg:
        for pixel_color in row:
            if pixel_color not in color_list:
                color_list.append(pixel_color)
    return color_list


def replace_color(img, og_color, new_color):
    data = np.array(img)
    
    r1, g1, b1 = og_color # Original value
    r2, g2, b2 = new_color # Value that we want to replace it with
    
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]
    
    return Image.fromarray(data)


''' probably not very efficient '''
def replace_all_colors_except(img, colors_to_not_replace_l, replacement_color):
    clr_l = get_list_of_colors_in_image(img)
    for clr in clr_l:
        if clr not in colors_to_not_replace_l:
            img = replace_color(img, clr, replacement_color)
    return img
        

 
''' if output_img_path == None, will return img, else img is saved and nothing is returned '''
def replace_colors(img, colors_to_replace_l, replacement_color):
    for clr in colors_to_replace_l:
        img = replace_color(img, clr, replacement_color)
        
    return img
     
     
     
def normalize_pixel_color_grid__by_dominant(img, norm_factor = 10):
    def colors_within_normilization_factior(c1, c2):
        if abs(c1[0] - c2[0]) <= norm_factor and \
           abs(c1[1] - c2[1]) <= norm_factor and \
           abs(c1[2] - c2[2]) <= norm_factor and \
           c1 != c2:
            print('found clr to normalize: ', c1, c2)#```````````````````````````````````````````````````````````````
            return True
        return False
    
    pcg = get_pixel_color_grid(img) 
    
    clr_occ_d = get_color_occurrence_d_from_pixel_color_grid(pcg)
  
    sorted_clr_occ_tup_l = sorted(clr_occ_d.items(), key=lambda clr_occ_d: clr_occ_d[1], reverse = True)
    
    # build sorted_clr_l
    sorted_clr_l = []
    for clr_occ_tup in sorted_clr_occ_tup_l:
        sorted_clr_l.append(clr_occ_tup[0])
               
#     # build clr_norm_d 
    clr_norm_d = {}
#     i = 0
#     while(i < len(sorted_clr_l)):
#         print('at top of while loop, size of sorted_clr_l: ', len(sorted_clr_l))#````````````````````````````````````````````````````
#         more_common_clr

    while(len(sorted_clr_l) > 1):
        most_common_color = sorted_clr_l[0]
        
        for less_common_color in sorted_clr_l[1:]:
            if colors_within_normilization_factior(most_common_color, less_common_color):
                clr_norm_d[less_common_color] = most_common_color
                sorted_clr_l.remove(less_common_color)
        sorted_clr_l.pop(0)



    
#     checked_clr_l = []
#     for more_common_clr_num, more_common_clr in enumerate(sorted_clr_l):
#         
#         for less_common_clr_num, less_common_clr in enumerate(sorted_clr_l):
#             if colors_within_normilization_factior(more_common_clr, less_common_clr):
#                 clr_norm_d[less_common_clr] = more_common_clr
#                 sorted_clr_l.pop(less_common_clr_num)
# #         checked_clr_l.append(more_common_clr)
# #         sorted_clr_l.remove(more_common_clr)
     
    # after finding the colors to normalize in clr_norm_d, go through and change the colors
    print('clr_norm_d: ', clr_norm_d)
#     img2 = img
    for old_clr, new_clr in clr_norm_d.items():
        print('replacing ', old_clr, ' with ', new_clr)#````````````````````````````````````````````````
        img = replace_color(img, old_clr, new_clr)
#         img2.show()
#     print(sorted_clr_occ_d)    
#     print(len(sorted_clr_occ_d)) 
#     return make_img_from_pixel_color_grid(pcg)
#     img2.show()
    return img
     
     
     
     
     
#  
# def normalize_pixel_color_grid__by_dominant(img, norm_factor = 100):
#     def colors_within_normilization_factior(c1, c2):
#         if abs(c1[0] - c2[0]) <= norm_factor and \
#            abs(c1[1] - c2[1]) <= norm_factor and \
#            abs(c1[2] - c2[2]) <= norm_factor and \
#            c1 != c2:
#             return True
#         return False
#     
#     pcg = get_pixel_color_grid(img)
#     clr_occ_d = get_color_occurrence_d_from_pixel_color_grid(pcg)
# 
#     sorted_clr_occ_d = sorted(clr_occ_d.items(), key=lambda clr_occ_d: clr_occ_d[1], reverse = True)
# #     print(sorted_clr_occ_d)
#     
#     
#     for cur_clr_occ_tup in sorted_clr_occ_d:
#         print
#         for clr_occ_tup_num, clr_occ_tup in enumerate(sorted_clr_occ_d):
# #             print('sfdf'  , cur_clr_occ_tup, clr_occ_tup)#``````````````````````````````````````````````````````````````````````````````
# #             print('fsf' , clr_occ_tup[0])#``````````````````````````````````````````````````````````````````````````````
# #             print('cur_clr_occ_tup[0]: ', cur_clr_occ_tup[0])#``````````````````````````````````````````````````````````````````````````````
#             
#             og_clr = cur_clr_occ_tup[0]
#             new_clr = clr_occ_tup[0]
#             if colors_within_normilization_factior(og_clr, new_clr):
#                 img = replace_color(img, og_clr, new_clr)
#     
# #     print(sorted_clr_occ_d)    
# #     print(len(sorted_clr_occ_d)) 
#     return img
 
 
#     pcg = get_pixel_color_grid(img)
#     print(pcg)
#     
#     for row_num, row in enumerate(pcg):
#         
#         print(row_num)
#         for col_num, pixel_clr in enumerate(row):
#             if pixel_clr in colors_to_replace_l:
#                 pcg[row_num][col_num] = replacement_color
#     return make_img_from_pixel_color_grid(pcg)      
    
                



''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Complex Tools                                                                                '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''


    # trims pic inward from each side until at lease one pixel in the row/col is not the same color as the original border
def trim_border(img):
    in_img = img.convert('RGB')
    
    pixel_color_grid = get_pixel_color_grid(in_img)
    border_color = pixel_color_grid[0][0]

    top_crop     = get_row_num_of_first_color_diff(pixel_color_grid, border_color)
    left_crop    = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 90), border_color)
    bottom_crop  = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 180), border_color)
    right_crop   = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 270), border_color)
     
    return crop_from_each_side(in_img, (left_crop, top_crop, right_crop, bottom_crop))


def simple_monospace_write_txt_on_img(img, lines, font, txt_color):
    draw = ImageDraw.Draw(img)
    letter_w, letter_h = draw.textsize("A", font) 
    Image.MAX_IMAGE_PIXELS = 1000000000   #need this here
    
    line_num = 0
    for line_num in range(len(lines)):
        line = lines[line_num]
        x_draw = 0
        
        for letter_num in range(len(line)):
            letter = line[letter_num]
            draw.text((x_draw, letter_h * line_num), letter, txt_color, font)
            x_draw += letter_w
        line_num += 10.
        
    return img



def write_txt_on_img_in_box_coords(img, box_coords_tup, lines, txt_color, font_path ):
    # get final aspect ratio
    longest_line_len = len(max(lines, key=len))
#     lines_aspect_ratio = longest_line_len / len(lines)
#     print(lines_aspect_ratio)
    font_aspect_ratio = get_aspect_ratio_monospace(font_path)
    print(font_aspect_ratio)
    total_aspect_ratio = (longest_line_len * font_aspect_ratio) / len(lines)

    
    box_w, box_h = get_box_coord_dims(box_coords_tup)
    print('total_aspect_ratio: ', total_aspect_ratio)#`````````````````````````````````````````````````````````````````
    
    # get font size
    print('box_w / total_aspect_ratio: ', box_w / total_aspect_ratio)
    print('box_h / len(lines): ', box_h / len(lines))

    font_h = int(min((box_w / longest_line_len) / font_aspect_ratio ,   box_h / len(lines))) 

    # get align offsets
    full_text_w = font_aspect_ratio * font_h * longest_line_len
    full_text_h = font_h * len(lines)
    
    y_align_offset, x_align_offset = get_align_paste_offset(full_text_w, full_text_h, box_w, box_h, horz_align = 'centered', vert_align = 'centered')
    
    print('offsets, x, y: ', x_align_offset, y_align_offset)#```````````````````````````````````````````````````````````````````````

    font = load_font_of_height(font_path, font_h)
    
    draw = ImageDraw.Draw(img)
    char_w, char_h = draw.textsize("A", font) # need ??? slow?????????????????????????????????????????????
    print('probably correct char_h: ', char_h, 'w: ', char_w)
    Image.MAX_IMAGE_PIXELS = 1000000000   #need this here
     
     
    for line_num, line in enumerate(lines):
        for char_num, char in enumerate(line):
            x_draw = (char_num * char_w) + box_coords_tup[0][1] + x_align_offset
            y_draw = (char_h * line_num) + box_coords_tup[0][0] + y_align_offset
            
            draw.text((x_draw, y_draw), char, txt_color, font)

    return img



''' returns the coords of the 4 corners of a box of given color
    returns false if color does not exist in img
    returns tuple: (top_right, top_left, bottom_right, bottom_left)
    box_color can be  tup or hex str
    
    scans each row horizontally until it finds the first / top line of the 
    box, then scans down on the left side until it finds the bottom left corner,
    then calculates where the bottom right corner would be
    could be made more efficient with better scanning algorithms
'''
def get_colored_box_corner_coords(img, box_color):
    box_coords = [None, None, None, None]
    rgb_tup_box_color = color_to_rgb_tup(box_color)
    pixel_color_grid = get_pixel_color_grid(img)
    
#     print('pixel_color_grid: ', pixel_color_grid)#````````````````````````````````````````````````````````````````
    
    for row_num, row in enumerate(pixel_color_grid):
#         print('scanning row #: ', row_num) #``````````````````````````````````````````````````````````````````````
        for col_num, pixel_clr in enumerate(row):
#             print(rgb_tup_box_color, pixel_clr)#````````````````````````````````````````````````````````````````````````
            
            # found top left pixel of box
            if pixel_clr == rgb_tup_box_color:
                print('in pil_utils,  found match')#```````````````````````````````````````````````````````````````````````````````
#                 return#`````````````````````````````````````````````````````````````````````````````````````````````
                top_left_coords = (row_num, col_num)
                box_coords[0] = top_left_coords

                # look for first non-box color to find top right pixel - efficient
                for col_num_minus_top_left_col_num, pixel_clr in enumerate(row[col_num:]):
                      
                    # found top right pixel of box
                    if pixel_clr != rgb_tup_box_color:
                        top_right_coords = (row_num, col_num + col_num_minus_top_left_col_num - 1)
                        box_coords[1] = top_right_coords
                        break
                      
                # if box touches left edge of image
                if box_coords[1] == None:
                    box_coords[1] = (row_num, len(row) - 1)
                                     
                
                # find bottom right pixel of box
                right_side_box_col_num = box_coords[1][1]
                for row_num_minus_top_right_row_num, row in enumerate(pixel_color_grid[row_num:]):
                    # found
                    if row[right_side_box_col_num] != rgb_tup_box_color:
                        bottom_right_coords = (row_num_minus_top_right_row_num + row_num - 1, right_side_box_col_num)
                        box_coords[3] = bottom_right_coords
                        break
                
                # if box touches bottom edge of image
                if box_coords[3] == None:
                    box_coords[3] = (len(pixel_color_grid) - 1, right_side_box_col_num)
                    
                # "calc: bottom left coords
                box_coords[2] = (box_coords[3][0], box_coords[0][1])
                
                
                return tuple(box_coords)
    
    return False
    
#     print(pixel_color_grid)



''' returns img after it resizes and pastes top_img onto background_img inside tuple of coords that forms a box 
    box_coords: (top_right, top_left, bottom_right, bottom_left) '''
def paste_nicely_in_box_coords(top_img, background_img, box_coords, horz_align = 'centered', vert_align = 'centered'):
    # resize top img to fit in box coords
    box_width, box_height = get_box_coord_dims(box_coords)
    resized_top_img = shrink_img_to_fit_dims(top_img, box_width, box_height)
    
    top_img_h, top_img_w = top_img.size
    in_box_row_offset, in_box_col_offset = get_align_paste_offset(top_img_w, top_img_h, box_width, box_height, horz_align = 'centered', vert_align = 'centered')
    
    row_offset = box_coords[0][0] + in_box_row_offset
    col_offset = box_coords[0][1] + in_box_col_offset
    
    background_img.paste(top_img, (col_offset, row_offset))
    return background_img



''' returns dict  with all the same keys as box_colors_d, but with the box coords of that that color box in the given img '''
def get_box_coords_d(img, box_colors_d):
    box_coords_d = {}
    
    for box_lbl, box_color in box_colors_d.items():
        box_coords = get_colored_box_corner_coords(img, box_color)
        box_coords_d[box_lbl] = box_coords
        
    return box_coords_d









''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' By_Path Wrappers                                                                             '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''   

def edit_img_by_path(func, args, in_img_path, out_img_path):
    img = Image.open(in_img_path)
    if args == None:        
        output_img = func(img)
    else:
        output_img = func(img, *args)
    output_img.save(out_img_path)
    
    

def add_border_by_path(in_img_path, out_img_path, border, color=0):
    edit_img_by_path(add_border, [border, color], in_img_path, out_img_path)
    
def invert_colors_by_path(in_img_path, out_img_path):
    edit_img_by_path(invert_colors, None, in_img_path, out_img_path)
    
def simple_monospace_write_txt_on_img_by_path(in_img_path, out_img_path, lines, font, txt_color):
    edit_img_by_path(simple_monospace_write_txt_on_img, [lines, font, txt_color], in_img_path, out_img_path)

def trim_border_by_path(in_img_path, out_img_path):
    edit_img_by_path(trim_border, None, in_img_path, out_img_path)


    
if __name__ == '__main__':
    print('in pil_utils main...')
    
#     import make_code_card
#     make_code_card.main()
    c_l = [ 
        (90, 155, 213),
        (69, 234, 113),
         (243, 62, 203),
         (237, 224, 68),
         (56, 79, 247),
         (181, 163, 123),
         (53, 212, 251),
         (167, 88, 216),
         (111, 193, 121),
         (219, 107, 83),
         (149, 155, 155)]
    
    
#     
    color_template_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\Picture1.png"
#     color_template_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\test.jpg"
    
    img = open_img(color_template_path)
    print()
    print(get_list_of_colors_in_image(img))
    print(len(get_list_of_colors_in_image(img)))
    
    img = normalize_pixel_color_grid__by_dominant(img, 10)
#     img.show()
    print('after norm')
#     print(get_list_of_colors_in_image(img))
    print('colors in normalized img: ')
    for clr in get_list_of_colors_in_image(img):
        print('  ', clr)
    print(len(get_list_of_colors_in_image(img)))
    
    
    
    for clr in get_list_of_colors_in_image(img):
        if clr in c_l:
            img = replace_color(img, clr, (255,255,255))
    
#     print('after replacing correct colors with white')
#     for clr in get_list_of_colors_in_image(img):
#         print(clr)
#     for clr in get_list_of_colors_in_image(img):
#         if clr != 255
#         img = replace_color(img, clr, (255,0,0))
#         (90, 154, 215) (90, 155, 213)
        
    img.show()
    
#     im = Image.open(color_template_path)
#     rgb_im = im.convert('RGB')
#     r, g, b = rgb_im.getpixel((1, 1))

# print(r, g, b)
    
    
    
#     color_template_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\Picture1.JPG"
#     save_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\color_template__g_cardNEW.JPG"
# 
#     img = open_img(color_template_path)
#     print(get_list_of_colors_in_image(img))


# 
#     
#     import numpy as np
#     from PIL import Image
#     
#     im = Image.open(color_template_path)
#     data = np.array(im)
#     
#     r1, g1, b1 = (90, 155, 213) # Original value
#     r2, g2, b2 = (255, 255, 255) # Value that we want to replace it with
#     
#     red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
#     mask = (red == r1) & (green == g1) & (blue == b1)
#     data[:,:,:3][mask] = [r2, g2, b2]
#     
#     im = Image.fromarray(data)
# #     im.save(save_img_path)
#     im.show()
#     
    
#     img = make_solid_color_img((50,100), (0,0,255), save_img_path)
#     img.show()
    
    
    

#     
#     color_template_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\color_template__g_card.JPG"
# #     color_template_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\code_cards\\492x1091\\blue.jpg"
# #     img = open_img(color_template_path)
#     
#     
#     
#     pcg = get_pixel_color_grid_from_path(color_template_path)
# 
#     
#     norm_bd_pcg = normalize_pixel_color_grid__by_dominant(pcg)
#     
#     clr_occ_d = get_color_occurrence_d_from_pixel_color_grid(pcg)
# #     print(clr_occ_d)
#     print(len(clr_occ_d))
# # #     print(Image.open(color_template_path).getcolors())
# # 
# # #     print(get_colored_box_corner_coords(img, (91, 155, 213)))
# # #     
# #     color_template_img = open_img(color_template_path)
# # #     color_template_img = Image.open(color_template_path).convert("RGBa")
# #     color_list = get_list_of_colors_in_image(color_template_img) 
# #     for color in color_list:
# #         print(color)
#     
# #     
# #     
# # #     import make_code_card
# # #     make_code_card.main()
# # #     
# # #     
# #     font_path = 'fonts\\SourceCodePro-Bold.ttf'
# #      
# #      
# #     barcode_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\test_images\\barcode_small.png"
# # #     64fe11
# # # 69f3ce
# #     test_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\test_images\\green_box_jj.png"
# #      
# #     save_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\g_card_tools_big_data\\images\\test_images\\pasted.png"
# # #     box_coords = ((4, 9), (4, 41), (9, 9), (9, 41))
# # #     box_coords = ((176, 55), (176, 271), (260, 55), (260, 271))
# #     box_coords = (((97, 51), (97, 320), (200, 51), (200, 320)))
# #      
# #     lines = ['123456789', 'Value$']
# # #     lines = ['abcdefghijklnop']
# # #     lines = ['a', 'G', 'S']
# #      
# #      
# # #     img = open_img(test_img_path)
# # #     txt_img = write_txt_on_img_in_box_coords(img, box_coords, lines, 'black', font_path)
# # #     txt_img.show()
# #      
# # #     
# # # 
# # #     
# # #     print('box_coord dims:  ', get_box_coord_dims(box_coords))
# # # 
# # # 
# # #     img = open_img(test_img_path)
# # #     barcode_img = open_img(barcode_img_path)
# # #     
# # # #     barcode_img = shrink_img_to_fit_dims(barcode_img, 500, 500)
# # # 
# # # 
# # #     
# # # 
# # # 
# # # 
# # # 
# # #     
# # # #     b = shrink_img_to_fit_dims(barcode_img, 100, 50)
# # # #     b.save("C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\big_data\\images\\test_images\\barcode_small.png")
# # # #     b.show()
# # #     
# # # #     print('img dims: ', img.size)
# # # 
# # # #     img.thumbnail([50,50],Image.ANTIALIAS)
# # # #     img.show()
# # # #  
# # #  
# # #     pasted_img = paste_nicely_in_box_coords(barcode_img, img, box_coords, horz_align = 'centered', vert_align = 'centered')
# # #     
# # #     pasted_img.show()
# # # 
# # # 
# # # 
# # # 
# # # 
# # # #     
# # #     img = open_img(test_img_path)
# #     barcode_img = open_img(barcode_img_path)
# # # #      
# # # #     img.paste(barcode_img, (0,0))
# # # #      
# # # #     img.save(save_img_path)
# # # #     img.show()
# # # #     
# #     p = get_colored_box_corner_coords(img, (91, 155, 213))
# #       
# #     print(p)
# # #     
# # #     
# # #     
# # #     
# # # #     trim_border_by_path("C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools\\code_card\\barcode.png", "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools\\code_card\\barcode_trimmed_border.png")
# # # 
# # # # #     in_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\pordh4hewmc01.jpg"
# # # # #     out_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\pordh4hewmc01_border.jpg"
# # # # # #     add_border_by_path(in_img_path, out_img_path, 200, (33,33,33))
# # # # #     
# # # # #     import font_tools
# # # # #     font = font_tools.load_font()
# # # # #     lines = ['test line', 'line 222222222222222222']
# # # # #     txt_color = 'yellow'
# # # # #     simple_monospace_write_txt_on_img_by_path(in_img_path, out_img_path, lines, font, txt_color)
# # # # #     show_img_from_path(out_img_path)
# # # # #     
# # # # #     
# # # # #     
# # # # #     
# # # # # #     input_path = "..\\white_paper_graphs\\btc_graph.jpg"#'../example_pics/big_black_a.jpg'
# # # # # #     output_path = '../example_pics/trimmed_green_triangle.jpg'
# # # # # #     
# # # # # #     trim_border(input_path, output_path)
# # # # # #     show_img_from_path(output_path)
# # # # # 
# # # # # #     pcg = get_pixel_color_grid_from_path(input_path)
# # # # # #     show_pixel_color_grid_as_img(pcg)
# # # # # #     
# # # # # #     pcg2 = rotate_pixel_color_grid(pcg, 90)
# # # # # #     show_pixel_color_grid_as_img(pcg2)
# # # # # #     
# # # # # #     pcg3 = rotate_pixel_color_grid(pcg, 180)
# # # # # #     show_pixel_color_grid_as_img(pcg3)
# # # # # 
# # # # #     invert_colors_by_path("C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_g.JPG","C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_graph_inverted.JPG")
# # # # # 
# # # # # 
# # # # # 
# # # # # #     test_m = [[0,0,0],
# # # # # #               [1,2,3]]
# # # # # #     for r in rotate_pixel_color_grid(test_m, 90):
# # # # # #         print(r)
# # # # 
# # # # 
# # # #     OUTPUT_VID_DIMS_L =[(3840,2160),
# # # #                         (2560,1440),
# # # #                         (1920,1080),
# # # #                         (1280, 720),
# # # #                          (854, 480),
# # # #                          (640, 360),
# # # #                          (426, 240)]
# # # # 
# # # #     x, y = OUTPUT_VID_DIMS_L[7]
# # # # #     x = 1000
# # # # #     y = x
# # # #     
# # # #     test_pics_dir_path = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\vid_m_comp_big_data\\test_pics'
# # # #     un_labeled_path = test_pics_dir_path +  '\\tp_' + str(x) + 'x' + str(y) + '.png'
# # # # #     labeled_path    = test_pics_dir_path +  '\\tpl_' + str(x) + 'x' + str(y)
# # # #     make_solid_color_img((x, y), 'green', un_labeled_path )
# # # # #     simple_monospace_write_txt_on_img_by_path(un_labeled_path, labeled_path, [str(x) + 'x' + str(y)], font, txt_color):


