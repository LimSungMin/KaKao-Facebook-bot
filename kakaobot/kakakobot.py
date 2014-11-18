#-*- coding: utf-8 -*-

import random
from pykakao import kakaotalk
from math import *
import time

from get_etc import *

import get_news
import google_translate
import get_rank
import get_weather
import get_lol


die=["교통사고로","칼에 찔려서","복상사로","경찰에게 도망가다가","술에 찌든체 밖에서 자다가","자연사로",
"성적 욕구를 푸는 행위를 하다가","레고를 밟아서","얼음에 미끄러져서","로또에 당첨되고 쇼크사로","북한군 총에 맞아",
"의문사로","실족사로","중국에서 음식을 맛있게 먹다가","어...음...어...","아이를 낳다가","화살에 맞아"]

hi=["안녕! 넌 참 못생겼구나!","안녕! 넌 참 잘생겼구나!","안녕! 넌 참...개성있게 생겼구나!","안녕! 넌! 엄...음...안녕!","안녕!","반가워!","만나서 반가워!","Hello Guys!","너도 안녕!"]
bye=['잘있어 친구들!','아디오스!','다음에 또 봐 친구들!','너무해ㅠ','다음에 또 찾아줄꺼지?']

food=["당연히 치킨! 치느님 헠헠","짜장면!","짬뽕!","족발!","곱창!","소화 잘되는 고기!","탕수육!","피자!","날먹어!","Error 404 : Not Found"]
foob=[04,18,26,33,50,76]

time_server_start=time.time()

chatroom_list=[70546206443768,36689620031549,46449584708757,43082374138863,34487711599430]


blocked_list = [74320040098303,70696651007294,67807514778851,74656146846107]


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

                        if len(message) <= 200 and not 'DEBUG' in message and not chat_id in blocked_list:
                            print "[%s] (%d) %s > %s" % (now, chat_id, author_name, message)
                        else:
                            kakao.leave(chat_id)
                        """
                        if not chat_id in chatroom_list:
                            kakao.write(chat_id,"(윙크)오늘은 여기까지!\n내일 봐요~")
                            kakao.leave(chat_id)
                            # 지울시 키워드 스타트 수정하기!
                        """
                        #KEYWARDS START
                        if not chat_id in blocked_list:
                            
                            if '@' in message:

                                message=message.replace('@','')

                            if message == "키워드" or message == "도움" or message=="도움말":

                                kakao.write(chat_id,"키워드는 다음과 같습니다. '@'는 빼고 말해주세요!")
                                kakao.write(chat_id,"◎실시간서비스 : 네이버실시간, 다음실시간, 영화실시간, 주식\n\n◎날씨서비스 : 날씨, 전국날씨\n\n◎뉴스서비스 : 뉴스, 스포츠뉴스, 축구뉴스, 야구뉴스, 농구뉴스\n\n◆유틸서비스 : 검색!, 위키!, 번역, 롤전적\n\n◎키워드등록 : 등록!, 뜻!\n\n◎기타서비스 : 나언제죽어?, 먹을거추천좀, 여자친구추천좀, 오늘의명언, 로또, 확률, 크기, 랜덤\n\n♠만든놈정보 : 개발자\n\n성민봇 페북 : http://facebook.com/lsmbot")

                            elif "오늘의명언" in message.replace(' ',''):

                                kakao.write(chat_id,get_today_saying())


                            elif "번역" in message:
                                try:
                                    message = message.replace('번역','')
                                    sl = message[0:3]
                                    tl = message[3:6]
                                    word = message[6:]

                                    kakao.write(chat_id,google_translate.translate(sl,tl,word))
                                except:
                                    
                                    kakao.write(chat_id,"언어코드는 다음과 같습니다.\n한국어 : 한, 영어 : 영\n중국어 : 중, 일본어 : 일\n독일어 : 독, 프랑스어 : 불\n러시아어 : 러, 스페인어 : 스\n라틴어 : 라, 아랍어 : 아\n이탈리아어 : 이")
                                    kakao.write(chat_id,"예) 한영번역 '번역할 문장'  을 말하시면 한->영 번역 결과가 나옵니다.")

                            elif message=="주식":
                                kakao.write(chat_id,get_rank.get_stock())

                            elif "안녕" in message or "ㅎㅇ" in message or "하이" in message:

                                kakao.write_emoticon(chat_id,random.choice(hi)+"\n@키워드 를 말해봐!","2202001.emot_037.png","(\uc774\ubaa8\ud2f0\ucf58)") 

                            elif '등록!' in message:
                                message = message.replace('등록!','')
                                try:
                                    keyward = message[0:message.index(':')]
                                    word = message[message.index(':')+1:]
                                    write_keyward(keyward.replace(' ','').replace("'",""),word,author_name)
                                    kakao.write(chat_id,"키워드가 등록되었습니다.\n뜻! 키워드 로 확인 가능합니다.")
                                except:
                                    kakao.write(chat_id,"등록! 키워드 : 뜻 을 입력해주세요.")

                            elif '뜻!' in message:
                                message = message.replace('뜻!','').replace(' ','')
                                try:
                                    kakao.write(chat_id,load_keyward(message))
                                except:
                                    kakao.write(chat_id,"등록되지 않은 키워드입니다.\n등록! 키워드 : 뜻 으로 키워드 추가가 가능합니다.")

                            elif message=='로또':
                                kakao.write_emoticon(chat_id,author_name+'님의 이번주 로또 번호는!\n'+get_lotto_num()+'\n입니다! 부자되세요.','2202002.emot_010.png')

                            elif '확률' in message:

                                if message[len(message)-6:] == '확률':

                                    if message == '확률':
                                        kakao.write(chat_id,"뭐뭐할 확률 을 말하시면 성민봇이 가늠해줍니다.")
                                    elif '내가' in message:
                                        message = message.replace('내가',author_name+"이")
                                        kakao.write(chat_id,probability(message))
                                    elif '성민' in message:
                                        message = message.replace('성민',author_name)
                                        kakao.write(chat_id,probability(message))
                                    else:
                                        kakao.write(chat_id,probability(message))

                            elif '크기' in message:

                                if message[len(message)-6:] == '크기':
                                    if message == '크기':
                                        kakao.write(chat_id,"뭐뭐의 크기 를 말하시면 성민봇이 추정해봅니다.")
                                    elif '성민' in message:
                                        message = message.replace('성민',author_name)
                                        kakao.write(chat_id,size(message))
                                    else:
                                        kakao.write(chat_id,size(message))

                            elif '랜덤' in message:
                                if message == '랜덤':
                                    kakao.write(chat_id,"나열된 단어중에서 하나를 선택합니다\n예) 랜덤 남자 여자 중성")
                                else:
                                    message = message.replace('랜덤','')
                                    kakao.write(chat_id,random_choice(message))

                            elif "검색!" in message:
                                if message != "검색!":
                                    try:
                                        word = message.replace("검색!","").replace(' ','')
                                        kakao.write(chat_id,get_dic_search(word))

                                    except:
                                        kakao.write(chat_id,"네이버사전에 등록되지 않은 단어입니다.\n위키! 를 통해 검색해보세요.")
                                else:
                                    kakao.write(chat_id,"검색! 키워드 를 말하시면 요약된 네이버사전 검색결과가 나옵니다.")

                            elif "위키!" in message:
                                if message != "위키!":
                                    try:
                                        word = message.replace("위키!","").replace(' ','')
                                        kakao.write(chat_id,get_wiki_search(word))

                                    except:
                                        kakao.write(chat_id,"엔하위키 사전에 등록되지 않은 단어이거나.\n현재 엔하위키 사이트가 응답하지 않습니다.")
                                else:
                                    kakao.write(chat_id,"위키! 키워드 를 말하시면 엔하위키 검색결과가 나옵니다..")

                            elif '롤전적' in message:

                                name = message.replace('롤전적','').replace("'","")
                                try:
                                    kakao.write(chat_id,get_lol.get_lol_info(name))
                                except:
                                    kakao.write(chat_id,"롤전적 제대로된 소환사명\n을 치세요")
                            

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

                            elif "계산" in message and author_id==14146663:
                                _message = message.replace("계산","")
                                try:
                                    kakao.write(chat_id,"결과 : "+str(float(eval(_message))))                                    
                                except:
                                    kakao.write(chat_id,"제대로 된 수식을 입력하세요.\n연산자 종류 : +, -, *, /, ** <- 제곱,\nsqrt(n) <- n의 제곱근,\nlog(x,y) <- 밑이 y인 로그 x\nsin(x), cos(x), tan(x) <- 삼각함수(라디안)\n**수식앞에 '계산' 을 붙여주세요.**")

                            elif message=="서버":

                                kakao.write(chat_id,server_time(time_server_start))

                            elif "언제죽어" in message.replace(' ',''):
                                if '은' in message:
                                    kakao.write_emoticon(chat_id,message[0:message.index('은')]+" 은(는) "+str(random.randint(1,70))+"년 뒤에 "+random.choice(die)+" 죽음 ^오^","2202002.emot_0"+str(random.randint(10,80))+".png","(\uc774\ubaa8\ud2f0\ucf58)")
                                elif '는' in message:
                                    kakao.write_emoticon(chat_id,message[0:message.index('는')]+" 은(는) "+str(random.randint(1,70))+"년 뒤에 "+random.choice(die)+" 죽음 ^오^","2202002.emot_0"+str(random.randint(10,80))+".png","(\uc774\ubaa8\ud2f0\ucf58)")
                                else:
                                    kakao.write_emoticon(chat_id,author_name+" 은(는) "+str(random.randint(1,70))+"년 뒤에 "+random.choice(die)+" 죽음 ^오^","2202002.emot_0"+str(random.randint(10,80))+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message=="먹을거추천좀":

                                kakao.write_emoticon(chat_id,random.choice(food),"2202001.emot_055.png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif "여자친구추천좀" in message.replace(' ',''):

                                kakao.write_emoticon(chat_id,"","2202001.emot_0"+str(random.choice(foob))+".png","(\uc774\ubaa8\ud2f0\ucf58)")

                            elif message == '개발자':

                                kakao.write(chat_id,"카카오톡 패킷분석은 김할라님의 pykakao를 사용하였습니다.\nhttps://github.com/HallaZzang/pykakao\n\n이메일 : lsmorigin@gmail.com\n\n개발자는 파릇파릇한 20살. 여친구함\n\n성민봇 페이스북 :\n http://facebook.com/lsmbot")                            

                            elif (message == "나가" or "꺼저" in message or "꺼져" in message):
                                
                                if chat_id in chatroom_list:
                                    kakao.write(chat_id,"이 방은 나가기가 제한되어있는 방입니다.")
                                else:
                                    kakao.write_emoticon(chat_id,random.choice(bye),"2202001.emot_065.png","(\uc774\ubaa8\ud2f0\ucf58)")

                                    kakao.leave(chat_id)
                            
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
    
    