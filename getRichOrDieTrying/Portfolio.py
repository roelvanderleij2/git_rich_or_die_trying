from getRichOrDieTrying.CashAccount import CashAccount

class Portfolio:
    def __init__(self, fin_products, cash_amount):
        self.fin_products = fin_products
        self.cash_account = CashAccount(cash_amount)

    def update_portfolio(self, product_mutations):
        #fin_products must be a dictionary with product name and plus or minus amount

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
                    if (self.fin_products[product] + product_mutations[product] >= 0):
                        self.fin_products[product] += product_mutations[product]
                    else:
                        raise Exception("Cannot have negative amount of a product in the portfolio")
                else:
                    if product_mutations[product] >= 0:
                        self.fin_products[product] = product_mutations[product]

    def value(self, market, date):

        # Return the value of the securities in the fin_products dictionary on date
        securities_value = 0

        for ticker in self.fin_products.keys():
            # Increment the return variable with the current security value
            securities_value += market.get_value(ticker, date) * self.fin_products[ticker]

        return securities_value + self.cash_account.value()

    def show_value_hist(self, date_range):
        print("Show value history")