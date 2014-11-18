# -*- coding: utf-8 -*- 
import mechanize
import time
from get_weather import *

#0은 이메일, 1은 패스워드
ACCOUNT = {"WEATHER":["USERNAME","PASSWORD"]}

def newspeed(email,password,word):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	cj = mechanize.LWPCookieJar()
	br.set_cookiejar(cj)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	

	br.open('https://m.facebook.com')
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	br.submit()

	br.open('https://m.facebook.com/profile.php?id=1474033099481542')
	
	
	
	#가계정은 1, 본계정은 0
	br.select_form(nr = 0)
	br.form['status']=word
	br.submit()
	

if __name__ == "__main__":
	
	flag =0
	while True:
		try:
			now = time.strftime("%m/%d %H:%M:%S")
			word = "[TESTING VERSION]\n현재(%s) 날씨 입니다. 주기적으로 자동 업데이트 됩니다.\n%s"%(now,get_seoul_weather())
			newspeed(ACCOUNT['WEATHER'][0],ACCOUNT['WEATHER'][1],word)
			print word
			time.sleep(600)
			

		except Exception, e:
			raise e
			#continue
	
