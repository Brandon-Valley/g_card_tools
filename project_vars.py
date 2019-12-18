import file_system_utils as fsu


# assumes directory structure like this:"
# some_dir
#  |
#  |-- g_card_tools_root
#  |   |-- g_card_tools
#  |       |-- project_vars.json
#  |       |-- fonts
#  |  
#  |   |-- g_card_tools_big_data
#  |       |-- images
#  |           |-- code_cards
#  |           |-- color_boxes




G_CARD_TOOLS_DIR_PATH = fsu.get_path_to_current_file(__file__)
G_CARD_TOOLS_BIG_DATA_DIR_PATH = fsu.get_parent_dir_from_path(G_CARD_TOOLS_DIR_PATH) + '\\g_card_tools_big_data'

FONTS_DIR_PATH = G_CARD_TOOLS_DIR_PATH + '//fonts'

IMAGES_DIR_PATH = G_CARD_TOOLS_BIG_DATA_DIR_PATH + '\\images'

CODE_CARDS_DIR_PATH  = IMAGES_DIR_PATH + '\\code_cards'
COLOR_BOXES_DIR_PATH = IMAGES_DIR_PATH + '\\color_boxes'












