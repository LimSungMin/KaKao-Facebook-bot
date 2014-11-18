#coding: utf-8
import sys
from bs4 import BeautifulSoup
import urllib, urllib2

import time

def translate(sl,tl,word):
	#from sl to tl
	data = {'sl':'ko','tl':'en','text': 'word'}

	language_code = {'한' : 'ko','영':'en','독':'de','일':'ja','아':'ar','중':'zh-CN','불':'fr','러':'ru',
	'라':'la','스':'es','이':'it'}

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


while True:
	try:
		
		sl_to_tl = raw_input('어떤 번역을 하시겠어요? : ')
		sl = sl_to_tl[0:3]
		tl = sl_to_tl[3:6]
		word = raw_input('번역할 문장을 입력하세요. : ')
		now = time.time()
		print translate(sl,tl,word)
		print '수행시간 : %f'%(time.time()-now)
	except KeyboardInterrupt:
		print '프로그램이 종료되었습니다.'
		break
	