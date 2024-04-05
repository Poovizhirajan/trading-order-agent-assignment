# Limit Order Agent

# Overview
The Limit Order Agent is a Python module designed to automate trading activities based on predefined limit orders. This agent listens to price tick events from the market and executes buy or sell orders when the current price meets the specified limits.

# Features
* Automated execution of buy and sell orders based on predefined limits.
* Integration with an execution client for actual buying and selling of assets.
* Support for handling price tick events from multiple products.

# Installation
To use the Limit Order Agent, follow these steps:
1. Clone the repository:
**git clone git@github.com:Poovizhirajan/trading-order-agent-assignment.git**

2. Navigate to the directory:
**cd limit-order-agent**

3. Install the dependencies:
**pip install -r requirements.txt**

# Usage
To use the Limit Order Agent in your application, follow these steps:
1. Import the necessary classes:
**from limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient**

2. Create an instance of the ExecutionClient:
**execution_client = ExecutionClient()**

3. Create an instance of the LimitOrderAgent:
**agent = LimitOrderAgent(execution_client)**

4. Add orders using the add_order method:
**agent.add_order("buy", "IBM", 1000, 100)**

5. Listen for price tick events and handle them:
**agent.on_price_tick("IBM", 99.5)**

6. Run your application.

# Testing
The Limit Order Agent includes unit tests to ensure its functionality. To run the tests, execute the following command:

**python -m unittest limit\tests\limit_order_agent_tests.py**

# License
The Limit Order Agent is licensed under the MIT License. See the LICENSE file for details.

# Contact
If you have any questions or suggestions, feel free to contact us at poovizhimech84@gmail.com. We'd love to hear from you!