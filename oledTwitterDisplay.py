import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://api.twitter.com"
bearerToken = ""

# function to perform applcation-only authentication with Twitter
def twitterApiAuthenticate(consumerKey, consumerSecret):
    url = baseUrl + "/oauth2/token"
    # in the future, may have to RFC 1738 encode the consumer key and secret

    # base64 encode the concetanated consumer key and secret
    consumerCredentials = consumerKey + ":" + consumerSecret
    encodedConsumerCredentials = base64.b64encode(consumerCredentials)

    # create the request headers and body
    headers = {
        # 'authorization': {
        #     'Basic': encodedConsumerCredentials
        # },
        'Authorization': 'Basic ' + encodedConsumerCredentials,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    body = "grant_type=client_credentials"

    # perform the request
    r = http.request(
        'POST',
        url,
        headers=headers,
        body=body
    )

    # convert the response data to a dictionary
    responseData = json.loads(r.data.decode('utf-8'))

    if 'token_type' in responseData and responseData['token_type'] == 'bearer' and 'access_token' in responseData:
        global bearerToken
        bearerToken = responseData['access_token']
        return True
    else:
        bearerToken = responseData
        return False

# function to read the last tweet from a user's timeline
def twitterApiGetLastTweet(userId):
    url = baseUrl + '/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': userId,
        'count': 1
    }

    # create the request headers
    headers = {
        'Authorization': 'Bearer ' + bearerToken
    }

    # execute the GET request
    r = http.request(
        'GET',
        url,
        headers=headers,
        fields=params
    )

    # convert the response data to a dictionary
    responseData = json.loads(r.data.decode('utf-8'))
    lastTweet = responseData[0]

    if 'text' in lastTweet:
        ret = {
            'text': lastTweet['text'].encode('utf-8'),
            'date': lastTweet['created_at']
        }
        return ret
    else:
        return False

def oledWriteTweet(user, text, date):
    if oledExp.driverInit() != 0:
        print 'ERROR: Could not initialize the OLED Expansion'
        return False

    # write out the name of the account
    oledExp.write('@' + user + ':')

    # set the cursor to the next line
    oledExp.setCursor(1,0)

    # write out the tweet
    oledExp.write(text)



### MAIN PROGRAM ###
# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# read the config file
with open( '/'.join([dirName, 'config.json']) ) as f:
	config = json.load(f)


# authenticate with twitter
authSuccess = twitterApiAuthenticate(config['authorization']['consumerKey'], config['authorization']['consumerSecret'])
if not authSuccess:
    print "ERROR: Invalid API credentials!"
    exit()

# use twitter api to get last tweet of specified user
tweet = twitterApiGetLastTweet(config['application']['user'])
if not tweet:
    print "ERROR: Could not retreive Tweet!"
    exit()

print 'Got tweet! ', tweet
# display the tweet on the OLED
oledWriteTweet(config['application']['user'], tweet['text'], tweet['date'])

print 'Done!'
