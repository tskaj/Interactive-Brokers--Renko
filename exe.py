from ib_insync import IB, Forex, Stock
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define the function for Renko chart generation
def calculate_renko_bricks(price_data, brick_size):
    renko_bricks = []
    current_brick = None
    for i in range(len(price_data)):
        if current_brick is None:
            start_price = price_data[i]
            current_brick = {
                'start_price': start_price,
                'end_price': start_price + brick_size
            }
        else:
            start_price = renko_bricks[-1]['end_price']
            price_change = price_data[i] - start_price
            num_bricks = abs(price_change) // brick_size
            if price_change > 0:
                current_brick['end_price'] += num_bricks * brick_size
            elif price_change < 0:
                current_brick['end_price'] -= num_bricks * brick_size
            else:
                continue
        renko_bricks.append(current_brick)
        current_brick = None
    return renko_bricks

# Connect to the IB TWS or Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Adjust host and port as necessary

# Define contract details for the instruments
contract1 = Forex('EURUSD')
contract2 = Forex('GBPUSD')
contract3 = Stock(symbol='AAPL', exchange='SMART', currency='USD')

# Request historical data for the contracts
bars1 = ib.reqHistoricalData(contract1, endDateTime='', durationStr='30 D',
                              barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
bars2 = ib.reqHistoricalData(contract2, endDateTime='', durationStr='30 D',
                              barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
bars3 = ib.reqHistoricalData(contract3, endDateTime='', durationStr='30 D',
                              barSizeSetting='1 day', whatToShow='TRADES', useRTH=True)

# Extract closing prices from the historical data
prices1 = [bar.close for bar in bars1]
prices2 = [bar.close for bar in bars2]
prices3 = [bar.close for bar in bars3]

# Disconnect from the IB TWS or Gateway
ib.disconnect()

# Define Renko brick size
brick_size = 2  # Adjust as needed

# Generate Renko bricks for each instrument
renko_bricks1 = calculate_renko_bricks(prices1, brick_size)
renko_bricks2 = calculate_renko_bricks(prices2, brick_size)
renko_bricks3 = calculate_renko_bricks(prices3, brick_size)

# Create Tkinter Application Window
root = tk.Tk()
root.title("Renko Chart Application")
root.iconbitmap('IB logo.ico')

# Define function to plot Renko chart
def plot_renko_chart(fig, renko_bricks):
    ax = fig.add_subplot(111)
    for brick in renko_bricks:
        ax.plot([brick['start_price'], brick['end_price']], [brick['start_price'], brick['end_price']], color='black')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Renko Chart')

# Create separate figures for each Renko chart
fig1 = plt.figure()
plot_renko_chart(fig1, renko_bricks1)
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.draw()

fig2 = plt.figure()
plot_renko_chart(fig2, renko_bricks2)
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.draw()

fig3 = plt.figure()
plot_renko_chart(fig3, renko_bricks3)
canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.draw()

# Function to switch instruments
def switch_instrument():
    global canvas1, canvas2, canvas3
    if switch_button.config('text')[-1] == 'Show EURUSD Chart':
        switch_button.config(text='Show GBPUSD Chart')
        canvas1.get_tk_widget().pack_forget()
        canvas2.get_tk_widget().pack()
    elif switch_button.config('text')[-1] == 'Show GBPUSD Chart':
        switch_button.config(text='Show AAPL Chart')
        canvas2.get_tk_widget().pack_forget()
        canvas3.get_tk_widget().pack()
    else:
        switch_button.config(text='Show EURUSD Chart')
        canvas3.get_tk_widget().pack_forget()
        canvas1.get_tk_widget().pack()

# Empty space for future use
empty_space_label = tk.Label(root, text="Empty space for future use")
empty_space_label.pack()

# Button to switch instruments
switch_button = tk.Button(root, text="Show EURUSD Chart", command=switch_instrument, bg="#236192", fg="white", padx=10, pady=5)
switch_button.pack()

# Run Tkinter event loop
canvas1.get_tk_widget().pack()
root.mainloop()
