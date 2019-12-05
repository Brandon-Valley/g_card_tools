from tkinter import Tk
import pyperclip

CLIPBOARD_INPUT_PATH = 'clipboard_input.txt'


def get_clipboard():
    return(Tk().clipboard_get())

def copy_to_clipboard(i):
    pyperclip.copy(i)
    spam = pyperclip.paste()
    
    
# def read_from_clipboard_input():
#     def read_text_file(file_path):
#         with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
#             result = tuple(l.rstrip() for l in text_file.readlines())
#             return result
#     
#     raw_tup = read_text_file(CLIPBOARD_INPUT_PATH)
#     
#     cb_str = raw_tup[0]
#     for str in raw_tup[1:]:
#         cb_str += '\n' + str
#     
#     return cb_str


if __name__ == '__main__':
#     a = read_from_clipboard_input()
    import code_check
    code_check.main()









        