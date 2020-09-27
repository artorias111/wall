#https://source.unsplash.com/daily
import requests as re
import os
url=r'https://source.unsplash.com/daily'
x=re.get(url)

if x.status_code==200:
    f=open('wallpaper.jfif','wb')
    f.write(x.content)
    f.close()
    print('download complete')   
    print('Your image is downloaded at '+str(os.getcwd()))
else:
    print('Unsplash servers are down, please try later :(')