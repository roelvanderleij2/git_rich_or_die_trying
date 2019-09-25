from .Portfolio import Portfolio
from .CashAccount import CashAccount
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
            ticker = input("Provide the ticker of the security you would like to trade?\n")
            order_type = input("What type of order would you like to do (e.g. Buy, Sell, Limit, Stop-Loss)?\n")
            amount = input("How much of this security would you like to trade?\n")
            trade_dict = {'Ticker': ticker, 'Order Type': order_type, 'Amount': amount}
            new_trades.append(dict(trade_dict))
            continue_statement = input("Would you like to add another trade (True/False)?\n")

        self.trade_list += new_trades

    def execute_trades(self, market, date):
        proceed_order = input("Are you sure you would like to execute these trades (Yes/No)?\n")
        if proceed_order == 'Yes':
            column_names = ['Ticker', 'Market Value', 'Order Type', 'Amount']
            df = pd.DataFrame(columns=column_names)
            #df.set_index('Ticker')

            for order in self.trade_list:
                order_list = []
                if order['Order Type'] == 'Buy':
                    order_list = [order['Ticker'], market.get_value(order['Ticker'], date), order['Order Type'],
                                  order['Amount']]
                elif order['Order Type'] == 'Sell':
                    order_list = [order['Ticker'], -1 * market.get_value(order['Ticker'], date), order['Order Type'],
                                  order['Amount']]

                row = pd.Series(order_list, column_names)
                df = df.append(row, ignore_index=True)
            print(df.head())
                # Check if you have enough cash in your cash account to execute the order.
            if self.cash_account.value() > df['Market Value'].sum():

                for row in df.iterrows():
                    if row['Order Type'] == 'Buy':

                        self.portfolio.update_portfolio({row['Ticker'], int(row['Amount'])})
                        self.cash_account.update_cash_account(-1 * row['Market Value'] * int(row['Amount']))
                        print("Bought" + row['Amount'] + "stock of" + row['Ticker'] + "and added to your portfolio.")

                    elif row['Order Type'] == 'Sell':
                        if not self.portfolio.fin_products.keys().__contains__(row['Ticker']):
                            print("You do not have this instrument in your portfolio")
                            return
                        elif self.portfolio.fin_products[row['Ticker']] >= row['Amount']:
                                self.portfolio.update_portfolio({row['Ticker'], -1 * int(row['Amount'])})
                                self.cash_account.update_cash_account(-1 * row['Market Value'] * int(row['Amount']))
                                print("Sold" + row['Amount'] + "stock of" + row['Ticker'] + "and removed from your portfolio.")
                        else:
                            print("You do not have enough stock in your portfolio to execute the sell order")

            else:
                print("You do not have enough cash in your account to execute this order. No trades executed.")

        else:
            print("No trades executed.")
