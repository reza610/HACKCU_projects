import new.py

conkey = "40pcCUjOIJBBDQqKLR4iMhJ5S"
consec = "4UXxbPGiErIy1R8YMnJK5jPOLmufgPoTDPukHc4pFBRKt62RB2"
access = "1129202941456371712-fcT7Y600QtC6NiVbooD1MitZgcY4Fl"
accsec = "WQIpzBA0SDj3A4xEUHBkOylNuaw9GRLl7ObjmGNrcrd0U"

#Authors: Andrew Philips, Reza Naiman, Murilo Tibana, Kevin O'Brien
#include the previous file to use the global variables 

#manage access of the account which will tweet the picture 
auth = tweepy.OAuthHandlers(conkey, consec)
auth.set_access_token(access, accsec)

api = tweepy.API(auth)
text = name
api.update_status("Hello world")

def upload_media(words, filename):
    media = api.media_upload(filename)
    return api.update_status(words, media_ids = [media.media_id_string])


upload_media(text, image)