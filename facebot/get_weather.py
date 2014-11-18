# coding: utf-8
from bs4 import BeautifulSoup

import urllib2
import time
def get_weather():
    response=urllib2.urlopen("http://m.weather.naver.com/m/nationWetr.nhn#idx=0")
    soup=BeautifulSoup(response)
    result=""
    result += soup.find("div",id="_sc_tg").find("p").get_text().replace('*','\n\n').encode("utf-8")

    return result

def get_seoul_weather():
    response=urllib2.urlopen("http://m.weather.naver.com/m/nationWetr.nhn#idx=0")
    soup=BeautifulSoup(response)
    result="\n"
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=09140104").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=08110580").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=01110675").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=02113128").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=07110101").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=06110101").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=05110101").get_text().replace('<br/>','').replace('\n',' | ').encode("utf-8")+'\n'

    return result

print get_seoul_weather()