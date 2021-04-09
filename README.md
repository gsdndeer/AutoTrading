# AutoTrading

In this project, I used a series of previous stock prices to decide my future actions and maximized maximize profits.


## Data
The training data is [NASDAQ:IBM](https://www.nasdaq.com/market-activity/stocks/ibm), contains about 6 years daily prices. And the testing data contains 20 days daily prices.
| ![]() |
| :--: |
|*trainin data*|


## Action type
The action should be one of these three types:

1 → means to “Buy” the stock. If I short 1 unit, I will return to 0 as the open price in the next day. If I did not have any unit, I will have 1 unit as the open price in the next day.

0 → means to “NoAction”. If I have 1-unit now, hold it. If my slot is available, the status continues. If I short 1 unit, the status continues.

-1 → means to “Sell” the stock. If I hold 1 unit, I will return to 0 as the open price in the next day. If I did not have any unit, I will short 1 unit as the open price in the next day. 


## Method
First step, I used LSTM to predict future 20 days daily prices.
Second step, I 

| Epoch | ep20 | ep500 | ep1500 |
| :--: | :--: | :--: |:--: |
| Figure | ![]() | ![]() | ![]() |
| Profit | +4.82 | + | +6.94 |
