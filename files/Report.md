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
[Link text](## Appendix)
The TF-IDF score is calculated for each word, using each tweet as a separate document. More information about the process is described in the <a id="Appendix">Appendix</a> Term frequency-inverse document frequency.


The total TF-IDF tweet score is averaged for each tweet to represent sentiment score of the tweet. In the table it is seen that the TF-IDF score range is widest within the big negative stock market change class and also the mean sentiment score value is biggest in the same class. The smallest mean for the score and lowest standard deviation can be seen in the medium stock market change classes. For negative stock market change classes the sentiment score values vary more than for the positive classes.



#### Making the model

FastText...

## Results

![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/Fig1.PNG "Fig1")

## Summary


## Appendix

### Term frequency-inverse document frequency
TF-IDF stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.
