from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import csv
import time


driver = webdriver.Chrome('C:\\Users\\david\\chromedriver.exe')
driver.set_window_position(0, 0)
driver.set_window_size(10, 10)



browser=driver.get('http://www.mieliestronk.com/corncob_caps.txt')
content = driver.page_source
soup = BeautifulSoup(content)




words=soup.text.split()



'''
with open('palabras.txt') as f:

    word_downl = f.readlines()

litleword=[]
for a in word_downl:
    a=a.replace("\n","")
    a=a.strip()
    litleword.append(a)

'''




diccinary={}

for a in words:

    h=a.replace(' ','+')
    browser=driver.get('https://www.collinsdictionary.com/dictionary/english/'+h)
    content = driver.page_source
    soup = BeautifulSoup(content)
    if  soup.find('div', attrs={'class': 'def'}) is None:
        b=''
    else:
        b=soup.find('div', attrs={'class': 'def'}).text


    if  soup.find('span', attrs={'class': 'pos'}) is None:
        c=''
    else:
        c=soup.find('span', attrs={'class': 'pos'}).text 


    if  soup.find('span', attrs={'class': 'quote'}) is None:
        d=''
    else:
        d=soup.find('span', attrs={'class': 'quote'}).text   


    synonyms=''
    if  soup.find('a', attrs={'class': 'form ref'}) is None:
        e=''
    else:
        for e in soup.find_all('a', attrs={'class': 'form ref'}): 
            e=e.text
            if e not in litleword:
                litleword.append(e)
            synonyms=synonyms + e+','

    diccinary[a]=[b,c,d,synonyms]
        

david=pd.DataFrame.from_dict(diccinary, orient='index',columns=[ 'Definition', 'Type', 'Example','synonyms'])

david.to_csv('david_4.csv',sep=';', header=True)



