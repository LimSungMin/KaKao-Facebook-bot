# -*- coding: utf-8 -*- 
import mechanize
import time
from get_weather import *
import get_rank

#0은 이메일, 1은 패스워드
ACCOUNT = {"Losa_Kim":["USERNAME","PASSWORD"]}

def newspeed(email,password, word,flag):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	cj = mechanize.LWPCookieJar()
	br.set_cookiejar(cj)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	if flag == 0:

		br.open('https://m.facebook.com')
		br.select_form(nr = 0)
		br.form['email'] = email
		br.form['pass'] = password
		br.submit()
		flag = 1

	br.open('https://www.facebook.com/pokes/?notif_t=poke')

	for form in br.forms():
		print form

	"""
	#가계정은 1, 본계정은 0
	br.select_form(nr = 1)
	br.form['status']=word
	br.submit()
	"""
if __name__ == "__main__":
	
	count,flag =0,0;
	while True:
		try:
			now = time.strftime("%m/%d %H:%M:%S")
			newspeed(ACCOUNT['Losa_Kim'][0],ACCOUNT['Losa_Kim'][1],"Testing ( Count %d )\n%s"%(count,now),flag)
			print "Testing ( Count %d )\n%s"%(count,now)
			time.sleep(61)
			count += 1	
		except Exception, e:
			raise e
			#continue
		
