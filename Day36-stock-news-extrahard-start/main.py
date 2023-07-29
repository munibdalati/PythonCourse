import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

API_KEY_STOCK = "T0SAMLI5WG55VNHS"
stock_Endpoint = "https://www.alphavantage.co/query"
API_KEY_NEWS = "575855efac534459bd17dcdbcf90e2be"
news_endpoint = "https://newsapi.org/v2/everything"
account_sid = 'AC3e09ae250855d60eca0f88453f22b8ec'
auth_token = '1ef44e8d9ee5e4c5f995184183ddf417'

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "interval": "60min",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK,
}
news_params = {
    "q": STOCK,
    "apiKey": API_KEY_NEWS,
}

response1 = requests.get(stock_Endpoint, params=stock_params)
print(response1.raise_for_status())
stock_data = response1.json()
yesterday_open = float(stock_data["Time Series (60min)"]["2023-02-03 20:00:00"]["1. open"])
day_before_yesterday_open = float(stock_data["Time Series (60min)"]["2023-01-26 20:00:00"]["1. open"])
change = round((yesterday_open - day_before_yesterday_open) / day_before_yesterday_open * 100, 2)

response2 = requests.get(news_endpoint, params=news_params)
print(response2.raise_for_status())
new_data = response2.json()

emoji = None
if change >= 5:
    emoji = "🔺"
elif change <= -5:
    emoji = "🔻"

if change >= 5 or change <= -5:
    print(change)
    for i in range(0, 3):
        news_heading = new_data["articles"][i]["title"]
        news_brief = new_data["articles"][i]["description"]
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK}: {emoji} {change}% \nHeadline:{news_heading}\nBrief: {news_brief}",
            from_='+16143899121',
            to='+962785056637'
        )
        print(message.status)
