from getRichOrDieTrying.User import User
from getRichOrDieTrying.Market import Market
from flask import Flask, render_template, request
import datetime as dt

app = Flask(__name__)


@app.route("/profile/<username>/<int:id_number>",
           methods=["GET", "POST"])  # the user will ask for this web-page where the user should enter the variable
# username and id_number
def profile(username, id_number):
    return render_template("profile.html", username=username, id_number=id_number)


#if __name__ == "__main__":
#    app.run(debug=True)


def main():
    # Initialize market
    market = Market()

    print("Welcome to Git Rich Or Die Trying investment platform")
    name = input("To open an account enter your Name:\n")
    cash_deposit = int(input("How much cash would you like to deposit in your account?\n"))
    user1 = User(name, cash_deposit)

    #create a portfolio with securities
    user1.define_trades()
    print(user1.trade_list)
    user1.execute_trades(market, dt.datetime(2019, 9, 23))

    print(user1.portfolio.cash_account.value())
    print(user1.portfolio.historical_performance(market))

main()
