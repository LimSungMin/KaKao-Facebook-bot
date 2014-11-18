#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import urllib2


def get_total_news():
	# coding : utf-8
    response=urllib2.urlopen("http://m.news.naver.com/rankingList.nhn")
    soup=BeautifulSoup(response)
    result=""
    
    result += "[정치 탑뉴스]\n"+soup.find("li",id="politics1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[경제 탑뉴스]\n"+soup.find("li",id="economy1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[연예 탑뉴스]\n"+soup.find("li",id="entertainments1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[사회 탑뉴스]\n"+soup.find("li",id="society1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[IT 탑뉴스]\n"+soup.find("li",id="it_secience1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[생활 탑뉴스]\n"+soup.find("li",id="life_culture1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += "[세계 탑뉴스]\n"+soup.find("li",id="world1").find('span').get_text().strip().encode("utf-8")+"\n\n"
    result += time.strftime("%m월 %d일 %H시")+" 네이버 뉴스 제공"
    return result

def get_sport_news():
    response=urllib2.urlopen("http://m.sports.naver.com/ranking/newsRanking.nhn")
    soup=BeautifulSoup(response)

    result = []

    cnt = 1

    for li in soup.find("ol").find_all("li"):
        result.append("%d. %s" % (cnt, li.get_text().lstrip().encode("utf-8")))
        cnt += 1
        if cnt > 5:
            break

    return result

def get_baseball_news():
    response=urllib2.urlopen("http://m.sports.naver.com/ranking/newsRanking.nhn?&section=baseball")
    soup=BeautifulSoup(response)

    result = []

    cnt = 1

    for li in soup.find("ol").find_all("li"):
        result.append("%d. %s" % (cnt, li.get_text().lstrip().encode("utf-8")))
        cnt += 1
        if cnt > 5:
            break

    return result

def get_soccer_news():
    response=urllib2.urlopen("http://m.sports.naver.com/ranking/newsRanking.nhn?&section=worldfootball")
    soup=BeautifulSoup(response)

    result = []

    cnt = 1

    for li in soup.find("ol").find_all("li"):
        result.append("%d. %s" % (cnt, li.get_text().lstrip().encode("utf-8")))
        cnt += 1
        if cnt > 5:
            break

    return result

def get_basketball_news():
    response=urllib2.urlopen("http://m.sports.naver.com/ranking/newsRanking.nhn?&section=basketball")
    soup=BeautifulSoup(response)

    result = []

    cnt = 1

    for li in soup.find("ol").find_all("li"):
        result.append("%d. %s" % (cnt, li.get_text().lstrip().encode("utf-8")))
        cnt += 1
        if cnt > 5:
            break

    return result
