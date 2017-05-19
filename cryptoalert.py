import requests
import slackweb
import json

coins = ['bitcoin','digibyte','namecoin','stellar','bytecoin-bcn'] #cryptocurrencies to monitor
coinurl = "https://api.coinmarketcap.com/v1/ticker/"
slack = slackweb.Slack(url="https://hooks.slack.com/services/TXXXX/BXXX/XXXX") #set up your own slack webhook
alertpercent = float(3.00) #if the price changes more than 3%, send an alert

def slackwebhook(alarmtext):
    slack.notify(text=alarmtext, channel="#alerts", username="cryptocoin-bot", icon_emoji=":warning:")

def checkprices(coin):
    url = coinurl + coin
    coindata = requests.get(url)
    coindatajson = json.loads(coindata.content)
    percentchange = float(coindatajson[0]['percent_change_1h'])
    currentusdprice = coindatajson[0]['price_usd']
    if abs(percentchange) > alertpercent:
        alert = "%s changed %s%% in the last hour. Current price: %s" % (coin,percentchange,currentusdprice)
        slackwebhook(alert)

for coin in coins:
    checkprices(coin)



