23.9.2018: The first version of the code fetching data from twitter added (Raw_tweets_DonaldTrump.ipynb) and the first set of 200 latest tweets as json file (raw_trump_tweets.json). Somte corrections needs to be done:
1) The code has to be changed in a way that the query to twitter can be called many times and it appends data to the same file based on the datetime or id of the latest downloaded tweet. That is due to the fact that only 200 tweets can be fetched in one query.
2) Datetime format may be necessary to change in a way that it can be linked with the stock market data

Some ideas/questions to proceed after the raw data is collected for further analysis:
1) data imputation -since the twitter/stock market data is quite large i don't feel it is necessary to replace missing/strange values. Just delete those from the sample data set.
2) Sampling - it would be good to develop sampling method for selecting the sample data set (for test and train data sets). Python code to be created
3) Data wrangling - methods used in this course. Python code to be created.
4) Data classification - classifying method? Range of the classes? Python code to be created.
5) Machine learning	- Fast Text for training based on train data
6) Visualizing -animated line graph of the stock market after the test data tweets. Python code to be created, examples can be found in web.

