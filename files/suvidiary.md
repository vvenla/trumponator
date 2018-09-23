23.9.2018: The first version of the code fetching data from twitter added (Raw_tweets_DonaldTrump.ipynb) and the first set of 200 latest tweets as json file (raw_trump_tweets.json). Somte corrections needs to be done:
1) The code has to be changed in a way that the query to twitter can be called many times and it appends data to the same file based on the datetime or id of the latest downloaded tweet. That is due to the fact that only 200 tweets can be fetched in one query.
2) Datetime format may be necessary to change in a way that it can be linked with the stock market data

Some ideas to proceed after the raw data is collected for further analysis:
