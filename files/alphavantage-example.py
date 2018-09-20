import requests

API_KEY = "KRN14ZLFIAEX3YGN"

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=' + API_KEY)
result = r.json()
dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2018-09-19']
print (dataForSingleDate)

