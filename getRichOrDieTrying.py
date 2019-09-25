from getRichOrDieTrying.User import User
from getRichOrDieTrying.Market import Market
from flask import Flask, render_template, request
import datetime as dt
from flask import Flask, render_template, request
import getRichOrDieTrying.Order

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

    # acquired_securities = user.create_order(buy, "Google", 1)

    # create a portfolio with securities
    user1.define_trades()
    print(user1.trade_list)

    acquired_securities = {"GOOGL": 2, "MSFT": 1}

    user1.portfolio.update_portfolio(acquired_securities)

    print("portfolio value:")
    print(user1.portfolio.value(market, dt.datetime(2019, 9, 23)))


main()
