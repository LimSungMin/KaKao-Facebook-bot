# coding: utf-8



from random import randint
from pykakao import kakaotalk

import time

from time import sleep

from bs4 import BeautifulSoup

import urllib2


sool=["연신내","역말사거리","민석이집","응암오거리","신사동고개 사거리","신촌","강남"]
sex=["나랑할까?","파워쎾쓰!","po쎾쓰!wer","싸..싼다!","찎"]
die=["교통사고로","칼에 찔려서","복상사로","경찰에게 도망가다가","술에 찌든체 밖에서 자다가","자연사로"]
hi=["안녕! 넌 참 못생겼구나!","안녕! 넌 참 잘생겼구나!","안녕! 넌 참...개성있게 생겼구나!","안녕! 넌! 엄...음...안녕!","안녕!","반가워!","만나서 반가워!","Hello Guys!","너도 안녕!"]
food=["당연히 치킨! 치느님 헠헠","짜장면!","짬뽕!","족발!","곱창!","소화 잘되는 고기!","탕수육!","피자!","날먹어!","Error 404 : Not Found"]
foob=[04,18,26,33,50,76]
boy_friend=["홍석천♥","지현우♥","신동근♥","가보현♥"]
slang = ["씨발","시발","ㅅㅂ","개새끼","ㅗ","개새","좆까","시1발","씨1발","시부랄","씨벌","ㅆㅂ","병신","지랄","ㅈㄹ","ㅂㅅ","시바","시파","씨팔","새끼"]
four_character=["네글자","4글자","네개","4개"]
time_server_start=time.time()
blocked_list = []
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
def get_weather():
    response=urllib2.urlopen("http://m.weather.naver.com/m/nationWetr.nhn#idx=0")
    soup=BeautifulSoup(response)
    result=""
    result += soup.find("div",id="_sc_tg").find("p").get_text().encode("utf-8")

    return result

def get_seoul_weather():
    response=urllib2.urlopen("http://m.weather.naver.com/m/nationWetr.nhn#idx=0")
    soup=BeautifulSoup(response)
    result=""
    result += soup.find("a",href="/m/locWetr.nhn?naverRgnCd=09140104").get_text().encode("utf-8")

    return result

def get_news():
    response=urllib2.urlopen("http://m.news.naver.com/rankingList.nhn")
    soup=BeautifulSoup(response)
    result=""
    
    result += "[정치 탑뉴스]\n"+soup.find("li",id="politics1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[경제 탑뉴스]\n"+soup.find("li",id="economy1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[연예 탑뉴스]\n"+soup.find("li",id="entertainments1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[사회 탑뉴스]\n"+soup.find("li",id="society1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[IT 탑뉴스]\n"+soup.find("li",id="it_secience1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[생활 탑뉴스]\n"+soup.find("li",id="life_culture1").get_text().strip().encode("utf-8")+"\n\n"
    result += "[세계 탑뉴스]\n"+soup.find("li",id="world1").get_text().strip().encode("utf-8")+"\n\n"
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

def main():

    
    
    kakao = kakaotalk(session_key="5e5ef730af994515a3d4e1ec1198653e05b1a8068c8d47f8a6ebc1847e332f93", device_uuid="s4", user_id=130229954)

    if kakao.login()["body"]["status"] == 0:

        print "Login succeed."



        while True:

            try:

                packet = kakao.translate_response()




                if packet:

                    command = packet["command"]

                    body = packet["body"]




                    now = time.strftime("%m/%d %H:%M:%S")




                    if command == "MSG":

                        message = body["chatLog"]["message"].encode("utf-8")

                        chat_id = body["chatLog"]["chatId"]

                        author_name = body["authorNickname"].encode("utf-8")

                        author_id = body["chatLog"]["authorId"]




                        print "[%s] (%d) %s > %s" % (now, chat_id, author_name, message)

                        sleep(0.1)
                        

                        list_txt=open("init_list.txt","r")
                        get_list_txt=list_txt.read()
                        list_txt.close()

                        if not str(chat_id) in get_list_txt:
                            kakao.write(chat_id,"@키워드 를 말해보세요!")
                            list_txt=open("init_list.txt","a")
                            list_txt.write(str(chat_id))
                            list_txt.close()

                        if message == "@차단" and (author_id == kakao.user_id or author_id == 14146663):

                            if chat_id in blocked_list:

                                kakao.write(chat_id, "[성민봇] 이미 차단된 방입니다.")

                            else:

                                kakao.write(chat_id, "[성민봇] 차단되었습니다.")

                                blocked_list.append(chat_id)

                        elif message == "@차단해제" and (author_id == kakao.user_id or author_id == 14146663):

                            if chat_id in blocked_list:

                                kakao.write(chat_id, "[성민봇] 차단 해제되었습니다.")

                                blocked_list.remove(chat_id)

                            else:

                                kakao.write(chat_id, "[성민봇] 이미 차단 해제된 방입니다.")

                        if "@차단:" in message and (author_id == kakao.user_id or author_id == 14146663):
                            name = message.replace("@차단:","")
                            list_txt=open("blocked_list.txt","r")
                            get_list_txt=list_txt.read()
                            list_txt.close()
                            if not name in get_list_txt:
                                #blocked_list.append(name)
                                list_txt=open("blocked_list.txt","a")
                                list_txt.write(name)
                                list_txt.close()
                                kakao.write(chat_id, name+"님이 차단 되었습니다.")
                            else:
                                kakao.write(chat_id, name+"님은 이미 차단 되었습니다.")

                        elif "@차단해제:" in message and (author_id == kakao.user_id or author_id == 14146663):
                            name = message.replace("@차단해제:","")
                            list_txt=open("blocked_list.txt","r")
                            get_list_txt=list_txt.read()
                            list_txt.close()
                            if name in get_list_txt:                                
                                #blocked_list.remove(name)
                                
                                list_txt=open("blocked_list.txt","w")
                                list_txt.write(get_list_txt.replace(name,""))
                                list_txt.close()
                                kakao.write(chat_id, name+"님이 차단해제 되었습니다.")
                            else:
                                kakao.write(chat_id, name+"님은 차단목록에 없습니다.")

                        list_txt=open("blocked_list.txt","r")
                        get_list_txt=list_txt.read()
                        list_txt.close()
                        if not chat_id in blocked_list and not author_name in get_list_txt:
                            if message == "@키워드":
                                kakao.write(chat_id,"키워드는 다음과 같습니다. '@'는 빼고 말해주세요!")
                                kakao.write(chat_id,"네이버실시간, 술어디서마실까?, 석뽕찡!, 나언제죽어?, 먹을거추천좀, 여자친구추천좀")
                                kakao.write(chat_id,"새 키워드 : 영화실시간, 서울날씨, 전국날씨, 뉴스, 스포츠뉴스, 축구뉴스, 야구뉴스")
                            
                            elif message == "나가" or "꺼저" in message or "꺼져" in message:                                

                                kakao.write_emoticon(chat_id,"잘있어 친구들!","2202001.emot_065.png","(\uc774\ubaa8\ud2f0\ucf58)")
                                #init_list.remove(chat_id)
                                list_txt=open("init_list.txt","r")
                                get_list_txt=list_txt.read()
                                list_txt.close()
                                list_txt=open("init_list.txt","w")
                                list_txt.write(get_list_txt.replace(str(chat_id),""))
                                list_txt.close()

                                kakao.leave(chat_id)
                                
                            elif "안녕" in message or "ㅎㅇ" in message or "하이" in message:

                                kakao.write_emoticon(chat_id,hi[randint(0,len(hi)-1)],"2202001.emot_037.png","(\uc774\ubaa8\ud2f0\ucf58)") 

                            elif message == "네이버실시간":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_naver_rank())))
                            
                            elif message == "영화실시간":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s"%("\n".join(get_movie_rank())))

                            elif message == "스포츠뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_sport_news())))

                            elif message == "축구뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_soccer_news())))

                            elif message == "야구뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_baseball_news())))

                            elif message=="전국날씨":
                                
                                kakao.write(chat_id,time.strftime("[%m월 %d일 %H시%M분%S초 현재]\n\n")+get_weather())

                            elif message=="서울날씨":

                                kakao.write(chat_id,time.strftime("[%m월 %d일 %H시%M분%S초 현재]\n")+get_seoul_weather())

                            elif message=="뉴스":

                                kakao.write(chat_id,get_news())

                            elif "수강신청" in message:

                                kakao.write(chat_id,"http://portal.yonsei.ac.kr\n수강신청 일자는 \n2월 12일(수)(2학년)(재수강 신청불가)\n 2월 14일(금)(전체)(재수강 신청가능) \n로그인 가능시간 07:00 ~ 17:00 \n수강신청 가능시간 09:00 ~ 17:00\n 수강변경 기간 : 3월 5일(수)~ 3월 7일(금)")

                            elif message=="서버":

                                time_server_runtime_second = int(time.time() - time_server_start)
                                time_server_runtime_minute = int(time_server_runtime_second/60)
                                time_server_runtime_hour =  int(time_server_runtime_minute/60)

                                if time_server_runtime_hour != 0:
                                    kakao.write(chat_id,"현재 서버가 %d시간 %d분 %d초 동안 가동중입니다."% (time_server_runtime_hour%60,time_server_runtime_minute%60,time_server_runtime_second%60))
                                elif time_server_runtime_minute != 0:
                                    kakao.write(chat_id,"현재 서버가 %d분 %d초 동안 가동중입니다."% (time_server_runtime_minute%60, time_server_runtime_second%60))
                                else:
                                    kakao.write(chat_id,"현재 서버가 %d 초 동안 가동중입니다."% (time_server_runtime_second%60))

                            elif "섹스" in message:

                                kakao.write(chat_id,sex[randint(0,len(sex)-1)])

                            elif message == "석뽕찡!":
                                cnt=0
                                while cnt < 5:
                                    kakao.write(chat_id,"نا سخية، وأنا كثيرا الحاكم من هذا العالم، وأنا")
                                    sleep(0.5)
                                    cnt += 1

                            elif message =="술어디서마실까?":
                                kakao.write(chat_id,sool[randint(0,len(sool)-1)])

                            elif message =="나언제죽어?":
                                #kakao.write(chat_id,str(randint(1,70))+"년 뒤에 "+die[randint(0,len(die)-1)]+" 죽음 ^오^")
                                kakao.write_emoticon(chat_id,str(randint(1,70))+"년 뒤에 "+die[randint(0,len(die)-1)]+" 죽음 ^오^","2202002.emot_0"+str(randint(10,80))+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message=="광주는?":

                                kakao.write_emoticon(chat_id,"광주는..그..하나의 광역시야..그래서 100만명이 넘기떄문에 광역시로 지정하지 않을수가 없잖아?","2202001.emot_054.png","(\uc774\ubaa8\ud2f0\ucf58)")
                        
                            elif message=="먹을거추천좀":

                                kakao.write_emoticon(chat_id,food[randint(0,len(food)-1)],"2202001.emot_055.png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message=="여자친구추천좀":

                                kakao.write_emoticon(chat_id,"","2202001.emot_0"+str(foob[randint(0,len(foob)-1)])+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message =="남자친구추천좀":

                                kakao.write(chat_id,boy_friend[randint(0,len(boy_friend)-1)])

                            elif "ㅋㅋㅋㅋ" in message:

                                kakao.write(chat_id,"ㅋㅋㅋㅋㅋㅋㅋㅋ")


                            elif "생축" in message or "생일축하" in message or "생일" in message:

                                kakao.write_emoticon(chat_id,"생일 축하드려요~","2202001.emot_045.png")

                            elif author_name == "핑중":
   
                                kakao.write(chat_id,"핑중아 조용히좀 해줄래?")
                            """
                            elif message == "알람":

                                kakao.write(chat_id,"(숫자)초알람 이라고 말하시면 (숫자)초 뒤에 알람이 울립니다")
                            
                            elif "초알람" in message:

                                number=message.replace("초알람","")
                                
                                try:
                                    _number=abs(int(number))
                                    if _number <= 60:
                                        kakao.write(chat_id,str(_number)+"초 뒤에 봐요!")
                                        sleep(_number)
                                        kakao.write(chat_id,str(_number)+"초가 경과하였습니다")
                                    else:
                                        kakao.write(chat_id,"60초 내에서 정해주세요!")
                                except ValueError:
                                    kakao.write(chat_id,"정수로 말해주세요!")
                            """

                            for word in slang:

                                if word in message:

                                    kakao.write(chat_id,"욕을하면 못써요")
                                    break

                            for word in four_character:

                                if word in message:

                                    kakao.write_emoticon(chat_id,"넵! 4글자 이상일때 제가 쳐웃습니다","2202001.emot_024.png")

                            
                    else: # unknown commands

                        # print "[%s] <%s, %s>" % (now, command, body)

                        pass

                else:

                    if kakao.login()["body"]["status"] != 0:

                        print "Auto-reconnect failed."

                        kakao.s.close()

                        break

            except KeyboardInterrupt:

                kakao.s.close()

                exit()

    else:

        print "Login failed."




if __name__ == "__main__":
    #main()
    
    while True:
        try:
            main()
        except:
            continue
    