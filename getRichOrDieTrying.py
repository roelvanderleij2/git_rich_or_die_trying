from getRichOrDieTrying import User
from getRichOrDieTrying import Market


def main():

    name = input("What is your name?")
    cash_deposit = input("How much cash would you like to deposit?")

    user1 = User.User(name, int(cash_deposit))

    print(user1.name)
    print(user1.cash)



main()


