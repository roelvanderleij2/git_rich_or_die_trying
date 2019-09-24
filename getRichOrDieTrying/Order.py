class Order:
    def __init__(self, security_name, amount):
        self.security_name = security_name
        self.amount = amount

    def buy(self):
        value = Market.value(security_name)
        return (value * self.amount) * - 1


    def sell(self):
        value = Market.value(security_name)
        return (value * self.amount)
