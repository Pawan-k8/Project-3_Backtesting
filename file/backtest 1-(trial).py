import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

# Simulated Data for the Backtest (for example, daily closing prices)
data = {
    'Date': pd.date_range(start="2020-01-01", periods=100, freq='D'),
    'Close': np.random.randn(100).cumsum() + 100  # Simulated stock price
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Parameters for moving averages
short_window = 10
long_window = 50

# Calculate short and long moving averages
df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate signals
df['Signal'] = 0
df['Signal'][short_window:] = np.where(df['Short_MA'][short_window:] > df['Long_MA'][short_window:], 1, 0)
df['Position'] = df['Signal'].diff()

# Backtest
initial_balance = 10000
balance = initial_balance
shares = 0
for i in range(1, len(df)):
    if df['Position'][i] == 1:  # Buy signal
        shares = balance // df['Close'][i]  # Buy as many shares as possible
        balance -= shares * df['Close'][i]
    elif df['Position'][i] == -1:  # Sell signal
        balance += shares * df['Close'][i]  # Sell all shares
        shares = 0

# End value of the portfolio
final_value = balance + shares * df['Close'].iloc[-1]
profit_loss = final_value - initial_balance

# Display output
print(f"Initial Balance: ${initial_balance}")
print(f"Final Value: ${final_value}")
print(f"Profit/Loss: ${profit_loss}")

# Plot the results using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Close'], label='Close Price', color='black')
ax.plot(df['Short_MA'], label=f'{short_window}-Day Moving Average', color='blue')
ax.plot(df['Long_MA'], label=f'{long_window}-Day Moving Average', color='red')

# Plot Buy and Sell signals
ax.plot(df[df['Position'] == 1].index, df['Short_MA'][df['Position'] == 1], '^', markersize=10, color='green', lw=0, label='Buy Signal')
ax.plot(df[df['Position'] == -1].index, df['Short_MA'][df['Position'] == -1], 'v', markersize=10, color='red', lw=0, label='Sell Signal')

ax.set_title('Moving Average Crossover Strategy Backtest')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()

# Show plot in tkinter window
root = Tk()
root.title("Backtesting Strategy Results")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
