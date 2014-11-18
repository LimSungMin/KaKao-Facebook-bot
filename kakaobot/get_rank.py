#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib2

def get_stock():
    response=urllib2.urlopen("http://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0")
    soup = BeautifulSoup(response)

    result = "".encode('utf-8')
    result += "■"+soup.find('tr',onclick="nclkR('mim.index', '', '', 'http://m.stock.naver.com/sise/siseIndex.nhn?code=KOSPI');").get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'
    result += "□"+soup.find('tr',onclick="nclkR('mim.index', '', '', 'http://m.stock.naver.com/sise/siseIndex.nhn?code=KOSDAQ');").get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'
    
    table = soup.find('table',{'class':'s_lst sd_lst'}).find('tbody').find_all('tr')
    cnt = 0
    for stock in table:
        result += "▶"+stock.get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'
        cnt += 1
        if cnt>5:
            break

    return result


def get_naver_rank():
    response = urllib2.urlopen("http://www.naver.com")
    soup = BeautifulSoup(response)

    result = []

    cnt = 1

    for li in soup.find("ol", id="realrank").find_all("li"):
        result.append("%d. %s" % (cnt, li.a["title"].encode("utf-8")))
        cnt += 1
        if cnt > 10:
            break

    return result

def get_daum_rank():
    response=urllib2.urlopen("http://m.daum.net/")
    soup = BeautifulSoup(response)

    result = []

    cnt = 1

    for rank in soup.find('ol',{'data-label':'실시간이슈'}).find_all('span',{'class':'txt_issue',}):
        result.append("%d. %s"%(cnt, rank.get_text().encode('utf-8')))
        cnt += 1

    return result

def get_movie_rank():
    response = urllib2.urlopen("http://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    soup = BeautifulSoup(response)

    result = []

    cnt = 1

    for tr in soup.find("tbody").find_all("a"):
        result.append("%d. %s" % (cnt, tr["title"].encode("utf-8")))
        cnt += 1
        if cnt > 10:
            break

    return result

def get_olympic_rank():
    
    response=urllib2.urlopen("http://m.sports.naver.com/sochi2014/medal/ranking.nhn")
    soup = BeautifulSoup(response)

    result = "%-25s %-3s %-3s %-3s %-3s\n" % ("메달순위","금","은","동","합계")

    
    for tr in soup.find('tbody').find_all('tr'):
        country = tr.find('div').get_text().replace('<br/>','').replace('\n',' ').lstrip().encode('utf-8')
        if '대한민국' in country:
            country = '★'+country
        gold = tr.find('span',{'class':'gold',}).get_text().encode('utf-8')
        silver = tr.find('span',{'class':'silver',}).get_text().encode('utf-8')
        bronze = tr.find('span',{'class':'bronze',}).get_text().encode('utf-8')
        total = tr.find('span',{'class':'total',}).get_text().encode('utf-8')
        #result+=tr["country"].get_text().replace('<br/>','').replace('\n',' ').lstrip().encode('utf-8')+'\n'
        result += "%-25s %-3s %-3s %-3s %-3s\n" % (country,gold,silver,bronze,total)

    result += "대한민국 화이팅"
    return result


