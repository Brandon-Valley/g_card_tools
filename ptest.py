import keyboard
import time
# 
# keyboard.press_and_release('tab', 3)
# 
# keyboard.write('The quick brown fox jumps over the lazy dog.')
# 

def func():
    print('ran func')
# keyboard.add_hotkey('ctrl+v', print, args=('triggered', 'hotkey'))
keyboard.add_hotkey('ctrl+v', func)
# 
# # Press PAGE UP then PAGE DOWN to type "foobar".
# keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
# 
# # Blocks until you press esc.
# keyboard.wait('esc')
# 
# # Record events until 'esc' is pressed.
# recorded = keyboard.record(until='esc')
# # Then replay back at three times the speed.
# keyboard.play(recorded, speed_factor=3)
# 
# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')
# 
# # Block forever, like `while True`.
# keyboard.wait()
while(True):
    time.sleep(3)
    print('waiting...')

# 
# from ctypes import windll
# if windll.user32.OpenClipboard(None):
#     windll.user32.EmptyClipboard()
#     windll.user32.CloseClipboard()
#     
#     
# from tkinter import Tk
# print('' == Tk().clipboard_get())
