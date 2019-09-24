from getRichOrDieTrying.User import User
from getRichOrDieTrying.Market import Market
from getRichOrDieTrying.Portfolio import Portfolio


def main():

    #Initialize market
    security_data = {"Apple": 239, "Shell": 100, "Google": 1200}
    market = Market(security_data)

    #create a portfolio with securities
    securities = {"Apple": 2, "Shell": 1}

    securities.keys()
    portfolio = Portfolio(securities, 100000)
    print("portfolio value")
    print(portfolio.value(market))


    name = input("What is your name?")
    cash_deposit = input("How much cash would you like to deposit?")
    user1 = User(name, int(cash_deposit))


    print(user1.name)
    print(user1.cash)


main()
