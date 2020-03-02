#coding: utf-8
import sys
from bs4 import BeautifulSoup
import urllib, urllib2
 
def translate(sl,tl,word):
        #from sl to tl
        data = {'sl':'ko','tl':'en','text': 'word'}
 
        language_code = {'��' : 'ko','��':'en','��':'de','��':'ja','��':'ar','��':'zh-CN','��':'fr','��':'ru',
        '��':'la','��':'es','��':'it'}
 
        data['sl']=language_code[sl]
        data['tl']=language_code[tl]
        data['text'] = word
 
        querystring = urllib.urlencode(data)
        request = urllib2.Request('http://www.translate.google.com' + '?' + querystring )
 
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
        opener = urllib2.build_opener()
        feeddata = opener.open(request).read()
        #print feeddata
        soup = BeautifulSoup(feeddata)
        return soup.find('span', id="result_box").get_text()
 
sl_to_tl = raw_input('� ������ �Ͻðھ��? : ')
sl = sl_to_tl[0:3]
tl = sl_to_tl[3:6]
word = raw_input('������ ������ �Է��ϼ���. : ')
print translate(sl,tl,word)