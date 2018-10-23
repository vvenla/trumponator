22.9.2018
The method to extract data from Twitter (Anaconda + Jupyter notebook):
1) Register as Twitter developer (explain carefully for what purpose the data is extracted)
2) Get the Consumer keys and access tokens from Twitter
3) Install tweepy module:
https://github.com/tweepy/tweepy/

Tweepy supports accessing Twitter API via OAuth. Instructions e.g:
https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/

4) Start analysing
Some general instructions to get Trump tweets out of Twitter:
https://medium.freecodecamp.org/learn-python-by-analyzing-donald-trumps-tweets-ccdf156cb5a3
http://2017.compciv.org/syllabus/assignments/homework/serials/trump-tweets-json.html


23.9.2018: The first version of the code fetching data from twitter added (Raw_tweets_DonaldTrump.ipynb) and the first set of 200 latest tweets as json file (raw_trump_tweets.json). Some corrections needs to be done:
1) The code has to be changed in a way that the query to twitter can be called many times and it appends data to the same file based on the datetime or id of the latest downloaded tweet. That is due to the fact that only 200 tweets can be fetched in one query.
2) Datetime format may be necessary to change in a way that it can be linked with the stock market data

Some ideas/questions to proceed after the raw data is collected for further analysis:
1) data imputation -since the twitter/stock market data is quite large i don't feel it is necessary to replace missing/strange values. Just delete those from the sample data set.
2) Sampling - it would be good to develop sampling method for selecting the sample data set (for test and train data sets). However it is difficult to get enough tweets for the analysis so all the tweets are used as training/validation/test data.
3) Data wrangling - methods used in this course. Python code to be created.
4) Weighting factor for words (e.g. TF/IDF values for rating important words)?
5) Data classification - classifying method NLP (Fast text is used). Range of the classes (-1,+1),(-3,...,+3),(up,down)?
6) Machine learning	- Fast Text for training based on train data
7) Summarization - power point slides
8) Visualizing -animated line graph of the stock market after the test data tweets. Python code to be created.

2.10.2018
The twitter has limitations for data extraction (only the latest +3000 tweets/person are available). The updated version of tweet extraction (Raw_tweets_DonaldTrump2.ipynb) is attached.

In some web pages all the tweets (e.g. Trump) can be found in raw format. The instructor (Teemu Roos) agreed that it is ok to use already extracted data from other sources if it is accepted by the provider. E.g. following web page has history data of Trump:
http://trumptwitterarchive.com/archive

3.10.2018
The method for animated plot: Install FFmpeg (Anaconda environment + Jupyter notebook)
https://www.wikihow.com/Install-FFmpeg-on-Windows
conda install -c conda-forge ffmpeg

The first version of animated plot presentation is attached (Animated_plot.ipynb + example data example.txt).

7.10.2018 Sourced two files of old Trump tweets from http://trumptwitterarchive.com/archive

1) Tweets after election 8.11.2016-7.10.2017 in the file Old_Trump_tweets_after_elec.json
2) The 2016 presidential campaign of Donald Trump was formally launched on June 16, 2015. In the file Old_Trump_tweets_before_elec.json are the tweets 15.6.2015-7.11.2016

Two files are combined for further analysis:
1) Raw_tweets_DonaldTrump_before_elec.json including 13132 tweets starting from the launch of the presidential campaign 15.6.2015-26.9.2018
2) Raw_tweets_DonaldTrump_after_elec.json including 5341 tweets after the election day 8.11.2016-26.9.2018

11.10.2018
The file Animated_plot.ipynb is updated

13.10.2018
The file Animated_plot.ipynb was updated to present stock market data of the latest 4 months. The arrows up an down present the direction of the predicted stock market change (six classes of small, medium and big change up or down). The green arrows are equal  predictions to the real big stock market changes and the red arrows are other predicted changes. Also the cleaned tweets of the green arrows are added as annotations to the graph. 
 animation function is not optimized enough since it can't process more than 4 months of data (depending on how many arrows it has to present). Also saving the animation video in the file is still in progress.

14.10.2018
The file combine_tweets_and_stocks_plots.ipynb is added to github including the tweets and stock market data combination. Also the pie graph of the predicion accurary is added (how many predicted changes are classified exactly in the correct class, how many changes are classified to the correct direction althought not to the correct class and how many to the opposite direction class). Also source data descriptive statistics is added to the run.

17.10.2018
The file Animated_plot.ipynb is upgraded for the presentation and the video is saved by Venla as .mp4. It is still not clear how to do the saving with python. Also the pie graph of the file combine_tweets_and_stocks_plots.ipynb is updated. The presentation goes well and few issues are pointed out by the instructor:
1) The data size before and after the election should be quite similar and it should be checked that the amount of tweets within each class is equal
2) user interface for the trumponator should be build up (one option is to create a github page for the trumponator)
3) report should be according to the general instructions and all the highlighted points should be commented in the report

22.10.2018
New files are commited to github:
1) Animated_plot.ipynb
2) animation (.txt)
3) combine_tweets_and_stocks_data.ipynb

Also the file tweets_and_stocks_desc_stat.ipynb is under construction for desriptive analytics


