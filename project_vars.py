import file_system_utils as fsu
# from code_check.Store import UNUSED_CODE_DIR_PATH


# assumes directory structure like this:"
# some_dir
#  |
#  |-- g_card_tools_root
#  |   |-- g_card_tools
#  |       |-- project_vars.json
#  |       |-- fonts
#  |       |-- txt
#  |           |-- instruction_txt
#  |  
#  |   |-- g_card_tools_big_data
#  |       |-- images
#  |           |-- code_cards
#  |           |-- color_boxes
#  |           |-- logos




G_CARD_TOOLS_DIR_PATH = fsu.get_path_to_current_file(__file__)
G_CARD_TOOLS_BIG_DATA_DIR_PATH = fsu.get_parent_dir_from_path(G_CARD_TOOLS_DIR_PATH) + '\\g_card_tools_big_data'

FONTS_DIR_PATH = G_CARD_TOOLS_DIR_PATH + '\\fonts'
TXT_DIR_PATH   = G_CARD_TOOLS_DIR_PATH + '\\txt'

CODE_CHECK_DIR_PATH = G_CARD_TOOLS_DIR_PATH + '\\code_check'

UNUSED_CODES_DIR_PATH = CODE_CHECK_DIR_PATH + '\\unused_codes'


INSTRUC_TXT_DIR_PATH = TXT_DIR_PATH + '\\instruction_txt'

IMAGES_DIR_PATH = G_CARD_TOOLS_BIG_DATA_DIR_PATH + '\\images'

CODE_CARDS_DIR_PATH  = IMAGES_DIR_PATH + '\\code_cards'
COLOR_BOXES_DIR_PATH = IMAGES_DIR_PATH + '\\color_boxes'
OG_LOGOS_DIR_PATH       = IMAGES_DIR_PATH + '\\logos_original'
TRIMMED_LOGOS_DIR_PATH       = IMAGES_DIR_PATH + '\\logos_trimmed'












