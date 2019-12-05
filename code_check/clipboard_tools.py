from tkinter import Tk
import pyperclip


def get_clipboard():
    return(Tk().clipboard_get())

def copy_to_clipboard(i):
    pyperclip.copy(i)
    spam = pyperclip.paste()