# Import the necessary modules
import tweepy

# Set up the API authentication credentials
consumer_key = "GXLRt374i7MXOxcW0kEkyHWfy"
consumer_secret = "3gy1aBDlIvxXMz1eAcxvXLjRhPRe68DUFPS1zSlnaxx0tm2ZRI"
access_token = "1600652058368954368-Jc1Ew4OXYO9qvI9X4AGWQE1DlCU8C3"
access_token_secret = "p033qafruhn7OkIlKp3UiT1MMCOGLRctI7Cg7O2cluxKk"

# Authenticate the API using the authentication credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Check that the API object is an instance of the tweepy.API class
if isinstance(api, tweepy.API):
    # Search Twitter for mentions of the stock market
    tweets = api.search_tweets("stockmarket", count=100)

    # Loop over the tweets and extract the text and sentiment score
    for tweet in tweets:
        text = tweet.text
        score = 0
        words = text.split()

        # Calculate the sentiment score of the tweet
        for word in words:
            if word.startswith("$"):
                # Increase the score if the word starts with $ (indicating a positive sentiment)
                score += 1
            elif word.startswith("!"):
                # Decrease the score if the word starts with ! (indicating a negative sentiment)
                score -= 1

        # Print the tweet text and sentiment score
        print(text, score)
elif type(api) == type(None):
    print("Error: the API Object is None")

else:
    print("Error: The API object is not an instance of the tweepy.API class")
