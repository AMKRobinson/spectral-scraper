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

url = 'https://ko-fi.com/album/Spectral-Chaos-Vol-1--Basic-Lands-W7W834ARJ'

r = requests.get(url, headers=headers)

print(r.status_code)

splits = r.text.split("""onclick="viewImage('""")[1:]

#splits[0].split("""'""")[0]

splits2 = []

for item in splits:
    splits2.append(item.split("""'""")[0])