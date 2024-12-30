#pip install pyshorteners
#pip install pyperclip

import pyshorteners

url = input("Enter URL: ")

def ShortenURL(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

ShortenURL(url)
