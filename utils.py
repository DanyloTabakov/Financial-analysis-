import numpy as np

def moving_average(data, window):
    moving_avgs = []
    i = 0
    while i < len(data) - window + 1:
        window_avg = np.sum(data[i:i+window]) / window
        moving_avgs.append(window_avg)
        i += 1

    return moving_avgs

def daily_returns(data):
    returns = (np.array(data[1:]) - np.array(data[:-1])) / np.array(data[:-1])
    return returns

def volatility(returns):
    
    return round(np.std(returns), 2)
    