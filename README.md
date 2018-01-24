# trx2tweet ![Alt text](trx2tweet/media/logo_.jpg?raw=true "trx2tweet")

Cryptocurrency madness! The trx2tweet package is a simple bot to get the current price of [TRON](https://tron.network/)
and tweet it. This crypto-bot handles automatic authentication, tweeting every 30 minutes
at [@TRXstats](https://twitter.com/TRXstats).

The code is written in Python and is meant to run on a \<insert your favourite cloud computing platform\> instance 
(@TRXstats uses AWS Lambda). The price data is provided by [CoinMarketCap](https://coinmarketcap.com/currencies/tron/).

CoinMarketCap API can be found [here](https://coinmarketcap.com/api/) (really straightforward!) 
and Twitter API can be found [here](https://developer.twitter.com/en/docs).

The [`twitter_bot`](twitter_bot.py) module defines two possible ways of authentication. For automatic authentication 
just use your *consumer_key* and *consumer_secret* and you'll be good to go!


Follow these steps to run the code yourself:

### 1. Twitter

Log in to your [Twitter](https://twitter.com/) account and
[create a new application](https://apps.twitter.com/app/new). Under the *Keys
and Access Tokens* tab for [your app](https://apps.twitter.com/) you'll find
the *Consumer Key* and *Consumer Secret*. 

```shell
# automatic authentication
self.consumer_key = <Consumer Key>
self.consumer_secret = <Consumer Secret>
```

If you want the tweets to come from the same account that owns the application,
simply use the *Access Token* and *Access Token Secret* on the same page. If
you want to tweet from a different account, follow the
[steps to obtain an access token](https://dev.twitter.com/oauth/overview).


### 2. Build your Lambda function 

Check out the [documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
to create one AWS Lambda function. To schedule automated actions CloudWatch Event seems to work well 
(triggered every 30 minutes in trx2tweet case).


### 3. Install dependencies

Just upload a [deployment package](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
and AWS Lambda will handle it for you. 


### 4. Start the bot

Save your Lambda function and start tweeting! 


