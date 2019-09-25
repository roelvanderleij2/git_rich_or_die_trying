class Order:
    def __init__(self, ticker, order_type, amount):
        self.ticker = ticker
        self.order_type = order_type
        self.amount = amount

    def buy(self):
        value = Market.value(security_name)
        return (value * self.amount) * - 1


    def sell(self):
        value = Market.value(security_name)
        return (value * self.amount)
