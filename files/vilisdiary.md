## Thu 20.9.18
At the second meeting I promised to wrangle the stock market data into a format where time intervals would have labels for following time periods _t_.
This preprocessing gives us the ability to fetch labels for tweets (positive or negative effect on the market) based on the tweets time stamp.

I will also do light research on the time interval that tweets affect the stock market. 

## Tue 25.9

I familiarized myself with alpha vantage, run some examples in jupyter notebook. We had a meeting where we agreed about the distribution of workload: I'll look into the stock data and wrangle it, Suvi will wrangle the tweets and Venla will do some wrangling and later concentrate on the logic to combine the wrangled tweet and stock data together for the fastText model.

## Thu 27.9

It turns out that the original idea of having 30min to maybe 2h intervals for the stock data doesn't really work out: markets are closed outside the office hours but mr Trump tweets around the clock. I think we need to go for daily closing values... oh well, it will make the wrangling easier and causality even more ambigious.


