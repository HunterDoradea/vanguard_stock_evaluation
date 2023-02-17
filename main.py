# PROGRAMMING IN PYTHON!!!

# import the necessary files:
import requests
import os
import datetime
from newsapi import NewsApiClient

STOCK_API_KEY = "LVADS8E4THBPUFUW"
NEWS_API_KEY = "94d4102873634a08b262d28b2499dbf1"

account_sid = 'AC4ec15d4a6c8edd0d801f719105ca53e4'
auth_token = '66d8a73ff3260968b1f359d4a1f35d93'

#CHANGE THE STOCK YOU WANT TO TRACK HERE!!!!
STOCK_NAME = "VOO"
COMPANY_NAME = "Vanguard S&P 500 ETF"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":STOCK_API_KEY,

}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

#print(data)
# get a hold of the closing days data:
 # turn this into a list and get each data that is associated with the kesy:
# each item in this new list is compossed of only the values and not the keys
data_list = [value for (key, value) in data.items()]
#print(data_list) # each item in this list is a dictionary with each days data
# ger a hold of yesterdays data:
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print("*******")
print("YESTERDAYS CLOSING PRICE: ")
print(f"$ {yesterday_closing_price}")
print("********")
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print("DAY BEFORE YESTERDAYS CLOSING PRICE: ")
print(f"$ {day_before_yesterday_closing_price}")
print("************")
difference = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))
print("THE DIFFERENCE BETWEEN THE TWO IN U.S. DOLLARS: ")
print(f"$ {difference}")
percentage = (difference / float(yesterday_closing_price) ) * 100
percentage = round(percentage, 2)

print("THE DIFFERENCE CALCULATED AS A PERCENTAGE: ")
print(f"{percentage} %")


# use the info above to print if the difference was either positive or negative:
if percentage < 0:
    print(f"{COMPANY_NAME} is DOWN by {percentage} %")
else:
    print(f"{COMPANY_NAME} is UP by {percentage} %")


print("**********")
news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
# list of all the articles:
news_data = news_response.json()["articles"]
#print(news_data)
# use python slice operator to create a list that contains the first 3 articles:
list_of_articles = news_data[:2]
#print(list_of_articles)
#print("*******")
# create a list of the first 2 articles headline and description using list comprehension:
two_articles = [f'Headline: {item["title"]}. \nBrief: {item["description"]}' for item in list_of_articles]
#print(three_articles)
print("**********")

#PRINT 2 DIFFERENT ARTICLES
for article in two_articles:
    print(article)
    print("*****")

