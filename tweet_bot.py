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

# Search for tweets containing the hashtag "#HBOMax"
tweets = api.search(q="#HBOMax")

# Retweet the tweets
for tweet in tweets:
    try:
        api.retweet(tweet.id)
        print(f"Retweeted tweet {tweet.id}")
    except tweepy.TweepError as e:
        print(f"Error tweeting: {e}")
