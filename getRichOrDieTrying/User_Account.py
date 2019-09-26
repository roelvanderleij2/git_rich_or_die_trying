from .Portfolio import Portfolio
from .CashAccount import CashAccount
import pandas as pd
import numpy as np

class User_Account:
    trade_list = []

    def __init__(self, name, start_cash):
        self.name = name
        self.portfolio = Portfolio(None, start_cash)

    def cash_amount(self):
        return self.portfolio.cash_value()

    def portfolio_value(self, market, date):
        return self.portfolio.value(market, date)

    def abs_profit_loss_value(self, market, start_date):
        return self.portfolio.abs_profit_loss(market, start_date)

    def rel_profit_loss_value(self, market, start_date):
        return self.portfolio.rel_profit_loss(market, start_date)

    def name(self):
        return self.name

    def define_trades(self):
        continue_statement = "True"
        new_trades = []
        while continue_statement == "True":
            ticker = input("Provide the ticker of the security you would like to trade?\n")
            order_type = input("What type of order would you like to do (e.g. Buy, Sell, Limit, Stop-Loss)?\n")
            amount = input("How much of this security would you like to trade?\n")
            trade_dict = {'Ticker': ticker, 'Order Type': order_type, 'Amount': amount}
            new_trades.append(dict(trade_dict))
            continue_statement = input("Would you like to add another trade (True/False)?\n")

        self.trade_list += new_trades

    def execute_single_order(self, row):
        if row['Order Type'] == 'Buy':

            costs = -1 * row['Market Value'] * int(row['Amount'])

            self.portfolio.update_portfolio({row['Ticker']: int(row['Amount'])}, costs, row['Date'])

        elif row['Order Type'] == 'Sell':

            if not self.portfolio.fin_products.keys().__contains__(row['Ticker']):
                print("You do not have this instrument in your portfolio")
                return
            elif self.portfolio.fin_products[row['Ticker']] >= (-1 * int(row['Amount'])):

                profit = -1 * row['Market Value'] * int(row['Amount'])

                self.portfolio.update_portfolio({row['Ticker']: int(row['Amount'])}, profit, row['Date'])
            else:
                print("You do not have enough stock in your portfolio to execute the sell order")

    def execute_trades(self, market, date):
        proceed_order = 'Yes' #input("Are you sure you would like to execute these trades (Yes/No)?\n")
        if proceed_order == 'Yes':
            column_names = ['Ticker', 'Market Value', 'Order Type', 'Amount', 'Date']
            df = pd.DataFrame(columns=column_names)

            for order in self.trade_list:
                order_list = []
                if order['Order Type'] == 'Buy':
                    order_list = [order['Ticker'], market.get_value(order['Ticker'], date), order['Order Type'],
                                  order['Amount'], date]
                elif order['Order Type'] == 'Sell':
                    order_list = [order['Ticker'], market.get_value(order['Ticker'], date), order['Order Type'],
                                  -1 * int(order['Amount']), date]

                row = pd.Series(order_list, column_names)
                df = df.append(row, ignore_index=True)

            total_order_value = df.apply(lambda row: row['Market Value'] * int(row['Amount']), axis=1).sum()

            # Check if you have enough cash in your cash account to execute the order.
            if self.portfolio.cash_account.value() > total_order_value:

                df.apply(self.execute_single_order, axis=1)
                print(self.portfolio.fin_products)
            else:
                print("You do not have enough cash in your account to execute this order. No trades executed.")
                return
        else:
            print("No trades executed.")
            return

        self.trade_list = []