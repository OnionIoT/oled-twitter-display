import os
import json
import base64
import urllib3
http = urllib3.PoolManager()

def twitterApiAuthenticate(consumerKey, consumerSecret):
    url = "https://api.twitter.com/oauth2/token"
    # RFC 1738 encode the consumer key and secret
    #urllib.parse.urlencode({'site':'Stack Overflow'})

    # base64 encode the concetanated consumer key and secret
    consumerCredentials = consumerKey + ":" + consumerSecret

    encodedConsumerCredentials = base64.b64encode(consumerCredentials)
    headers = {
        # 'authorization': {
        #     'Basic': encodedConsumerCredentials
        # },
        'Authorization': 'Basic ' + encodedConsumerCredentials,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    body = "grant_type=client_credentials"

    # print "POST to %s:: headers = ", headers
    # print "             body    = ", body

    r = http.request(
        'POST',
        'https://api.twitter.com/oauth2/token',
        headers=headers,
        body=body
    )

    responseData = json.loads(r.data.decode('utf-8'))

    if 'token_type' in responseData and responseData['token_type'] == 'bearer' and 'access_token' in responseData:
        return responseData['access_token']
    else:
        return responseData


### MAIN PROGRAM ###
# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# read the config file
with open( '/'.join([dirName, 'config.json']) ) as f:
	config = json.load(f)


# authenticate with twitter
authToken = twitterApiAuthenticate(config['authorization']['consumerKey'], config['authorization']['consumerSecret'])
print "Auth Token: ", authToken

if authToken == -1:
    print "ERROR: Invalid API credentials!"
    exit()

print "doing other stuff"
