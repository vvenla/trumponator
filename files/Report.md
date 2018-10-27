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

Lorem ipsum...

### Venla

Venla has been studying Mathematics and Computer science before starting the Danta Science masters program. She had some experience of natural language progressing before the project.

## Project description

Trumponator is a tool for predicting stock market development based on the tweets of a famous comedian Donald Trump. 
We use advanced machine learning techniques like natural language processing to analyse the tweets and an artificial 
intelligence to predict how the stock markets will behave.




### Data

Tweets of Donald Trump, preprocessed by removing special characters, punctuation and case specific stopwords. We access 
the tweets by Twitter API.
 
Stock market information (timestamps, value) accessed through XXX -API


### Data analysis

We will build a supervised vector model with Fast Text -library, where the tweets will be labeled by effects on the stock 
market. The effects will be calculated from the changes in stock markets in a certain time frame after the tweets timestamp.

### Communication of results

We will document our project and findings, and make a visualization where we compare the real stock markets and the changes 
our model predicted. We will demonstrate the power (or the lack of it) of our model by applying the predictor to recent 
tweets of Trump.

### Operationalization

TIf the results match the real stock markets, there is a tool for traders to make short term investments. Our predictor 
will show if there is clear correlation between the tweets of Trump and the stock market. This correlation is now suspected 
and speculated by many, so it is interesting to do research on the matter.

## Steps of action

In thie section we will explain how the project developed, from ideation and data wrangling to the model and user interface. We will also mention the challenges and other unpredictable things we faced on each step.

### Idea

Where did the idea came from?

### Uploading the data

#### Tweets

Lorem ipsum... (Suvi)

#### Stock market data

Lorem ipsum... (Vili)

### Wrangling

#### Tweets

At this points we had tweets in two json-files, before and after the election day. Texts of the tweets looked all something like this:

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

Lorem ipsum... (Vili) 

#### Combining the datasets

Lorem ipsum... (Vili)

### Data analysis

#### Descriptive statistics

##### TF-IDF scores

The TF-IDF score is calculated for each word, using each tweet as a separate document. More information about the process is described in the [Term frequency-inverse document frequency](#Term-frequency-inverse-document-frequency) Term frequency-inverse document frequency.



The total TF-IDF tweet score is averaged for each tweet to represent sentiment score of the tweet. In the table it is seen that the TF-IDF score range is widest within the big negative stock market change class and also the mean sentiment score value is biggest in the same class. The smallest mean for the score and lowest standard deviation can be seen in the medium stock market change classes. For negative stock market change classes the sentiment score values vary more than for the positive classes.



#### Making the model

FastText...

## Results



## Summary


The prediction model was formed by taking all the tweets starting at the 15th of June 2015 when the Trump's presidential campaign was launched until 25th of Sep 2018. The results of the model predicting Trump's influence on the stock market are very promising.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_all.PNG "Long-term accuracy of the model")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_all.PNG "Long-term number of tweets")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_per_all.PNG "Long-term percentage share of tweets")

For curiosity the model results were separated in two based on the Trump's election day as U.S. President. The election day was the 8th of Nov 2016. During the presidency until 25th of Sep 2018 Trump has posted 854 tweets (counting only business days).

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_aft.PNG "Accuracy of the model during presidency")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_aft.PNG "Number of tweets during presidency")


The rest 831 tweets before the presidential election day are starting from the presidential campaign launch at 15th June 2015 until the 8th of Nov 2016.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/pie_bef.PNG "Accuracy of the model during the presidential campaign")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/cross_num_bef.PNG "Number of tweets during the presidential campaign")

The difference in results is clear before and after the election day. It was decided to separate dataset to train two models before and after the Trump's election as U.S. president. The results of these two models are compared to review if the presidency has improved his power. The assumption is that his authority did not have such an effect on stock markets when he was just one of the applicants during the presidential campaign.

One logical solution is to take equal amount of Trump tweets before he was elected as president. It is necessary to select stock market period close to the period of the "after" model to minimize effects of the market situation. All the tweets before the presidential election day (but after the launch of the campaign) are selected for the "before" model.

As a conclusion accuracy of all the models are presented in the bar chart. Also the fourth model was built by selecting randomly tweets during the total time period (15.6.2015-25.9.2018). The randomly selected tweets are the worst ones to predict the stock market change.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/All_models.PNG "All models")



## Appendix

### Term frequency-inverse document frequency
TF-IDF stands for term frequency-inverse document frequency, and the TF_IDF weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.


### Correlation results

Correlation tests are performed to assure if the relationship between the stock market daily changes and TF-IDF scores representing tweet sentiment scores can be found. First the normality of the variables need to be checked. Therefore density plot and histogram for both stock market daily changes and TF_IDF scores are plotted. This chart is a variation of a histogram that uses kernel smoothing to plot values, allowing for smoother distributions by smoothing out the noise. In the plots it is easy to see that the stock market daily change data distribution is normal but TF-IDF scores are not normally distributed. In the scatter plot in the figure the TF-IDF scores are concentrated close to the zero showing that most tweets don’t include ”significant” words affecting high scores. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/hist_df_all.PNG "Density plot and histogram for stock market daily change")

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/hist_tf_all.PNG "Density plot and histogram for TF_IDF scores")

The sampling distribution for Pearson's correlation does assume normality; in particular this means that although you can compute it, conclusions based on significance testing may not be sound. Outliers seen in the boxplot figure for varibles can have great influence on Pearson's correlations. Many outliers in applied settings reflect measurement failures or other factors that the model is not intended to generalise to. 

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/boxplot_all.PNG "Boxplot for the ")

Rank correlation non-parametric tests can be used for examing independency of variables since test like Spearman's and Kendall's Tau do not rest upon an assumption of normality. Rank correlation refers to the association between the observed values of two variables. The negative association means that as the values for one variable increase, then the values of the other variable decrease. Correlation quantifies this association, often as a measure between the values -1 to 1 for perfectly negatively correlated and perfectly positively correlated. The calculated correlation is referred to as the “correlation coefficient.” This correlation coefficient can then be interpreted to describe the measures. In the table the results of the three correlation tests are presented. All of them indicate that there is correlation between stock market daily changes and TF/IDF scores. The selected significance level is 5%.

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/Corr_all.PNG "Correlation test results")
