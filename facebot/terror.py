# -*- coding: utf-8 -*- 
import mechanize
from datetime import datetime
import time

AUTHOR = """
개발자 : 성민(lsm_origin)
이메일 : lsmorigin@yonsei.ac.kr
블로그 : http://blog.naver.com/lsm_origin

이 파이썬 프로그램은 python 2.7.X 버전과 mechanize 라이브러리를 반드시 필요로 합니다.
"""

class facebot:
	def __init__(self,email=None,password=None):
		self.email=email
		self.password=password

		self.br = mechanize.Browser()
		self.br.set_handle_robots(False)
		self.cj=mechanize.LWPCookieJar()
		self.br.set_cookiejar(self.cj)
		self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

		self.nr_num=False

	def login(self, email=None,password=None):
		if email:
			self.email=email
		if password:
			self.password=password

		url = "https://m.facebook.com"

		self.br.open(url)
		
		self.br.select_form(nr=0)
		self.br.form['email']=self.email
		self.br.form['pass']=self.password

		self.br.submit()

		return len(self.br.title()) < 15

	def write(self,url,word):

		self.br.open(url)
		
		if self.nr_num==False:
			for n in range(1,11):
				try:
					self.br.select_form(nr=n)
					self.br.form['xhpc_message']=word
					self.nr_num=n
					break
				except:
					continue

		self.br.select_form(nr=self.nr_num)
		self.br.form['xhpc_message']=word						
		self.br.submit()		
		
if __name__ == "__main__":
	
	email="페이스북 아이디"
	password="페이스북 비밀번호"
	url = "타임라인에 글을올릴 주소"
	word = "타임라인에 올릴 글"

	fb_bot=facebot(email=email,password=password)

	if fb_bot.login():
		while True:
			try:
				fb_bot.write(url,word)
				print word
			
			except KeyboardInterrupt:
				print '자동 글쓰기 종료'
				exit()
			
			except Exception, e:
				raise e
	else:
		print '이메일 또는 비밀번호가 틀렸습니다.'