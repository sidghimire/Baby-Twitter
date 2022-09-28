import tweepy
import json
import time
import serial
arduino = serial.Serial(port='COM3', baudrate=9600)
API_KEY="G2QoU2J3mnk79KMlUS9dmg5hD"
API_KEY_Secret=""
Bearer_Token=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""
auth=tweepy.OAuthHandler(API_KEY,API_KEY_Secret)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)
newid=1
newFollower=0
while True:
    userTweets=api.user_timeline(screen_name="sid_ghimire")
    x={}
    for tweet in userTweets:
        x={
            "id":tweet.id,
            "tweet":tweet.text,
            "date":tweet.created_at,
            "likes":tweet.favorite_count,
            "retweet":tweet.retweet_count,
            "followers":tweet.user._json['followers_count'],
            
        }
        break
    tweetLen=len(x['tweet'])
    if(tweetLen>=20):
        tweetText1=str((x['tweet'])[0:20])
        if(tweetLen<40):
            tweetText2=str((x['tweet'])[20:])
            if(tweetLen<36):
                tweetText2=tweetText2+"..."
        else:
            tweetText2=str((x['tweet'])[20:36])+"..."
    else:
        tweetText1=str((x['tweet']))[0:tweetLen]

    followers="Followers: "+str(x['followers'])
    tweetID=(x['id'])
    followerCount=(x['followers'])
    if(newid!=tweetID or newFollower!=followerCount ):
        arduino.write(("##"+"\r\n").encode())
        time.sleep(1.3)

        if(tweetLen>20):
            arduino.write((tweetText1).encode())
            time.sleep(1.3)
            arduino.write(("###"+"\r\n").encode())
            time.sleep(1.3)
            arduino.write((tweetText2).encode())
            time.sleep(1.3)
        else:
            arduino.write((tweetText1).encode())
            time.sleep(1.3)
       
        arduino.write(("#####"+"\r\n").encode())
        time.sleep(1.3)
        arduino.write((followers).encode())
        newid=tweetID
        newFollower=followerCount
        tweetText1=""
        tweetText2=""
            #arduino.write(fhilloollowers)
            
