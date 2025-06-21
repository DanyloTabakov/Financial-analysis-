from stock_analyzer import StockAnalyzer

st_an = StockAnalyzer("sample_stock_data.csv")
# Create an instance of StockAnalyzer with the sample CSV
# Call the plot_data method
# Print the volatility

st_an.plot_data(window=10)
print("Volatility: ", st_an.compute_volatility())