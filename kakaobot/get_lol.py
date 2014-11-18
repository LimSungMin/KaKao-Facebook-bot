# coding: utf-8

from bs4 import BeautifulSoup

import urllib2

def get_lol_info(name):
    site= "http://m.fow.kr/?name="+name
    # 아주 의미있는 함수.... 403 forbiden 은 이걸로 해결하면 댐...
    hdr = {'User-Agent':'Mozilla/5.0','referer':'http://m.fow.kr'}
    
    req = urllib2.Request(site,headers=hdr)

    response=urllib2.urlopen(req)
    soup = BeautifulSoup(response)

    result = name+"님의 전적정보\n"
    
    cnt = 0
    for level_win in soup.find('div',id='profile').find_all('a'):
        result += "■ "+level_win.get_text().encode('utf-8')+'\n'
        cnt += 1
        if cnt > 1:
            break   

    try:
        result += soup.find('div',style="top:7px; left:145px; position:absolute;").get_text().replace(' ','').encode('utf-8')+'\n'
    except:
        result += "랭크게임 정보가 없습니다.\n\n"

    try:
        result += "※특이사항 : \n일반겜은 "+soup.find('div',{'class':'c_champ'}).find('div',style="position:absolute; left:40px; top:3px; font-size:12px; font-weight:bold;").get_text().encode('utf-8')+"성애자\n"
    except:
        pass

    try:
        result += "랭겜은 "+soup.find('div',{'class':'c_champ_s4'}).find('div',style="position:absolute; left:40px; top:3px; font-size:12px; font-weight:bold;").get_text().encode('utf-8')+"성애자"
    except:
        pass
    
    return result

while True:
    name = raw_input('누구를 검색하시겠습니까? : ')
    print get_lol_info(name)
    print '\n\n'


