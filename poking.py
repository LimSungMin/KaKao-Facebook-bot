# coding: utf-8

FACEBOOK_EMAIL = ""
FACEBOOK_PASSWORD = ""


import re
from time import sleep
from datetime import datetime
from urllib import urlencode
from urllib2 import build_opener, install_opener, HTTPCookieProcessor, Request
from cookielib import CookieJar
from bs4 import BeautifulSoup


class FacebookAutoPoke:
	def __init__(self, email=None, password=None):
		self.email = email
		self.password = password

		self.cookie_jar = CookieJar()
		self.url_opener = build_opener(HTTPCookieProcessor(self.cookie_jar))
		install_opener(self.url_opener)

	def login(self, email=None, password=None):
		if email:
			self.email = email
		if password:
			self.password = password

		url = "https://m.facebook.com/login.php"
		data = {
			"email": self.email,
			"pass": self.password
		}
		headers = {
			"User-Agent": "Mozilla/5.0 Gecko/20100101 Firefox/25.0"
		}

		request = Request(url, urlencode(data), headers)
		response = self.url_opener.open(request)

		return "<title>Facebook</title>" in response.read()

	def do(self):
		url = "https://m.facebook.com/pokes"
		headers = {
			"User-Agent": "Mozilla/5.0 Gecko/20100101 Firefox/25.0"
		}

		request = Request(url, None, headers)
		response = self.url_opener.open(request)
		soup = BeautifulSoup(response)

		poke_area = soup.find("div", id="poke_area")

		poke_item_pattern = re.compile(r"poke_live_item_\d+$")
		poke_back_pattern = re.compile(r"/pokes/.+$")

		for poke_item in poke_area.find_all("div", id=poke_item_pattern):
			
			poke_back = poke_item.find("a", href=poke_back_pattern)
			name = poke_item.get_text().encode('utf-8')

			self.url_opener.open("https://m.facebook.com" + poke_back["href"])
			print '%50s :: %s'%(name,datetime.now())
			

if __name__ == "__main__":
	

	autopoke = FacebookAutoPoke(email=FACEBOOK_EMAIL, password=FACEBOOK_PASSWORD)

	if autopoke.login():
		while True:
			try:
				autopoke.do()
				sleep(1)
			except KeyboardInterrupt:
				print '자동찌르기 종료'
				exit()
			except Exception, e:
				continue
	else:
		print '이멜 또는 비번 틀린듯;'
