import keyboard
import time
import os
import shutil
 
 
def wait_for_hotkey_to_be_pressed(hotkey):
    def is_file(in_path):
        return os.path.isfile(in_path)
    
    def delete_if_exists(path):
        if os.path.exists(path):
            if   os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
            else:
                raise Exception('ERROR:  Gave something that is not a file or a dir, bad path: ', path)
            
    def get_names_of_files_in_dir(in_dir_path):
        file_name_l = []
        
        for r, d, f in os.walk(in_dir_path):
            for file in f:
                file_name_l.append(file)
        return file_name_l
    
    
    def pressed():
        open(file_path, 'a').close()
        
    def get_file_path():
        file_num = 0
        
        file_path = 'zzz_waiting_file__' + str(file_num) + '.txt'
        while(is_file(file_path)):
            file_num += 1
            
        return file_path

        
    file_path = get_file_path()
    delete_if_exists(file_path)
        
    keyboard.add_hotkey(hotkey, pressed)
    
    while(True):
        if is_file(file_path):
            delete_if_exists(file_path)
            return
 
wait_for_hotkey_to_be_pressed('ctrl+v')
wait_for_hotkey_to_be_pressed('ctrl+x')
 
# global pressed
# def wait_for_hotkey_to_be_pressed(hotkey):
#     try:
#         pressed = False
#         def hotkey_pressed():
#             print("HOTKEY HAS BEEN PRESSED< IN FUNC")
#             pressed = True
#             return
#         keyboard.add_hotkey(hotkey, hotkey_pressed())
#         
#         while(pressed == False):
#         #         print('waiting...')
#         #         time.sleep(1)
#             pass
#         print('PRESSED!')
#     except:
#         print('failed')
#         return
#  
# wait_for_hotkey_to_be_pressed('ctrl+v')


# import pynput,time
# 
# is_quit = False
# 
# # KeyComb_Quit = [
# #     {pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode(char='g')},
# #     {pynput.keyboard.Key.ctrl_l, pynput.keyboard.KeyCode(char='g')},
# #     {pynput.keyboard.Key.ctrl_r, pynput.keyboard.KeyCode(char='g')}
# #  
# # ]
# KeyComb_Quit = [
#     { pynput.keyboard.KeyCode(char='g'), pynput.keyboard.Key.ctrl,},
#     {pynput.keyboard.KeyCode(char='g'), pynput.keyboard.Key.ctrl_l},
#     {pynput.keyboard.KeyCode(char='g'), pynput.keyboard.Key.ctrl_r}
#  
# ]
# 
# def on_press(key):
#     global is_quit
#     if any([key in comb for comb in KeyComb_Quit]):
#         current.add(key)
#         if any(all(k in current for k in comb) for comb in KeyComb_Quit):
#             is_quit = True
# 
# def on_release(key):
#     try:
#         current.remove(key)
#     except KeyError:
#         pass
# 
# 
# # The currently active modifiers
# current = set()
# 
# listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()
# 
# ##### MAIN Script #####
# while True:
# #     print('...')
#     time.sleep(0.00833)
#     if is_quit:
#         break




# from pynput import keyboard
# import datetime
# 
# # The key combinations to check
# COMBINATIONS = [
#     {keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')},
#     {keyboard.Key.ctrl_r, keyboard.KeyCode(char='c')}
# ]
# 
# # The currently active modifiers
# current = set()
# all = []
# 
# tnow = datetime.datetime.now()
# tcounter = 0
# 
# def on_press(key):
#     print(key , ' pressed ')
#     if any([key in comb for comb in COMBINATIONS]):
#         current.add(key)
# #         all.append(key)
#         if any(all(k in current for k in comb) for comb in COMBINATIONS):
#             global tnow
#             global tcounter
#             tcounter += 1
#             if datetime.datetime.now() - tnow < datetime.timedelta(seconds=1):
#                 if tcounter > 1:
#                     tcounter = 0
#                     main_function()
#             else:
#                 tnow = datetime.datetime.now()
#                 
#     print('all: ', all)
#     if key == keyboard.Key.esc:
#         listener.stop()
# 
# 
# def on_release(key):
#     print(key, ' released ')
#     try:
#         current.remove(key)
#         print('all: ', all)
#     except KeyError:
#         print('all: ', all)
#         pass
# 
# def main_function():
#     print('Main function fired!')
#     # rest of your code here...
# 
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()











# 
# 
# 
# from pynput import keyboard
# 
# # The key combination to check
# COMBINATION = {keyboard.KeyCode.from_char('x'), keyboard.Key.ctrl_l}
# 
# # The currently active modifiers
# current = set()
# 
# 
# def on_press(key):
# #     print('current: ', current)
#     if key in COMBINATION:
#         current.add(key)
#         if all(k in current for k in COMBINATION):
#             print('All modifiers active!')
#             listener.stop()
#     if key == keyboard.Key.esc:
#         listener.stop()
# 
# 
# def on_release(key):
#     try:
#         current.remove(key)
#     except KeyError:
#         pass
# 
# 
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()









# from pynput import keyboard
# # import keyboard
# 
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
# 
# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.char:
# #     if key == 'ctrl+v':
#         # Stop listener
#         return False
# 
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
# 
# 
# print('done')


# ctrl_v_pressed = False
# 
# 
# 
# 
# def add_hotkey_____ctrl_v(ctrl_v_pressed):
#     def hotkey_pressed():
#         print('setting to true')
#         ctrl_v_pressed = True
#     keyboard.add_hotkey('ctrl+v', hotkey_pressed)
# 
# 
# # def func():
# #     print('ran func')
# # # keyboard.add_hotkey('ctrl+v', print, args=('triggered', 'hotkey'))
# # keyboard.add_hotkey('ctrl+v', func)
# 
# add_hotkey_____ctrl_v(ctrl_v_pressed)
# 
# import time
# while(True):
#     time.sleep(1)
#     print(ctrl_v_pressed)
#     ctrl_v_pressed = True