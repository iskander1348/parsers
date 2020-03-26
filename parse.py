import requests
#from lxml import html
from bs4 import BeautifulSoup


def getmanagers(http):
    r = requests.get(http)
    soup = BeautifulSoup(r.text)
    fclass = 'max-w-full'
    dat = soup.find('div', {'class': fclass}).find_all('img')
    result = []
    for d in dat:
        result.append(d['alt'])
    return result

def getobjectname(http):
    r = requests.get(http)
    soup = BeautifulSoup(r.text)
    return soup.find('h2', {'class': 'py-1'}).text

def getestate(http):
    r = requests.get(http)
    soup = BeautifulSoup(r.text)
    dat = soup.find('div', {'class': 'flex flex-wrap max-w-full w-full self-end items-start justify-start'}).find_all('a')
    for d in dat:
        if str(d).find('find-real-estate-agent') > 0:
            return d['href']
    

def getrequsites(http, name):
    
    r = requests.get('https://www.fastighetsbyran.com/'+http)
    soup = BeautifulSoup(r.text)
    dat = soup.find('img', {'alt': name})
    photo = dat['src']
    #phone
    
        
    #print(len(phones))
    dat = soup.find_all('div', {'class': 'mt-6 cursor-pointer px-1 md:px-4 lg:px-8 w-1/2 md:w-1/3 lg:w-1/4'})
    for d in dat:
        if str(d).find(name) > 0:
            a = d.find_all('a')
            
            phone = a[1]['href'].replace('tel:','')
            email = a[2]['href'].replace('mailto:','')
    return {photo, phone, email}
            
    
    
    

http = 'https://www.fastighetsbyran.com/en/spanien/objekt/?objektid=2255360'

objectname = getobjectname(http)
print(objectname)
managers = getmanagers(http)
estate = getestate(http)
for manager in managers:
    print(manager)
    for p in getrequsites(estate, manager):
        print(p)

