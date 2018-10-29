# Trumponator
Trumponator is tool to predict stock market development. It utilizes supervised machine learning to predict changes of Dow Jones Industrial Average by reading tweets of Donald Trump, the president of United States. Developed further, trumponator would be cabable to predict any stock market index based on any individual's (or group's of individuals) tweets.

This is a project work for Introduction to Data Science -course of University of Helsinki, 2018.

## Trumponator in action

![alt text](https://www.github.com/vvenla/trumponator/raw/master/files/presentation/ezgif.com-video-to-gif.gif)
      
Visualization of some predictions drawn over the actual stock market index. Green arrows are the predictions that were given to the tweets that are written to the upper part of the animation. Red arrows represent predictions for which tweets are not shown in this animation.

## How to use it

1. Fork [the trumponator project][project] and clone it to your local machine.

2. Install the [FastText library][fasttext] to be able to run trumponator.

3. Run trumponator.py using [python3](https://realpython.com/installing-python/).

      `python3 trumponator.py "write or paste here the tweet you want to predict from"`  

      ![alt text](https://github.com/vvenla/trumponator/raw/master/files/pictures/trump_use-case_MAGA.gif)  

      In the gif above the program is run in a conda virtual environment called "alphavantage", which has all the required dependencies installed. You can install the dependencies in any environment of your liking, or not to use virtual environment at all.  

4. Read the result, invest and profit $$$.

### How to develop Trumponator for your own needs

1. Fork [the trumponator project][project], clone it and install the dependencies needed:
- [Alpha Vantage to access the stock market data used for training](https://www.alphavantage.co/)
- [Twitter API for the tweets (training and usage automatization)](https://developer.twitter.com/en.html)
- [FastText library for classifying the tweets and predicting the market][fasttext]

2. Train different models using different datasets of stock market indexes and tweets.

3. Predict, invest, profit $$$.

### Links:

[Report](https://github.com/vvenla/trumponator/blob/master/files/Report.md)

[FastText tutorial](https://github.com/facebookresearch/fastText/blob/master/docs/supervised-tutorial.md)

[Alpha Vantage API documentation](https://www.alphavantage.co/documentation/)

[Wrangling tweets example](https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)



[project]: https://github.com/vvenla/trumponator/
[fasttext]: https://fasttext.cc/docs/en/support.html
