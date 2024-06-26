# Interactive-Brokers--Renko
Created a desktop application in Python that interfaces with Interactive Brokers (IB) and displays basic Renko charts for three instruments.

Ensure these requirements for the application to execute:

Here's a step-by-step guide for you to execute the Python script:

1. **Install Python**: If you haven't already, please install Python on your computer. You can download it from the official website [python.org](https://www.python.org/) and follow the installation instructions for your operating system.

2. **Install Required Packages**: Once Python is installed, you'll need to install the `ib_insync` package. You can do this by opening a terminal or command prompt and running the following command:
   ```
   pip install ib_insync
   ```

3. **Download the Script**: I've provided you with the Python script. Please save it to a location on your computer where you can easily access it.

4. **Interactive Brokers Account**: You'll need an Interactive Brokers account to connect to the TWS (Trader Workstation) or Gateway. If you don't have one yet, please sign up for an account on the Interactive Brokers website.

5. **Configure TWS or Gateway**: Before running the script, you need to configure the TWS or Gateway application from Interactive Brokers. Make sure to enable API access and configure it to allow connections from localhost.

6. **Adjust Script Configuration**: In the Python script, there are parameters related to the connection to Interactive Brokers, such as host, port, and client ID. Please adjust these parameters according to your setup:
   - `host`: The IP address of the machine where TWS or Gateway is running. By default, it's set to `127.0.0.1`, which is localhost.
   - `port`: The port number used by TWS or Gateway. The default port for TWS is `7496`, and for Gateway, it's `4001`.
   - `clientId`: This is a unique identifier for the client application connecting to TWS or Gateway. Choose any positive integer, but ensure it's unique if you're running multiple instances of the script simultaneously.

Since I'm using a demo acccount, i would be expecting you would have an account of your own.

7. **IB Gateway or TWS Running**: Before running the script, ensure that IB Gateway or TWS is running on the specified host and port.

8. **Run the Script**: You can execute the Python script by navigating to the directory where the script is saved using the terminal or command prompt, and then running the following command:
   ```
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the Python script file.

9. **View Renko Charts**: After running the script, a Tkinter application window will open, displaying Renko charts for three instruments: EURUSD, GBPUSD, and AAPL. You can switch between the charts by clicking the corresponding buttons.

That's it! You should now be able to execute the Python script and view the Renko charts for the specified instruments. If you encounter any issues, feel free to reach out for further assistance.