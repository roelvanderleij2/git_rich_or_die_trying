from getRichOrDieTrying.CashAccount import CashAccount
from getRichOrDieTrying.Utilities import copy_dictionary
from datetime import datetime, date, timedelta

class Portfolio:
    portfolio_history = {}

    def __init__(self, fin_products, cash_amount):
        self.fin_products = fin_products
        self.cash_account = CashAccount(cash_amount)

    def update_portfolio(self, product_mutations, price, date):
        # fin_products must be a dictionary with product name and plus or minus amount

        # when there is no portfolio yet,
        if self.fin_products is None:
            self.fin_products = {}
            for product in product_mutations:
                if product_mutations[product] >= 0:
                    self.fin_products[product] = product_mutations[product]
                else:
                    raise Exception("Cannot have negative amount of a product in the portfolio")
        else:
            for product in product_mutations:
                if self.fin_products.keys().__contains__(product):
                    if self.fin_products[product] + product_mutations[product] >= 0:
                        self.fin_products[product] += product_mutations[product]
                    else:
                        raise Exception("Cannot have negative amount of a product in the portfolio")
                else:
                    if product_mutations[product] >= 0:
                        self.fin_products[product] = product_mutations[product]

        self.cash_account.update_cash_account(price)
        self.save_current_state_of_portfolio(date)

    def get_last_portfolio_state(self, date):
        if self.portfolio_history.keys().__contains__(date):
            return self.portfolio_history[date]
        else:
            date = date - timedelta(days=1)

            if min(self.portfolio_history.keys()) <= date:
                return self.get_last_portfolio_state(date)
            else:
                raise Exception("no portfolio history available")

    def save_current_state_of_portfolio(self, date):
        portfolio_state = Portfolio(copy_dictionary(self.fin_products), self.cash_account.value())
        self.portfolio_history[date] = portfolio_state

    def value(self, market, date):
        # Return the value of the securities in the fin_products dictionary on date
        securities_value = 0

        for ticker in self.fin_products.keys():
            # Increment the return variable with the current security value
            securities_value += market.get_value(ticker, date) * self.fin_products[ticker]

        return securities_value + self.cash_account.value()

    def historical_performance(self, market):

        historical_portfolio_values = {}

        initial_date = min(self.portfolio_history.keys())
        last_date = datetime.now() - timedelta(days=1)
        delta = last_date - initial_date

        for i in range(delta.days + 1):
            day = initial_date + timedelta(days=i)

            day_value = self.get_last_portfolio_state(day).value(market, day)

            historical_portfolio_values[day] = day_value

        return historical_portfolio_values
