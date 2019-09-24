class Portfolio:
    def __init__(self, fin_products, cash_acmount):
        self.fin_products = fin_products
        self.cash_acmount = cash_acmount

    def update_portfolio(self, security, amount):

        #make a list/dictionary of the financial products in your portfolio and update when one is added through Order class
        print("update portfolio")

    def value(self, market):
        securities_value = market.value(self.fin_products)
        return securities_value + self.cash_acmount

    def show_value_hist(self, date_range):
        print("Show value history")