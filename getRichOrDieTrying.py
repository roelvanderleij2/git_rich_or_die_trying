from getRichOrDieTrying.User import User
from getRichOrDieTrying.Market import Market
from flask import Flask, render_template, request, redirect
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

app = Flask(__name__)

market = Market()
user = User("TestUser", 0)
current_date = dt.datetime(2019, 9, 16)


@app.route("/home", methods=["GET", "POST"])
def home():

    global current_date
    if request.method == "POST":
        if "execute_trades" in request.form:
            user.execute_trades(market, current_date)
            return redirect("home")
        elif "add_trade" in request.form:
            return redirect("new_trade")
        elif "next_day" in request.form:

            current_date = current_date + timedelta(days=1)
            if dt.datetime.weekday(current_date) == 5:
                current_date = current_date + timedelta(days=2)
            elif dt.datetime.weekday(current_date) == 6:
                current_date = current_date + timedelta(days=1)
            return redirect("home")
        elif "today" in request.form:
            current_date = dt.datetime.now()
            return redirect("home")


        cash = int(request.form["cash"])
        user.portfolio.cash_account.update_cash_account(cash)
        return redirect("home")
    else:
        return render_template("home.html", user_account=user, market=market, current_date=current_date)

@app.route("/new_trade", methods=["GET", "POST"])
# the user will ask for this web-page where the user should enter the variable
# username and id_number
def new_trade():
    if request.method == "POST":
        # get the form data from the user
        num_sequrities = request.form["number"]
        type_order = request.form['type']
        stock_ticker = request.form['stock']

        new_trades = []
        trade = {'Ticker': stock_ticker, 'Order Type': type_order, 'Amount': int(num_sequrities)}
        new_trades.append(dict(trade))
        user.trade_list += new_trades

        print(stock_ticker)
        return redirect("home")
    else:
        return render_template("new_trade.html", title="new_trade")


if __name__ == "__main__":
    app.run(debug=True)


def main():
    # Initialize market
    market = Market()
    start_date = dt.datetime(2019, 9, 16)

    print("Welcome to Git Rich Or Die Trying investment platform")
    name = input("To open an account enter your Name:\n")
    cash_deposit = int(input("How much cash would you like to deposit in your account?\n"))
    user1 = User(name, cash_deposit)

    #create a portfolio with securities
    user1.define_trades()

    user1.execute_trades(market, start_date)

    user1.portfolio.cash_account.value()

    user1.portfolio.value(market, current_date)
    print(user1.trade_list)
    user1.execute_trades(market, dt.datetime(2019, 9, 23))


    print(user1.portfolio.cash_account.value())
    print(user1.portfolio.value(market, start_date))
    print(user1.portfolio.historical_performance(market))
    df = pd.DataFrame.from_dict(user1.portfolio.historical_performance(market), orient='index', columns=['Market Value'])
    print(df)
    plt.plot(df.index.values, df['Market Value'])

#main()
