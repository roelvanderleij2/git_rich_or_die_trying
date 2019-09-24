from getRichOrDieTrying.User import User
from getRichOrDieTrying.Market import Market
import datetime as dt


def main():

    #Initialize market
    security_data = {"Apple": 239, "Shell": 100, "Google": 1200}
    market = Market()
    market.load_securities(["GOOGL","MSFT"])

    print("Welcome to Git Rich Or Die Trying investment platform")
    name = input("To open an account enter your Name:\n")
    cash_deposit = int(input("How much cash would you like to deposit in your account?\n"))
    user1 = User(name, cash_deposit)

    #acquired_securities = user.create_order(buy, "Google", 1)

    #create a portfolio with securities
    acquired_securities = {"GOOGL": 2, "MSFT": 1}

    user1.portfolio.update_portfolio(acquired_securities)

    print("portfolio value")
    print(user1.portfolio.value(market, dt.datetime(2019,9,23)))

main()
