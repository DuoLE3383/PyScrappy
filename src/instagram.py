import urllib.request
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
except:
    print("<--- Please install the below packages  --->")
    print("--pip install selenium")
    print("--pip install webdriver-manager")
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import time
import json
import re
import os 

usr_agent = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive',
}


def insta_details(link, n_pages):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    for _ in range(n_pages):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find_all('section', {"class": "zwlfE"})
    main2 = soup.find_all('div', {"class": "_2z6nI"})

    for details in main:
        title = details.find('h1', {"class": "rhpdm"})
        #posts = details.find('li', {"class": "Y8-fY"})
        info = details.find_all('span', {"class": "g47SY"})
        data = details.find('div', {"class": "-vDIg"}).find_all('span')
        posts = info[0].text
        followers = info[1].text
        following = info[2].text
        if(data): bio = data[0].text
        print("Name: ", title.text)
        print("Number of Posts: ", posts)
        print("Followers: ", followers)
        print("Following: ", following)
        if(data): print("Bio: ", bio) 
        else: print("Bio: None")
        print()
        break

    u = []
    for i in main2:
        url = i.find_all('div', {"class": "v1Nh3 kIKUG _bz0w"})
        for x in url:
            a = 'https://www.instagram.com/'+x.a['href']
            u.append(a)

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def func(a):
        driver.get(a)
        for _ in range(1):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        main = soup.find_all('div', {"class": "C4VMK"})
        for details in main:
            title = details.find('span', {"class": ""})
            return title.text
            
    caption =[]
    for i in u:
        caption.append(func(i))

    df = pd.DataFrame({'Captions': caption})
    return df