#https://www.pexels.com/search/desktop%20wallpaper/

#pexels api key: 563492ad6f917000010000013b7de554cc354ac6b1ea6f2c419369e3


import requests as re
from bs4 import BeautifulSoup as bs
from os import makedirs
from time import sleep

url=r'https://www.pexels.com/search/desktop%20wallpaper/'

if re.get(url).status_code==200:
    a=re.get(url)
    x=bs(a.text,'html.parser')
    m=x.find_all('a')
    print(m)

else:
    print("The pexels website is down right now, please try later")
