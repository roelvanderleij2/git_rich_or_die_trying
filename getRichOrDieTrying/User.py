from getRichOrDieTrying.Portfolio import Portfolio

class User:
    def __init__(self, name, start_cash):
        self.name = name
        self.portfolio = Portfolio(None, start_cash)



    def name(self):
        return self.name
