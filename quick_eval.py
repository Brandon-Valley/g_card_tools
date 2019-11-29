import webbrowser
from googlesearch import search
import pyperclip



def chrome_search(search_terms):   
#     for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(search_terms)
#     webbrowser.open_new_tab(url)
    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    chrome_browser.open_new_tab(url)
        
from tkinter import Tk

        
STORE_NAME = Tk().clipboard_get()  


chrome_search(STORE_NAME + ' check giftcard balance' )
chrome_search(STORE_NAME + ' ebay gift card' )
chrome_search(STORE_NAME + ' number of locations' )


pyperclip.copy(STORE_NAME)
spam = pyperclip.paste()