class Portfolio:
    def __init__(self, fin_products, cash_account):
        self.fin_products = fin_products
        self.cash_account = cash_account

    def update_portfolio(self, security, amount):

        #make a list/dictionary of the financial products in your portfolio and update when one is added through Order class
        print("update portfolio")

    def show_value(self):
        Market.value(self.fin_products)
        print("Show value")

    def show_value_hist(self, date_range):
        print("Show value history")