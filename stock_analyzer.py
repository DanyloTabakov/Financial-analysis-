import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import moving_average, daily_returns, volatility

class StockAnalyzer:
    def __init__(self, filepath):
        # convert date column (datetime- inbuilt function), and initialize attributes
        self.df = pd.read_csv(filepath)
        self.df['Date'] =  pd.to_datetime(self.df['Date'])
        self.close_prices = self.df['Close'].values

    def compute_moving_average(self, window=5):
        # Use moving_average from utils
        avgs = moving_average(self.df['Close'].values, window)
        self.df[f'Avgs_{window}'] = [np.nan] * (window - 1) + avgs
        return np.array(avgs)

    def compute_daily_returns(self):
        # Use daily_returns from utils
        self.df['Daily_Returns'] = self.df['Close'].pct_change()

        return self.df['Daily_Returns'].dropna()


    def compute_volatility(self):
        # Use volatility function on daily returns
        daily_returns = self.compute_daily_returns()
        
        return daily_returns.std()

    def plot_data(self, window=5):
        # Plot close prices and moving average
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['Close'], label='Close Price')
        plt.title('Close Price and Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()