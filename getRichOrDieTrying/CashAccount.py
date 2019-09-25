class CashAccount:
    def __init__(self, start_cash):
        self.cash_position = start_cash

    def value(self):
        return self.cash_position

    def update_cash_account(self, amount):
        self.cash_position += amount