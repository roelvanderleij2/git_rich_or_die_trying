from getRichOrDieTrying.Portfolio import Portfolio
from getRichOrDieTrying.CashAccount import CashAccount
import pandas as pd

class User:
    trade_list = []
    def __init__(self, name, start_cash):
        self.name = name
        self.portfolio = Portfolio(None, start_cash)
        self.cash_account = CashAccount(start_cash)

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

        self.trade_list += new_trades

   def execute_trades(self, market, date):
       proceed_order = input("Are you sure you would like to execute these trades (Yes/No?")
       if proceed_order == 'Yes':

           df = pd.DataFrame(columns=['Ticker','Market Value', 'Order Type', 'Amount'])
           for order in self.trade_list:
               order_list = []
               if order['Order Type'] == 'Buy':
                   order_list = [order['ticker'], market.get_value(order['ticker'], date), order['Order Type'], order['Amount']]
               elif order['Order Type'] == 'Sell':
                   order_list = [order['ticker'], -1 * market.get_value(order['ticker'], date), order['Order Type'], order['Amount']]

               df.append(order_list)
               df.set_index('Ticker')

           # Check if you have enough cash in your cash account to execute the order.
           if self.cash_account.value() > df['Market Value'].sum():

               for index, order in df:
                   if order['Order Type'] == 'Buy':

                       self.portfolio.update_portfolio({index, int(order['Amount'])})
                       self.cash_account.update_cash_account(order['Market Value'] * int(order['Amount']))
                       print("Bought" + order['Amount'] + "stock of" + index + "and added to your portfolio.")

                   elif order['Order Type'] == 'Sell':

                       self.portfolio.update_portfolio({index, -1 * int(order['Amount'])})
                       self.cash_account.update_cash_account(order['Market Value'] * int(order['Amount']))
                       print("Sold" + order['Amount'] + "stock of" + index + "and removed from your portfolio.")

           else:
               print("You do not have enough cash in your account to execute this order. No trades executed.")

       else:
           print("No trades executed.")
