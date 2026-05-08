import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, OptionMenu, StringVar, Label, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

# Simulated Data for the Backtest (for example, daily closing prices)
data = {
    'Date': pd.date_range(start="2020-01-01", periods=100, freq='D'),
    'Close': np.random.randn(100).cumsum() + 100  # Simulated stock price
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Strategy 1: Moving Average Crossover
def moving_average_crossover():
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

    return fig, f"Profit/Loss: ${profit_loss:.2f}"

# Strategy 2: Simple Buy & Hold Strategy
def buy_and_hold():
    initial_balance = 10000
    balance = initial_balance
    shares = balance // df['Close'][0]  # Buy as many shares as possible at the start
    balance -= shares * df['Close'][0]

    # End value of the portfolio
    final_value = balance + shares * df['Close'].iloc[-1]
    profit_loss = final_value - initial_balance

    # Plot the results using matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Close'], label='Close Price', color='black')

    ax.set_title('Buy & Hold Strategy Backtest')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    return fig, f"Profit/Loss: ${profit_loss:.2f}"

# Function to switch between strategies
def update_dashboard(strategy_choice):
    if strategy_choice == "Strategy 1":
        fig, result = moving_average_crossover()
    else:
        fig, result = buy_and_hold()

    # Update result label
    result_label.config(text=result)

    # Update plot in tkinter window
    canvas.get_tk_widget().destroy()  # Remove the old canvas
    canvas.figure = fig  # Set new figure
    canvas.draw()  # Draw the new figure

# Tkinter GUI setup
root = Tk()
root.title("Backtesting Strategy Dashboard")

# Frame for dropdown and result label
top_frame = Frame(root)
top_frame.pack(pady=10)

# Dropdown for choosing strategies
strategy_var = StringVar(value="Strategy 1")
strategy_dropdown = OptionMenu(top_frame, strategy_var, "Strategy 1", "Strategy 2", command=update_dashboard)
strategy_dropdown.pack(side="left", padx=10)

# Label for displaying Profit/Loss result
result_label = Label(top_frame, text="Profit/Loss: $0.00", font=("Helvetica", 12))
result_label.pack(side="left")

# Frame for the plot
plot_frame = Frame(root)
plot_frame.pack(pady=20)

# Initial plot
fig, result = moving_average_crossover()
result_label.config(text=result)

# Show plot in tkinter window
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack()

# Start the tkinter loop
root.mainloop()
