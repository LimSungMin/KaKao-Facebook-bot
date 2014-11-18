#-*- coding: utf-8 -*-

from random import randint
from pykakao import kakaotalk
from math import *
import time

from time import sleep

from bs4 import BeautifulSoup

import urllib2

from get_etc import *

import get_news
import google_translate
import get_rank
import get_weather



die=["교통사고로","칼에 찔려서","복상사로","경찰에게 도망가다가","술에 찌든체 밖에서 자다가","자연사로",
"성적 욕구를 푸는 행위를 하다가","레고를 밟아서","얼음에 미끄러져서","로또에 당첨되고 쇼크사로","북한군 총에 맞아",
"의문사로","실족사로","중국에서 음식을 맛있게 먹다가","어...음...어...","아이를 낳다가","화살에 맞아"]
hi=["안녕! 넌 참 못생겼구나!","안녕! 넌 참 잘생겼구나!","안녕! 넌 참...개성있게 생겼구나!","안녕! 넌! 엄...음...안녕!","안녕!","반가워!","만나서 반가워!","Hello Guys!","너도 안녕!"]
food=["당연히 치킨! 치느님 헠헠","짜장면!","짬뽕!","족발!","곱창!","소화 잘되는 고기!","탕수육!","피자!","날먹어!","Error 404 : Not Found"]
foob=[04,18,26,33,50,76]

time_server_start=time.time()
blocked_list = []
chatroom_list=[36689620031549,46449584708757,43082374138863,34487711599430]


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
                            list_txt.write(str(chat_id)+'\n')
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


                        if "notice " in message and chat_id == 70546206443768:
                            f= open('init_list.txt','r')
                            notice_rooms = f.readlines()
                            f.close()

                            for notice_room in notice_rooms:
                                try:
                                    kakao.write(int(notice_room.replace('\n','')),message.replace('notice ',''))

                                except:
                                    print notice_room.replace('\n','')+"번 방 실패"

                        list_txt=open("blocked_list.txt","r")
                        get_list_txt=list_txt.read()
                        list_txt.close()


                        if not chat_id in blocked_list and not author_name in get_list_txt:
                            
                            if '@' in message:
                                message=message.replace('@','')

                            if message == "키워드":
                                kakao.write(chat_id,"키워드는 다음과 같습니다. '@'는 빼고 말해주세요!")
                            
                                kakao.write(chat_id,"◎실시간서비스 : 네이버실시간, 다음실시간, 영화실시간, 올림픽\n\n◎날씨서비스 : 날씨, 전국날씨\n\n◎뉴스서비스 : 뉴스, 스포츠뉴스, 축구뉴스, 야구뉴스, 농구뉴스\n\n◆유틸서비스 : 계산, 검색! , 번역\n\n◎기타서비스 : 나언제죽어?, 먹을거추천좀, 여자친구추천좀, 오늘의명언")
                                
                                kakao.write(chat_id,"[!NEW!]새 키워드 : 번역, 오늘의명언")

                            elif "오늘의명언" in message.replace(' ',''):

                                kakao.write(chat_id,get_today_saying())

                            elif "롤전적" in message:
                                kakao.write(chat_id,"롤전적 검색 기능은 삭제되었습니다.")
                            elif "성민봇" in message and not chat_id in chatroom_list:

                                kakao.write(chat_id,"주인님 카카오톡 : lsmorigin")

                            elif (message == "나가" or "꺼저" in message or "꺼져" in message):                                
                                #kakao.write(chat_id,"잠시 점검중 입니다.")
                                
                                kakao.write_emoticon(chat_id,"잘있어 친구들!","2202001.emot_065.png","(\uc774\ubaa8\ud2f0\ucf58)")
                                #init_list.remove(chat_id)
                                list_txt=open("init_list.txt","r")
                                get_list_txt=list_txt.read()
                                list_txt.close()
                                list_txt=open("init_list.txt","w")
                                list_txt.write(get_list_txt.replace(str(chat_id)+'\n',""))
                                list_txt.close()

                                kakao.leave(chat_id)

                            elif "번역" in message:
                                try:
                                    message = message.replace('번역','')
                                    sl = message[0:3]
                                    tl = message[3:6]
                                    word = message[6:]

                                    kakao.write(chat_id,google_translate.translate(sl,tl,word))
                                except:
                                    
                                    kakao.write(chat_id,"언어코드는 다음과 같습니다.\n한국어 : 한, 영어 : 영\n중국어 : 중, 일본어 : 일\n독일어 : 독, 프랑스어 : 불\n러시아어 : 러, 스페인어 : 스\n라틴어 : 라, 아랍어 : 아")
                                    kakao.write(chat_id,"예) \"한영번역 '번역할 문장' \" 을 말하시면 한->영 번역 결과가 나옵니다.")

                            elif message=="올림픽":
                                kakao.write(chat_id,get_rank.get_olympic_rank())

                            elif "안녕" in message or "ㅎㅇ" in message or "하이" in message:

                                kakao.write_emoticon(chat_id,hi[randint(0,len(hi)-1)]+"\n@키워드 를 말해봐!","2202001.emot_037.png","(\uc774\ubaa8\ud2f0\ucf58)") 

                            elif "검색!" in message:
                                if message != "검색!":
                                    try:
                                        word = message.replace("검색!","").replace(" ","")
                                        kakao.write(chat_id,get_dic_search(word))

                                    except:
                                        kakao.write(chat_id,"사전에 등록되지 않은 단어입니다.")
                                else:
                                    kakao.write(chat_id,"검색! '키워드' 를 말하시면 요약된 사전검색결과가 나옵니다.")


                            elif message.replace(' ','') == "네이버실시간":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_rank.get_naver_rank())))

                            elif message.replace(' ','') == "다음실시간":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_rank.get_daum_rank())))                            
                            
                            elif message.replace(' ','') == "영화실시간":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s"%("\n".join(get_rank.get_movie_rank())))

                            elif message.replace(' ','') == "스포츠뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_news.get_sport_news())))

                            elif message.replace(' ','') == "축구뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_news.get_soccer_news())))

                            elif message.replace(' ','') == "야구뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_news.get_baseball_news())))

                            elif message.replace(' ','') == "농구뉴스":

                                kakao.write(chat_id, time.strftime("[%m월 %d일 %H시%M분%S초 현재]")+"\n"+"%s" % ("\n".join(get_news.get_basketball_news())))

                            elif message.replace(' ','')=="전국날씨":
                                
                                kakao.write(chat_id,time.strftime("[%m월 %d일 %H시%M분%S초 현재]\n\n")+get_weather.get_weather())

                            elif message=="날씨":

                                kakao.write(chat_id,time.strftime("[%m월 %d일 %H시%M분%S초 현재]\n")+get_weather.get_seoul_weather())

                            elif message=="뉴스":

                                kakao.write(chat_id,get_news.get_total_news())

                            elif message=="야동":

                                kakao.write(chat_id,".prx2.unblocksit.es 사이트 주소뒤에 이거 붙이고 들어가면 warning.or.kr 안뜸 ㅋ")

                            elif "계산" in message and author_name != "이민성":
                                _message = message.replace("계산","")
                                try:
                                    kakao.write(chat_id,"결과 : "+str(float(eval(_message))))
                                    if '/' in _message:
                                        kakao.write(chat_id,"소숫점까지 아시려면 소수형태로 숫자를 써주세요.\n(예 : 1.0/2.0) ")
                                except:
                                    kakao.write(chat_id,"제대로 된 수식을 입력하세요.\n연산자 종류 : +, -, *, /, ** <- 제곱,\nsqrt(n) <- n의 제곱근,\nlog(x,y) <- 밑이 y인 로그 x\nsin(x), cos(x), tan(x) <- 삼각함수(라디안)\n**수식앞에 '계산' 을 붙여주세요.**")

                            elif message=="서버":

                                kakao.write(chat_id,server_time(time_server_start))


                            elif "섹스키워드 " in message:
                                sexkey = message.replace("섹스키워드 ","")
                                f = open('sex.txt','a')
                                f.write(sexkey+'\n')
                                kakao.write(chat_id,"키워드가 추가되었습니다.")
                                f.close()

                            elif "섹스" in message:
                                f = open('sex.txt','r')
                                sex = f.readlines()                                
                                kakao.write(chat_id,sex[randint(0,len(sex)-1)])
                                kakao.write(chat_id,"섹스키워드 '키워드' 로 키워드 추가가 가능합니다. ")
                                f.close()

                            elif "언제죽어" in message.replace(' ',''):
                                
                                kakao.write_emoticon(chat_id,author_name+" 은(는) "+str(randint(1,70))+"년 뒤에 "+die[randint(0,len(die)-1)]+" 죽음 ^오^","2202002.emot_0"+str(randint(10,80))+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message=="광주는?":

                                kakao.write_emoticon(chat_id,"광주는..그..하나의 광역시야..그래서 100만명이 넘기떄문에 광역시로 지정하지 않을수가 없잖아?","2202001.emot_054.png","(\uc774\ubaa8\ud2f0\ucf58)")
                        
                            elif message=="먹을거추천좀":

                                kakao.write_emoticon(chat_id,food[randint(0,len(food)-1)],"2202001.emot_055.png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif "여자친구추천좀" in message.replace(' ',''):

                                kakao.write_emoticon(chat_id,"","2202001.emot_0"+str(foob[randint(0,len(foob)-1)])+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            
                            
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
    