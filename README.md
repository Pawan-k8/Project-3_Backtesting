# Project-3_Backtesting

## Backtesting script with moving average crossover

### Duration: oct 2024 - dec 2024

**Git upload : 8 may 2026**

## Summary:

This script creates a small GUI Backtesting dashboard for two trading strategies on simulated stock prices. It first generates fake daily closing prices, then defines 

(1) a moving-average crossover strategy that buys when a short moving average goes above a long one and sells when it goes below, and 

(2) a simple buy-and-hold strategy that buys once at the start and holds to the end. Each strategy computes final Profit/Loss, plots the price (and indicators/signals for the crossover), 

and returns a matplotlib figure plus a result string. Tkinter is used to build a window with a dropdown to switch strategies; when you change the selection, it reruns the chosen strategy, updates the Profit/Loss label, and redraws the corresponding chart inside the GUI.

## Basic Workflow

    Program
    |_ Data setup
    |   |_ Import libraries
    |   |_ Generate simulated prices (df)
    |
    |_ Strategies
    |   |_ moving_average_crossover
    |   |   |_ Calculate MAs
    |   |   |_ Generate signals & positions
    |   |   |_ Backtest loop (buy/sell)
    |   |   |_ Plot price + MAs + markers
    |   |
    |   |_ buy_and_hold
    |       |_ Buy at start
    |       |_ Hold to end
    |       |_ Compute P/L
    |       |_ Plot price
    |
    |_ GUI
        |_ Build widgets (root, frames, dropdown, label)
        |_ Initial plot (run MA crossover)
        |_ update_dashboard on dropdown change
        |_ mainloop (event loop)

## Tools 
Python, SQL, VS code, Excel, Json

## Libraries used 
Pandas, Matplotlib, tKinter, SmartApi, pyotp, asyncio, Telegram

## API connection
AngelOne API

## Market 
NSE

## Steps

1- The program first imports libraries, generates 100 days of simulated stock prices into a pandas DataFrame.

2- defines two backtest strategies (moving average crossover and buy & hold) with their logic for computing signals, executing trades, and calculating Profit/Loss. 

3- It then defines a GUI update function that chooses the correct strategy when the dropdown changes, updates the Profit/Loss label, and redraws the matplotlib figure in the Tkinter window. 

4- Finally, it builds the Tkinter interface (window, frames, dropdown, label, plot area), runs the moving average strategy once to show the initial chart and result, and enters the main event loop so the user can switch strategies interactively.

## Architecture

    Backtesing Script
    |_ Start
    |   |_ Import libraries
    |   |_ Create simulated DataFrame (dates + Close)
    |
    |_ Define logic
    |   |_ Define moving_average_crossover
    |   |   |_ Compute Short_MA and Long_MA
    |   |   |_ Create Signal and Position
    |   |   |_ Run buy/sell backtest loop
    |   |   |_ Compute final value and Profit/Loss
    |   |   |_ Create matplotlib figure
    |   |
    |   |_ Define buy_and_hold
    |       |_ Buy shares on first day
    |       |_ Hold until last day
    |       |_ Compute final value and Profit/Loss
    |       |_ Create matplotlib figure
    |
    |_ Define GUI behavior
    |   |_ Define update_dashboard
    |       |_ Choose strategy based on dropdown
    |       |_ Update result label
    |       |_ Clear old plot and draw new figure
    |
    |_ Run GUI
        |_ Create root window, frames, dropdown, label
        |_ Run initial moving_average_crossover and display plot + P/L
        |_ Start mainloop (wait for user to change strategy, update dashboard)

## Results

The code builds a simple interactive backtesting dashboard using simulated price data, two basic strategies, and a Tkinter GUI. 

for calculations, a loop for trade simulation, and embedded in Tkinter for visualization.

## Conclusion

By switching strategies from the dropdown, the user can visually and numerically compare Profit/Loss behavior under different trading rules. 

This is a good starting pattern for expanding to real market data and more advanced strategies.
