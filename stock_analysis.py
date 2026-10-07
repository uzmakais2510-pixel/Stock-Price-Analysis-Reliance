import pandas as pd
import yfinance as yf
stock = yf.download(
    "RELIANCE.NS", start="2023-01-01", 
    end="2025-12-31"
)
stock.columns = stock.columns.droplevel(1)
print("Highest price:")
print(stock['Close'].max())

print("\nLowest price:")
print(stock['Close'].min())
print(stock.head())
print(stock.columns)

stock['Daily Return'] = stock['Close'].pct_change()
print(stock['Daily Return'].describe())

#If someone invested in Reliance Stock at the beginning of 2023, how much would they have made by the end of 2025?
close_prices = stock['Close'].squeeze()
print("Highest Price:", close_prices.max())
print("Lowest Price:", close_prices.min())

initial_price = close_prices.iloc[0]
final_price = close_prices.iloc[-1]
profit = final_price - initial_price
print(type(initial_price))
print(type(final_price))

print(f"\nIf someone invested in Reliance Stock at the beginning of 2023, they would have made a profit of INR {profit:.2f} by the end of 2025.")

total_return_percentage = (profit / initial_price) * 100

print(f"Total return percentage: {total_return_percentage:.2f}%")
print(f"Initial Price: INR {initial_price:.2f}")
print(f"Final Price: INR {final_price:.2f}")

#Best and worst days to invest in Reliance Stock
best_day = stock['Daily Return'].max()
worst_day = stock['Daily Return'].min()
print(f"\nBest Daily Return: {best_day:.2%}")
print(f"Worst Daily Return: {worst_day:.2%}")

volatility = stock['Daily Return'].std()

print(f"Daily Volatility: {volatility:.2%}")

import matplotlib.pyplot as plt
stock['Close'].plot(figsize=(10, 5))
plt.title("Reliance Stock Price (2023-2025)")
plt.xlabel("Date")
plt.ylabel("Closing Price (INR)")

plt.savefig("images/reliance_stock_price.png")  # Save the plot as a PNG file


plt.figure(figsize=(8,5))

stock['Daily Return'].hist(bins=50)

plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

plt.savefig("images/return_distribution.png")

plt.show()



