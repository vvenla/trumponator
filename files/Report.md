- [The Team](#the-team)
  * [Vili](#vili)
  * [Suvi](#suvi)
  * [Venla](#venla)
- [Project description](#project-description)
  * [Data](#data)
  * [Data analysis](#data-analysis)
  * [Communication of results](#communication-of-results)
  * [Operationalization](#operationalization)
- [Steps of action](#steps-of-action)
  * [Idea](#idea)
  * [Uploading the data](#uploading-the-data)
    + [Tweets](#tweets)
    + [Stock market data](#stock-market-data)
  * [Wrangling](#wrangling)
    + [Tweets](#tweets)
    + [Stock market data](#stock-market-data)
    + [Combining the datasets](#combining-the-datasets)
  * [Data analysis](#data-analysis-1)
    + [Making the model](#making-the-model)
- [Results](#results)


# Trumponator - Behind the scenes

> Report

<!-- toc -->

## The Team

### Vili

Lorem ipsum...

### Suvi

Suvi has Bachelor in Statistics and some introductory Data Science Master studies completed.

### Venla

Venla has been studying Mathematics and Computer science before starting the Danta Science masters program. She had some experience of natural language progressing before the project.

## Project description

Trumponator is a tool for predicting stock market changes based on the twitter tweets of a famous comedian Donald Trump. 
We use advanced machine learning technique natural language processing to analyse the tweets and an artificial 
intelligence to predict how the stock markets will behave. 


### Data

Twitter tweets of Donald Trump, preprocessed by removing special characters, punctuation and case specific stopwords. We access 
the tweets by Tweepy API.
 
Stock market information (timestamps, value) accessed through Alpha Vantage API


### Data analysis

The supervised vector model is built with Fast Text -library, where the tweets are labeled within six sentiment classes based on the real stock market changes. The stock market change is the difference in business day closing values. The six sentiment classes for tweets are evaluated by diviving the daily changes in real stock market in small, medium and big negative or positive class.

### Communication of results

The document of the project and findings can be found in github with the visualization of the real stock market daily changes and the changes our model predicted. The power of the model is demonstrated by applying the predictor to recent tweets of Trump.

(github page)

### Operationalization

Trumponator is a tool for traders to base on the decision of trading. The tool is especially useful as long as Trump is the President of U.S. or has a high political status. Although the stock market changes depend also on many non-political factors there is strong correlation between the tweets of Trump/current political climate and the stock market daily changes. This correlation is currently suspected and speculated by many other studies, so one purpose of the tool is to prove the connection between U.S politics and financial markets. There are also other public figures who's tweets migth have direct effect on stock markets and who could be involved in the model in the next step. Elon Musk and the car industry could be mentioned as one of the examples.

## Steps of action

In the next chapters we will explain how the project developed from brainstorming and data sourcing, via data wrangling and predictive analysis, to the model creation and user interface. We will also mention the challenges and other unpredictable things we faced on each step.

### Idea behind the Trumponator

U.S politics have always been one of the factors affecting stock markets. The country is influencial in worldwide perspective and stock markets nationally and internationally follow U.S. politics and relationship to other countries. To give few examples if the political decision is made to raise taxes that has a clear negative affect to the stock markets. Also changing laws and regulations, or export/import sanctions for products may have either positive or negative impact. Goverment spending and misallocating of resources and money supply may hurt the economy resulting either inflationary or deflationary environment. Monetary policy may cause direct up or down change in interest rates and e.g. higher rates make credit more expensive for companies and the stock markets turn down. 

The interest towards the Donald Trump has arises from his contradictory personality in today's politics in U.S.  As a business man he understands how to manipulate markets but his impulsive behaviour especially towards differing opinions cause unwanted reactions. During the Trump presidency many of the above mentioned political decisions have been made causing uncertainty in the financial markets.


### Uploading the data

#### Tweets

The process to access the Twitter tweets of the real Donald Trump account is quite simple:
-Register as Twitter developer (explain carefully for what purpose the data is extracted for)
-Get the Consumer keys and access tokens from Twitter
-Install tweepy module: https://github.com/tweepy/tweepy/

However only the latest tweets from period of one year could be fetched via Tweepy API due to Twitter limitations. To get wider data set it was decided to fetch older tweets from one of the open twitter archieves of Trump tweets: http://trumptwitterarchive.com/archive

Authenticity of the older tweets can not be verified but there is no other way to get enough tweets for analyses.

Only the variables "created_at" standing for timestampt and "text" or the tweet itself were saved into the .json file. The encoding option is selected to UTF-8.


#### Stock market data

Alpha Vantage delivers a free API for real time and historical financial data and most used finance indicators.
The process to access Alpha 
-Register as Alpha Vantage user
-Get the API key
-Install alpha-vantage module: https://github.com/RomelTorres/alpha_vantage

20-years latest stock market daily closing values are downloaded by selecting symbol='DJI' (the variable name is "4. close"). The startpoint index is saved as date. Yesterday's bin will hold value of change between yesterdays closing and todays closing, so yesterdays tweets get the value impact of today's stock market value development (the variable name is "value change").


### Wrangling

#### Tweets

After uploading we had tweets in two json-files, divided in before and after the election day. Texts of the tweets looked all something like this:

> Thank you @ShopFloorNAM. An honor to be with you today. Great news! Manufacturers report record-high economic optimism in 2017. #TaxReform https://t.co/4sgMWGotOF

<!-- toc -->

To clean the texts we first chenged all the links to only "https", since we only wanted our model to recognise the existence of a tweet, not the content. We also removed all the special characters, so that there was only letters left. After that our examle tweet looked like this:

> Thank you ShopFloorNAM An honor to be with you today Great news Manufacturers report record high economic optimism in TaxReform https

<!-- toc -->

The last step was to change everything to lower case letters:

> thank you https an honor to be with you today great news manufacturers report record high economic optimism in taxreform https

<!-- toc -->

Clean texts were then saved as a json-file, together with original tweets and the timestamps. We made three files: Before and after the election day, and one that had all tweets from both categories.

When we tried to combine the data from tweets and stock markets, we noticed that there was one more thing to wrangle in tweets: Timestamps were not in easily readable form, so we had to change those and rewrite the json-files.

#### Stock market data

The stock market daily change values are categorized in six sentiment classes: small, medium and big negative or positive class. The small positive class includes the smallest 25% of positive change values and the big positive class includes the biggesst 25% of positive change values. The medium positive class includes rest of the positive change values. The negative classes are formed in similar way for negative change values.

The stock markets are open only on business days so it was decided to impute non-business day values. The method used is to copy the closest class for the missing dates. For example the Sat and Sun class is the same with the following first available class on Monday. Now we have change value classes determined for all the days and all the possible tweets. The dates and change values are saved into the .json file.

#### Combining the datasets

Lorem ipsum... (Vili)

### Data analysis

#### Descriptive statistics

##### TF-IDF scores

The TF-IDF score is calculated for each word, using each tweet as a separate document. More information about the process is described in the [Term frequency-inverse document frequency](#Term-frequency-inverse-document-frequency) Term frequency-inverse document frequency.

The total TF-IDF tweet score is averaged for each tweet to represent sentiment score of the tweet. In the table it is seen that the TF-IDF score range is widest within the big negative stock market change class and also the mean sentiment score value is biggest in the same class. The smallest mean for the score and lowest standard deviation can be seen in the medium stock market change classes. For negative stock market change classes the sentiment score values vary more than for the positive classes.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_tf_all.PNG "Statistics for TF_IDF scores")

(how to present the tweets with high scores)

##### Stock market daily changes

The stock market daily changes during latest 20 years vary according to the figure presented below. Few interesting peaks hit our analysis period starting from 15th June 2015. In the fall 2015 investors sold shares globally as a result of slowing growth in the GDP of China, a fall in petroleum prices and the Greek debt default in June 2015. Another roller-coaster is seen after a long calm rise period in January-March 2018 when investors suddenly became worried the economy, boosted by huge tax cuts and fear of inflation. After the decline the market returned to the normal trend soon. The analysis period is otherwise quite stable and therefore perfect for detecting weak signals caused by twitter tweets.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/stock_all.PNG "Stock market daily changes time-series")

##### Comparison of tweet sentiment and stock market data

When plotting the stock market daily changes and TF-IDF scores it is evident that there are only few larger stock market changes during the analysis period. In the scatter plot figure the TF-IDF scores are concentrated close to the zero showing that most tweets don’t include ”significant” words affecting high scores. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/Scatter_all.PNG "Stock market daily changes vs. tweet sentiment scores")

To be able to use the selected data sets as basis for predictive model we need to prove that there is relationship between these variables. In the appendix [Correlation results](#Correlation-results) the strong evidence is build for the argument that the stock market daily changes are correlated with the tweet TF_IDF scores. Therefore we have good foundation for creating the predictive model based on these data sets.

Although the variables are correlated they do not necessarily have causal relatonship between each other. Causation indicates that the change in one variable is the cause of the change in the values of the other variable. In the test setting the Trump tweets might cause some portion of the stock market daily changes but it is also possible that the stock market changes do have an effect on Trump opinions/tweets. Causation is usually studied by organizing a controlled situation which is not possible in real life. But there are also few techniques that can be used when studying e.g. time series such as stock markets. Granger causality test could be done for comparing the TF/IDF scores with the stock daily change data in a way described in the appendix [Granger causality test](#Granger-causality-test). Due to time issues it was decided not to study causation at this point.


#### Making the model

We used the tweets labeled with the stock market changes to teach the model. FastText takes in the labeled data and builds a model based on word vectors. It is then able to predict a label to a given text, in this case, a tweet. 

We splitted the labeled data into training set and validation set. The training set consisted of 85% of the data, and we used the remaining 15% to validate and test the accuracy of the model. 

## Results


The prediction model was formed by taking all the tweets starting at the 15th of June 2015 when the Trump's presidential campaign was launched until 25th of Sep 2018. The results of the model predicting Trump's influence on the stock market are very promising.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_all.PNG "Long-term accuracy of the model")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_all.PNG "Long-term number of tweets")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_per_all.PNG "Long-term percentage share of tweets")

For curiosity the model results were separated in two based on the Trump's election day as U.S. President. The election day was the 8th of Nov 2016. During the presidency until 25th of Sep 2018 Trump has posted 1180 tweets.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_aft.PNG "Accuracy of the model during presidency")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_aft.PNG "Number of tweets during presidency")


The rest 1168 tweets before the presidential election day are starting from the presidential campaign launch at 15th June 2015 until the 8th of Nov 2016.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_bef.PNG "Accuracy of the model during the presidential campaign")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_bef.PNG "Number of tweets during the presidential campaign")

The difference in results is clear before and after the election day. It was decided to separate dataset to train two models before and after the Trump's election as U.S. President. The results of these two models are compared to review if the presidency has improved his power. The assumption is that his authority did not have such an effect on stock markets when he was just one of the applicants during the presidential campaign.

One logical solution is to take equal amount of Trump tweets before he was elected as president. It is necessary to select stock market period close to the period of the "after" model to minimize effects of the market situation. All the tweets before the presidential election day (but after the launch of the campaign) are selected for the "before" model.

As a conclusion accuracy of all the models are presented in the bar chart. Also the fourth model was built by selecting randomly tweets during the total time period (15.6.2015-25.9.2018). (how this was done?) The randomly selected tweets are the worst ones to predict the stock market change. Although the Trump tweets as president seem to be better fit for explaining stock market changes that does not transform to better model when comparing the before and after results. The best model is the one using all the tweets implying that the more data points are available for training the better the result will be.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/All_models.PNG "All models")

Plot of the latest stock market values and predicted changes is presented in the figure. The green arrows show the points were the predicted big positive or negative change was correctly predicted and the tweet causing the prediction can be seen attached to the date. The red arrows visualizes the points where the big positive or negative change was predicted but the real change was not as big or to the opposite direction. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/plot_latest.PNG "Plotting the latest stock market values and predicted changes")

## Improvement possibilities

There are still few improvement possibilities that could be done to enhance the model performance. The number of tweets daily and the number of retweets/tweet could be used as explanatory variables. That might highlight the importance of certain days and tweets when training the model. Also we could use mixture of different used stock markets (nationally and internationally) to see how the model succeeds. Or we could try to select only those stock market companies that would be most vulnerable for the Trump tweets.


## Appendix

### Term frequency-inverse document frequency
TF-IDF stands for term frequency-inverse document frequency, and the TF_IDF weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

### Correlation results

Correlation tests are performed to assure if the relationship between the stock market daily changes and TF-IDF scores representing tweet sentiment scores can be found. First the normality of the variables need to be checked. Therefore density plot and histogram for both stock market daily changes and TF_IDF scores are plotted. This chart is a variation of a histogram that uses kernel smoothing to plot values, allowing for smoother distributions by smoothing out the noise. In the plots it is easy to see that the stock market daily change data distribution is normal but TF-IDF scores are not normally distributed. In the scatter plot in the figure the TF-IDF scores are concentrated close to the zero showing that most tweets don’t include ”significant” words affecting high scores. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/hist_dc_all.PNG "Density plot and histogram for stock market daily change")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/hist_tf_all.PNG "Density plot and histogram for TF_IDF scores")

The sampling distribution for Pearson's correlation does assume normality; in particular this means that although you can compute it, conclusions based on significance testing may not be sound. Outliers seen in the boxplot figure for varibles can have great influence on Pearson's correlations. Many outliers in applied settings reflect measurement failures or other factors that the model is not intended to generalise to. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/boxplot_all.PNG "Boxplot for the variables")

Rank correlation non-parametric tests can be used for examing independency of variables since test like Spearman's and Kendall's Tau do not rest upon an assumption of normality. Rank correlation refers to the association between the observed values of two variables. The negative association means that as the values for one variable increase, then the values of the other variable decrease. Correlation quantifies this association, often as a measure between the values -1 to 1 for perfectly negatively correlated and perfectly positively correlated. The calculated correlation is referred to as the “correlation coefficient.” This correlation coefficient can then be interpreted to describe the measures. In the table the results of the three correlation tests are presented. All of them indicate that there is correlation between stock market daily changes and TF/IDF scores. The selected significance level is 5%.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/Corr_all.PNG "Correlation test results")


### Granger causality test

Granger Causality (GC) is a probabilistic approach for determining if information about past of one variable can explain another and it is based on aversion of the probabilistic theory of causality. A time-series Y (stock market daily changes) can be written as an autoregressive process in which the past values of Y are able to explain (in part) the current value of Y:



Consider another variable X (tweets TF_IDF scores) which has past values as well. If the past values of X help improve the prediction of current values of Y beyond what we get with past values of Y alone, then X is said to Granger Cause Y. The test is under taken as:

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/math1.PNG)

The test is an F-test on all being jointly equal to zero for all values of J. If you reject the null hypothesis then X is said to Granger Cause Y.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/math2.PNG)
