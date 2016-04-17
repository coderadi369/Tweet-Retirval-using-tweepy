Python 2.7.11 |Anaconda 2.5.0 (64-bit)| (default, Jan 29 2016, 14:26:21) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tweepy
>>> ckey="ev945sP6s5xrtmfCpsYC982Kd"
>>> csec="AxLEqZ1j3cNMEndVPzrjz7aiGRbdi5n6lC4kqk8AVPanwQdffn"
>>> akey="528632029-F28dDaQ4Mw96FXarTnTPCu6NHT4Q5YwhZ7bDKvHJ"
>>> asec="7FxfxuT2iGJjocIITFLyefPplv1VkwJC84xP8Yfu6eQDX"
>>> auth = tweepy.OAuthHandler(ckey, csec)
>>> auth.set_access_token(akey, asec)
>>> api = tweepy.API(auth)
>>> msg=" "
>>> data=api.search("q=Easter",count=10)
>>> for tweet in data:
	line=tweet._json["text"]
	msg=msg+"<p>"+line+"</p><br/>"

	
>>> msg="<html><head></head><body>"+msg+"</body></html>"
>>> msg=msg.encode('ascii','ignore').decode('ascii')
>>> f=open('practice.html','w')
>>> f.write(msg)
>>> f.close()
>>> import webbrowser
>>> webbrowser.open_new_tab('practice.html')
True
>>> 
