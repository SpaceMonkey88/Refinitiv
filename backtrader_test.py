import backtrader as bt
import datetime
import yfinance as yf

# Create a Strategy
class TestStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if self.dataclose[0] < self.dataclose[-1]:
            if self.dataclose[-1] < self.dataclose[-2]:
                self.buy()

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(TestStrategy)

# Download data using yfinance
data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')

# Convert the data to a format that Backtrader can use
data_feed = bt.feeds.PandasData(dataname=data)

# Add the Data Feed to Cerebro
cerebro.adddata(data_feed)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Run over everything
cerebro.run()

# Plot the result
cerebro.plot()