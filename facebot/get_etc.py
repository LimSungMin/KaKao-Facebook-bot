#-*- coding: utf-8 -*-

import time
import random
from bs4 import BeautifulSoup

import urllib, urllib2

import sys


def random_choice(items):
    items = items.split(' ')
    result = random.choice(items) 
    return result


def probability(some):
    percent=random.uniform(0,100)
    result = "%s은 %.2f퍼센트 입니다.\n" %(some,percent)
    if percent >= 90:
        result += "이건 일어날 수 밖에 없습니다!"
    elif percent >= 70:
        result += "비교적 높은 확률로 일어납니다!"
    elif percent >= 50:
        result += "성공할지 실패할지 장담 할 수 없습니다."
    elif percent >= 30:
        result += "일어나지 않을 확률이 약간 높습니다."
    elif percent >= 10:
        result += "비교적 높은 확률로 일어나지 않습니다."
    else:
        result += "이건 일어나지 않을 수 밖에 없습니다!"

    return result

def size(some):
    size = random.uniform(0,200)
    result = "음....%s는 %.2fcm 같군요..이건 확실합니다!"%(some,size)
    return result


def get_lotto_num():
    return "(%2d) (%2d) (%2d) (%2d) (%2d) (%2d)\n+ 보너스번호 (%2d)"%(random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45))


keywards={}
def write_keyward(keyward, word, name):
    
    keywards[keyward] = [word,name]

def load_keyward(keyward):
    return "%s 은(는) %s을(를) 의미한다.\n[%s님 께서 등록하신 키워드]"%(keyward,keywards[keyward][0],keywards[keyward][1])

def server_time(time_server_start):
    
    time_server_runtime_second = int(time.time() - time_server_start)
    time_server_runtime_minute = int(time_server_runtime_second/60)
    time_server_runtime_hour =  int(time_server_runtime_minute/60)

    result=""

    if time_server_runtime_hour != 0:
        result += "현재 서버가 %d시간 %d분 %d초 동안 가동중입니다."% (time_server_runtime_hour%60,time_server_runtime_minute%60,time_server_runtime_second%60)
    elif time_server_runtime_minute != 0:
        result += "현재 서버가 %d분 %d초 동안 가동중입니다."% (time_server_runtime_minute%60, time_server_runtime_second%60)
    else:
        result += "현재 서버가 %d 초 동안 가동중입니다."% (time_server_runtime_second%60)

    return result + "\n서버 재시작시 초기화됩니다."

def get_dic_search(word):
    response=urllib2.urlopen("http://terms.naver.com/search.nhn?query="+word)
    soup = BeautifulSoup(response)

    result=""
    result += soup.find('dd',{'class':'dsc'}).get_text().encode('utf-8')

    a = soup.find('ul',{'class':'thmb_lst',}).find('li').find('dt').find('a')

    result += "\n[본문링크]\n"+"http://terms.naver.com"+a["href"].encode('utf-8')

    return result


def get_wiki_search(word):
    #400 에러는 이렇게 해석
    site= "http://mirror.enha.kr/search/?q=%s"%urllib.quote(word)
    
    hdr = {'User-Agent':'Mozilla/5.0','referer':'http://mirror.enha.kr/'}
    
    req = urllib2.Request(site,headers=hdr)

    response=urllib2.urlopen(req)
    soup = BeautifulSoup(response)

    result=""
    result += soup.find('div',{'class':'snippet'}).get_text().encode('utf-8')
    a=soup.find('div',{'class':'search-result'}).find('a',{'class':'wiki'})
    result += "\n[본문링크]\n"+"http://mirror.enha.kr"+a["href"].encode('utf-8')

    return result


def get_today_saying():

    site= "http://m.search.naver.com/search.naver?query=오늘의명언"
    # 아주 의미있는 함수.... 403 forbiden 은 이걸로 해결하면 댐...
    hdr = {'User-Agent':'Mozilla/5.0','referer':'http://m.naver.com'}
    
    req = urllib2.Request(site,headers=hdr)

    response=urllib2.urlopen(req)
    soup = BeautifulSoup(response)

    saying = []

    for word in soup.find('div',{'class':'cnt_area'}).find_all('div',{'class':'fm_card'}):
        saying.append(word.find('p',{'class':'txt'}).get_text().encode('utf-8')+'\n- '+word.find('p',{'class':'writer'}).get_text().encode('utf-8'))

    return saying[random.randint(0,len(saying)-1)]




