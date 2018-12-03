# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:36:00 2018

@author: user
"""
import codecs
from yandex_translate import YandexTranslate
translate=YandexTranslate('trnsl.1.1.20181107T060212Z.3e0de2328c695a49.df206211182b02620e2cc7931da8fe53ed06cb15') # Api key found on https://translate.yandex.com/developers/keys
untranslated = codecs.open('tel.txt','r','utf8')
content=untranslated.read()
print(content)
#a = content.split()
#for i in a:
#    print(i)
 out = translate.translate(a, 'te-en')
print(out["text"])
op=''.join(out["text"])
#outputt=res.decode('utf-8').strip()
open('D:\dump.txt', 'w').write(op)


