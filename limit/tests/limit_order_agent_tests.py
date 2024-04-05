# Importing the required module for unittest
import unittest
from unittest.mock import Mock
from limit.limit_order_agent import LimitOrderAgent


# Defining a test case class for LimitOrderAgent
class LimitOrderAgentTest(unittest.TestCase):

    # Setting up the test case
    def setUp(self):
        # Creating a mock object for execution client
        self.execution_client = Mock()
        # Creating an instance of LimitOrderAgent for testing
        self.agent = LimitOrderAgent(self.execution_client)

    # Defining a test method for buy order execution
    def test_buy_order_execution(self):
        # Add a buy order for IBM with a limit of $100
        self.agent.add_order("buy", "IBM", 1000, 100)

        # Simulate a price tick event where the price drops below the limit
        self.agent.on_price_tick("IBM", 99.5)

        # Ensure that the "buy" method of execution client is called once with specific arguments
        self.execution_client.buy.assert_called_once_with("IBM", 1000)

    # Defining a test method for sell order execution
    def test_sell_order_execution(self):
        # Add a sell order for IBM with a limit of $110
        self.agent.add_order("sell", "IBM", 1000, 110)

        # Simulate a price tick event where the price goes above the limit
        self.agent.on_price_tick("IBM", 110.5)

        # Ensure that the "sell" method of execution client is called once with specific arguments
        self.execution_client.sell.assert_called_once_with("IBM", 1000)


if __name__ == "__main__":
    unittest.main()
