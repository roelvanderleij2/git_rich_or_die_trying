from getRichOrDieTrying.User_Account import User_Account
from getRichOrDieTrying.Market import Market
from flask import Flask, render_template, request, redirect, send_file
import datetime as dt
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import timedelta
from getRichOrDieTrying.Utilities import plot_performance


plt.style.use('ggplot')

app = Flask(__name__)

market = Market()
user = User_Account("TestUser", 0)
current_date = dt.datetime(2019, 9, 16)
hist_performance_start_date = dt.datetime(2019, 9, 9)


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


def hist_performance(stock_ticker):
    tempUser = User_Account("Temp", 100000000)
    tempUser.trade_list = [{'Ticker': stock_ticker, 'Order Type': "Buy", 'Amount': 1}]
    tempUser.execute_trades(market, hist_performance_start_date)
    fig, ax = plt.subplots()
    df = pd.DataFrame.from_dict(tempUser.portfolio.historical_performance(market), orient='index', columns=['Market Value'])
    df['Market Value'].plot()
    fig.savefig("static/img.png")



@app.route("/new_trade", methods=["GET", "POST"])
# the user will ask for this web-page where the user should enter the variable
# username and id_number
def new_trade():
    if request.method == "POST":

        stock_ticker = request.form['stock']

        if "check_perfomance" in request.form:
            hist_performance(stock_ticker)
            return render_template("new_trade.html", title="new_trade", stock_ticker=stock_ticker)

        # get the form data from the user
        num_sequrities = request.form["number"]
        type_order = request.form['type']

        new_trades = []
        trade = {'Ticker': stock_ticker, 'Order Type': type_order, 'Amount': int(num_sequrities)}
        new_trades.append(dict(trade))
        user.trade_list += new_trades

        return redirect("home")
    else:
        stock_ticker = None
        return render_template("new_trade.html", title="new_trade", stock_ticker=None)


if __name__ == "__main__":
    app.run(debug=True)


def main():
    # Initialize market
    market = Market()
    start_date = dt.datetime(2019, 1, 2)
    view_date = dt.datetime(2019, 9, 25)

    print("Welcome to Git Rich Or Die Trying investment platform")
    name = input("To open an account enter your Name:\n")
    cash_deposit = int(input("How much cash would you like to deposit in your account?\n"))
    user_account = User_Account(name, cash_deposit)

    #create a portfolio with securities
    user_account.define_trades()
    user_account.execute_trades(market, start_date)

    cash_amount = user_account.cash_amount()
    portfolio_value = user_account.portfolio_value(market, start_date)
    abs_profit_loss = user_account.abs_profit_loss_value(market, start_date, view_date)
    rel_profit_loss = user_account.rel_profit_loss_value(market, start_date, view_date)
    print("Your cash position is:", cash_amount, ".")
    print("Your portfolio value is:", portfolio_value, ".")
    print("Your profit/loss is:", abs_profit_loss, ".")
    print("Your profit/loss percentage is:", rel_profit_loss, ".")

    df = pd.DataFrame.from_dict(user_account.portfolio.historical_performance(market), orient='index', columns=['Portfolio Value'])
    plot_performance(df, 'Historical Portfolio Performance', 'Date Range', 'Portfolio Value')
    plt.show()

main()
