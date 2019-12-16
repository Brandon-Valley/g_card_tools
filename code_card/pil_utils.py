from PIL import Image
from PIL import ImageDraw

import PIL.ImageFont
import PIL.ImageOps 

import numpy as np








''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Uses Direct PIL import                                                                       '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''

def open_img(path):
    return Image.open(path) 

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
def make_solid_color_img(dims, color, out_file_path):
    img = Image.new('RGB', dims, color)
    img.save(out_file_path)
    
  
def invert_colors(img):
    return PIL.ImageOps.invert(img)




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
            img.putpixel((x,y), pixel_color_grid[y][x])
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
    
 
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''
'''                                                                                              '''
''' Simple Tools                                                                                 '''
'''                                                                                              '''
''' vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv '''

def pixel_color(img, x, y):
    pcg = get_pixel_color_grid(img)
    return pcg[y][x]

# border can be an int (for adding same border to all sides) or tuple (left, top, right, bottom)
def add_border(img, border, color=0):
    if isinstance(border, int) or isinstance(border, tuple):
        return PIL.ImageOps.expand(img, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')


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
    
    for row_num, row in enumerate(pixel_color_grid):
        for col_num, pixel_clr in enumerate(row):
            
            # found top left pixel of box
            if pixel_clr == rgb_tup_box_color:
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


''' resizes and pastes top_img onto background_img inside tuple of coords that forms a box 
    box_coords: (top_right, top_left, bottom_right, bottom_left) '''
def paste_nicely_in_box_coords(top_img, background_img, box_coords, horz_align = 'centered', vert_align = 'centered'):
    box_width, box_height = get_box_coord_dims(box_coords)
    
    print(box_width, box_height)
    









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
    

    
    
    barcode_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\big_data\\images\\test_images\\barcode.png"
#     64fe11
# 69f3ce
    test_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\big_data\\images\\test_images\\green_box_jj.png"
    
    save_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools_root\\big_data\\images\\test_images\\pasted.png"
    box_coords = ((4, 9), (4, 41), (9, 9), (9, 41))




    img = open_img(test_img_path)
    barcode_img = open_img(barcode_img_path)

    paste_nicely_in_box_coords(barcode_img, img, box_coords, horz_align = 'centered', vert_align = 'centered')





    
#     img = open_img(test_img_path)
#     barcode_img = open_img(barcode_img_path)
#     
#     img.paste(barcode_img, (4,10))
#     
#     img.save(save_img_path)
#     img.show()
    
#     p = get_colored_box_corner_coords(img, (105, 243, 206))
    
#     print(p)
    
    
    
    
#     trim_border_by_path("C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools\\code_card\\barcode.png", "C:\\Users\\Brandon\\Documents\\Personal_Projects\\g_card_tools\\code_card\\barcode_trimmed_border.png")

# #     in_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\pordh4hewmc01.jpg"
# #     out_img_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\pordh4hewmc01_border.jpg"
# # #     add_border_by_path(in_img_path, out_img_path, 200, (33,33,33))
# #     
# #     import font_tools
# #     font = font_tools.load_font()
# #     lines = ['test line', 'line 222222222222222222']
# #     txt_color = 'yellow'
# #     simple_monospace_write_txt_on_img_by_path(in_img_path, out_img_path, lines, font, txt_color)
# #     show_img_from_path(out_img_path)
# #     
# #     
# #     
# #     
# # #     input_path = "..\\white_paper_graphs\\btc_graph.jpg"#'../example_pics/big_black_a.jpg'
# # #     output_path = '../example_pics/trimmed_green_triangle.jpg'
# # #     
# # #     trim_border(input_path, output_path)
# # #     show_img_from_path(output_path)
# # 
# # #     pcg = get_pixel_color_grid_from_path(input_path)
# # #     show_pixel_color_grid_as_img(pcg)
# # #     
# # #     pcg2 = rotate_pixel_color_grid(pcg, 90)
# # #     show_pixel_color_grid_as_img(pcg2)
# # #     
# # #     pcg3 = rotate_pixel_color_grid(pcg, 180)
# # #     show_pixel_color_grid_as_img(pcg3)
# # 
# #     invert_colors_by_path("C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_g.JPG","C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_graph_inverted.JPG")
# # 
# # 
# # 
# # #     test_m = [[0,0,0],
# # #               [1,2,3]]
# # #     for r in rotate_pixel_color_grid(test_m, 90):
# # #         print(r)
# 
# 
#     OUTPUT_VID_DIMS_L =[(3840,2160),
#                         (2560,1440),
#                         (1920,1080),
#                         (1280, 720),
#                          (854, 480),
#                          (640, 360),
#                          (426, 240)]
# 
#     x, y = OUTPUT_VID_DIMS_L[7]
# #     x = 1000
# #     y = x
#     
#     test_pics_dir_path = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\vid_m_comp_big_data\\test_pics'
#     un_labeled_path = test_pics_dir_path +  '\\tp_' + str(x) + 'x' + str(y) + '.png'
# #     labeled_path    = test_pics_dir_path +  '\\tpl_' + str(x) + 'x' + str(y)
#     make_solid_color_img((x, y), 'green', un_labeled_path )
# #     simple_monospace_write_txt_on_img_by_path(un_labeled_path, labeled_path, [str(x) + 'x' + str(y)], font, txt_color):


