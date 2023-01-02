import tweepy

consumer_key = "kpzC6M6ZLrUz9xKX6PAuoHKhN"
consumer_secret = "3XBxAGbwlJ1m4ghEZkG7ytYAAhX1G06urxNeDkVlWzzGebruaB"
bearer_token =r"AAAAAAAAAAAAAAAAAAAAAMbPkwEAAAAAdl%2FlZC%2FLXsBEx0PR3pKI7vK6iXE%3DQrxVNUPbh4DW8hncnMP25zYpPBQ9pNOE5TGp3qGgDhqdhgYIW9"
access_token = "1478786089674444802-jTAYxlKju3BJYbCKwoAtgHEC3KMPVo"
access_token_secret = "D6877m3q1QmiX08z1fl8q9pcPqvL2ANX9s96RMnbyU8Ia"

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Search for tweets from the accounts "@THR" and "@DEADLINE" containing the hashtags "#HBO", "#HBOMax", or the word "HBO"
tweets = api.search_tweets(q="from:THR OR from:DEADLINE OR from:TheLastOfUs OR from:MattBelloni OR from:loudmouthjulia OR from:Great_Katzby OR from:wbd OR from:wbpictures OR from:HeroMode OR from:Variety OR from:Caseybloys OR from:HBO OR from:hbomax OR from:warnerbros #HBO OR #HBOMax OR HBO OR hbo OR HBOMAX OR HBOMax OR #TLOU OR #TheLastOfUs OR #CartoonNetwork OR #CN OR #WarnerBros OR #WB OR #DC OR DC OR HBODOCUMENTRIES OR HBOdocumentries", lang="en", result_type="recent", count=1000)

# Retweet the tweets that have been retweeted at least 0 time
for tweet in tweets:
    if tweet.retweet_count >0:
        try:
            api.retweet(tweet.id)
            print(f"Retweeted tweet {tweet.id}")
        except tweepy.TweepyException as e:
            print(f"Error tweeting: {e}")
