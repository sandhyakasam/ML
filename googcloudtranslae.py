# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:13:21 2018

@author: user
"""
import requests 
import codecs
import re
from google.cloud import translate

untranslated = codecs.open('.txt','r','utf8')
content=untranslated.read()
print('\n')
print(content)
for i in content:
    sent = re.split(r' *[\.\?!]',content)
vr=len(sent)    
for i in range(vr-1):
    base_url = 'https://www.google.com/inputtools/request?text='+sent[i]+'&ime=transliteration_en_te'
    json_data = requests.get(base_url).json()
    resu = json_data[1][0][1]
    result='\n'.join(resu)
    file=codecs.open('newl.txt', 'a+' ,'utf-8').write(result+".")
client = translate.Client()
untranslated = codecs.open('newl.txt','r','utf8')
content=untranslated.read()
#print("Actual :",content)
import re
nstr = re.sub(r'[?|$|!|"|#]',r'',content)
#print("with out special characers:",nstr)
#trans=client.translate(nstr,target_language='en')
for i in nstr:
    sentences = re.split(r' *[\.\?!]',nstr)
for stuff in sentences:
     print(stuff)
     trans=client.translate(stuff,target_language='en')
     translated_text=u'{}'.format(trans['translatedText'])
     print(translated_text + "\n")
     file=codecs.open('transl.txt', 'a+').write(translated_text+"\n")
#translated_text=u'{}'.format(trans['translatedText'])
#print("After_Translation:",translated_text)

#file=codecs.open('transl.txt', 'w').write(translated_text)
