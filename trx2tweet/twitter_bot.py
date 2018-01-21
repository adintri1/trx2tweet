import tweepy
from trx2tweet.data import TrxData


class TwitterBot:

    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.key = ""
        self.secret = ""
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        #self.authenticate()
        self.auth.set_access_token(self.key, self.secret)
        self.api = tweepy.API(self.auth)

    def authenticate(self):
        print(self.auth.get_authorization_url())
        verifier = input('Verification code: ')
        try:
            self.auth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error: failed to get access token.')

        self.key = self.auth.access_token
        self.secret = self.auth.access_token_secret

    def tweet(self, price):
        try:
            self.api.update_status(f"The price of TRON (TRX) on @CoinMarketCap is now {price} USD")
        except tweepy.TweepError:
            pass


if __name__ == '__main__':
    trx_data = TrxData()
    twitter_bot = TwitterBot()
    trx_price = trx_data.get_price()
    if trx_price is not None:
        twitter_bot.tweet(trx_price)



