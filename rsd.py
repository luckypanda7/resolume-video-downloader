  _____                 _                         _____ _ _         _____                      _                 _           
 |  __ \               | |                       / ____| (_)       |  __ \                    | |               | |          
 | |__) |___  ___  ___ | |_   _ _ __ ___   ___  | |    | |_ _ __   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 |  _  // _ \/ __|/ _ \| | | | | '_ ` _ \ / _ \ | |    | | | '_ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | | \ \  __/\__ \ (_) | | |_| | | | | | |  __/ | |____| | | |_) | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |_|  \_\___||___/\___/|_|\__,_|_| |_| |_|\___|  \_____|_|_| .__/  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                           | |                                                               
                                                           |_|                                                               

#This can be used to download sample clips from the resolume.com 
#To run it, replace the URL with the page that you want to download clips from. 


import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://resolume.com/footage/internationalpatterns'
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers)
soup = bs(r.content, 'lxml')
table = soup.find_all("div", class_="previews",)


link_list = [a['href'] for a in soup.find_all('a', href=True)]

letters = ["mp4"]

res = [data for data in link_list if all(item in data for item in letters)]


for clips in res:
    clip_title = os.path.basename(clips)
    r = requests.get(clips)
    with open(clip_title, 'wb') as f:
        f.write(r.content)
