class Market:
    def __init__(self, security_data):
        self.security_data = security_data


    def load(self, directory):
        print("Load data")

    def value(self, fin_products):
        securities_value = 0
        for product_name in fin_products.keys():
            securities_value += self.security_data[product_name] * fin_products[product_name]
        return securities_value

