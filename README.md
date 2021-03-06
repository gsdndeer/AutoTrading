# AutoTrading

In this project, I used a series of previous stock prices to decide my future actions and maximize profits.


## Usage

``` python trader.py --training training.csv -- testing testing.csv --output output.csv ```


## Data
The training data is [NASDAQ:IBM](https://www.nasdaq.com/market-activity/stocks/ibm), contains about 6 years daily prices. And the testing data contains 20 days daily prices.
| ![](https://github.com/gsdndeer/AutoTrading/blob/main/figures/train.jpg) |
| :--: |
|*training data*|


## Action type
The action should be one of these three types:

1 → means to “Buy” the stock. If I short 1 unit, I will return to 0 as the open price in the next day. If I did not have any unit, I will have 1 unit as the open price in the next day.

0 → means to “NoAction”. If I have 1-unit now, hold it. If my slot is available, the status continues. If I short 1 unit, the status continues.

-1 → means to “Sell” the stock. If I hold 1 unit, I will return to 0 as the open price in the next day. If I did not have any unit, I will short 1 unit as the open price in the next day. 


## Method
### I. Used LSTM to predict future 20 days daily prices.
### II. Decided actions by using the following algorithm.
Let F be the stock price of the day after tomorrow minus the stock price of tomorrow and C be current stock{-1, 0, 1} in hand.
```
(CASE 1) C == 0         
    (CASE 1A) F > 0                  
        ACTION : 1                         
    (CASE 1B) F < 0                      
        ACTION : -1                         
    (CASE 1C) F = 0
        ACTION : 0 

(CASE 2) C == 1
    (CASE 2A) F >= 0
        ACTION : 0
    (CASE 2B) F < 0
        ACTION : -1  

(CASE 3) C == -1
    (CASE 3A) F <= 0
        ACTION : 0
    (CASE 3B) F > 0
        ACTION : 1
```

## Result

| Epoch | ep20 | ep500 | ep1500 |
| :--: | :--: | :--: |:--: |
| Figure | ![](https://github.com/gsdndeer/AutoTrading/blob/main/figures/epoch20.jpg) | ![](https://github.com/gsdndeer/AutoTrading/blob/main/figures/epoch500.jpg) | ![](https://github.com/gsdndeer/AutoTrading/blob/main/figures/epoch1500.jpg) |
