# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:19:24 2021

@author: Anthony
"""
import requests

cookie = input('paste your kofi cookie here')

headers = {
    'cookie': cookie,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

# replace url with volume you need to download
url = 'https://ko-fi.com/album/Spectral-Chaos-Vol-1--Basic-Lands-W7W834ARJ'

r = requests.get(url, headers=headers)

print(r.status_code)

splits = r.text.split("""onclick="viewImage('""")[1:]

hires_keys = []

for item in splits:
    hires_keys.append(item.split("""'""")[0])

for key in hires_keys:
    print('formatting url with custom key mapped out of hires_keys')
    coolurl = "https://ko-fi.com/Buttons/LoadGalleryItem?galleryItemId={}&external=true&_=1611636437630".format(key)
    
    print('storing new get request in coolr containing new formatted url containing mapped key')
    coolr = requests.get(coolurl, headers=headers)
    
    print('extracting hires url out of coolr, splitting where necessary and storing it as hires_url')
    hires_url = coolr.text.split('''label-hires pull-right hint mt mb-xs"><a href="''')[1].split('''"''')[0]
    
    print('creating a new get request with just the direct url of the png file')
    get_the_actual_thing = requests.get(hires_url, headers=headers)
    
    print('creating a png file using write bytes to get the image')
    with open(hires_url.split("_")[1], 'wb') as png:
        png.write(get_the_actual_thing.content)
    
