# Importing PriceListener, ExecutionClient class from trading_framework module
from trading_framework.price_listener import PriceListener
from trading_framework.execution_client import ExecutionClient


class LimitOrderAgent(PriceListener):

    # Calling the constructor of the parent class
    def __init__(self, execution_client: ExecutionClient) -> None:
        """
        Initialize LimitOrderAgent.

        :param execution_client: An instance of ExecutionClient used to buy or sell assets.
                                 See ExecutionClient protocol definition.
        """

        super().__init__()
        self.execution_client = execution_client
        # Initializing an empty list to store orders
        self.orders = []

    def on_price_tick(self, product_id: str, price: float):
        """
        Handle price ticks received from the market.

        :param product_id: The ID of the product (e.g., stock, cryptocurrency) for which the price tick is received.
        :param price: The current price of the product.
        """

        # Iterating over a copy of orders list to avoid modifying it while iterating
        for order in self.orders[:]:
            # Checking if the order is for the same product
            if order["product_id"] == product_id:
                # Checking if the price meets buy condition
                if order["action"] == "buy" and price <= order["limit"]:
                    # Executing buy order
                    self.execution_client.buy(product_id, order["amount"])
                    # Removing the executed order from the orders list
                    self.orders.remove(order)

                # Checking if the price meets sell condition
                elif order["action"] == "sell" and price >= order["limit"]:
                    # Executing sell order
                    self.execution_client.sell(product_id, order["amount"])
                    # Removing the executed order from the orders list
                    self.orders.remove(order)

    def add_order(self, action: str, product_id: str, amount: int, limit: float):
        """
        Add a new order to the list of orders.

        :param action: Action to perform (either 'buy' or 'sell').
        :param product_id: The ID of the product for which the order is placed.
        :param amount: The amount of the product to buy or sell.
        :param limit: The price at which the order will be executed.
        """

        # Appending the new order to the orders list
        self.orders.append({"action": action, "product_id": product_id, "amount": amount, "limit": limit})
