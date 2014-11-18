from pykakao import kakaotalk

kakao = kakaotalk()
if kakao.auth("lsmorigin@gmail.com", "anfrhrl", "smbot1", "vega1"):
    # computer name and device id are not important things. you can pass any string you want.
    print kakao.session_key
    print kakao.user_id
else:
    print "auth failed."