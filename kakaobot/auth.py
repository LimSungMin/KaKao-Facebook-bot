from pykakao import kakaotalk

kakao = kakaotalk()
if kakao.auth("YOUR ACCOUNT", "YOUR PASSWORD", "COMPUTER NAME", "DEVICE ID"):
    # computer name and device id are not important things. you can pass any string you want.
    print kakao.session_key
    print kakao.user_id
else:
    print "auth failed."
