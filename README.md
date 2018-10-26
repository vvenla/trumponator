# Trumponator
Trumponator is tool to predict stock market development. It utilizes supervised machine learning to predict changes of Dow Jones Industrial Average by reading tweets of Donald Trump, the president of United States. Developed further, trumponator would be cabable to predict any stock market index based on any individual's (or group's of individuals) tweets.

This is a project work for Introduction to Data Science -course of University of Helsinki, 2018.

## Trumponator in action

TODO gif and pitch here


## How to use it

1. Fork [the trumponator project][project] and clone it to your local machine.

2. Install the [FastText library][fasttext] to be able to run trumponator.

3. Run trumponator.py using [python3](https://realpython.com/installing-python/).
`python3 trumponator.py`

TODO add gif

4. Give the program a tweet on the command line.

TODO add gif

5. Read the result, invest and profit $$$.

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
