from getRichOrDieTrying.Order import Order
from getRichOrDieTrying.Portfolio import Portfolio

class User:
    trade_list = []
    def __init__(self, name, start_cash):
        self.name = name
        self.portfolio = Portfolio(None, start_cash)

    def name(self):
        return self.name

    def define_trades(self):
        continue_statement = True
        new_trades = []
        while continue_statement == True:
            ticker = input("Provide the ticker of the security you would like to trade?")
            order_type = input("What type of order would you like to do (e.g. Buy, Sell, Limit, Stop-Loss)?")
            amount = input("How much of this security would you like to trade?")
            trade_dict = {'Ticker': ticker, 'Order Type': order_type, 'Amount': amount}
            new_trades.append(dict(trade_dict))
            continue_statement = input("Would you like to add another trade (True/False)?")

        self.trade_list.append(new_trades)
