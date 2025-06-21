📊 Financial Data Analyzer

A Python application that loads financial time series data and performs basic analysis. It provides visualizations, moving averages, daily returns, and volatility measures for stock data.

🚀 Features
Load and process stock data from a CSV file
Compute:
Moving averages
Daily returns
Volatility (standard deviation of returns)
Generate plots with matplotlib
Modular and object-oriented design
🗂 Project Structure
Financial-analysis-/
├── sample_stock_data.csv         # Sample input data
├── main.py                       # Entry point: runs the analysis
├── stock_analyzer.py             # StockAnalyzer class with core logic
├── finance_utils.py              # Helper functions for computations
└── output_plot.png               # Output plot (created on runtime)
📦 Requirements
Python 3.x
pandas
numpy
matplotlib
Install dependencies using:

pip install -r requirements.txt
📈 Usage
python main.py
Or in code:

from stock_analyzer import StockAnalyzer

analyzer = StockAnalyzer('sample_stock_data.csv')
analyzer.plot_data(window=10)
print("Volatility:", analyzer.compute_volatility())
🧠 Core Components
StockAnalyzer (in stock_analyzer.py)

__init__(filepath) — Loads and prepares data
compute_moving_average(window=5) — Rolling average of closing prices
compute_daily_returns() — Daily % returns
compute_volatility() — Standard deviation of returns
plot_data(window=5) — Plot of closing prices & moving average
finance_utils.py

moving_average(data, window)
daily_returns(data)
volatility(returns)
📌 Sample Data
The provided sample_stock_data.csv should contain columns:

Date — in YYYY-MM-DD format
Close — closing stock price
Volume — trading volume
🌱 Extension Ideas
Analyze multiple stocks and compare metrics
Flag anomalies or sharp price movements
Export processed data for further analysis
🧑‍💻 Author
Danylo Tabakov