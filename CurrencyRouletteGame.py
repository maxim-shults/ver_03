from currency_converter import CurrencyConverter
import random

def get_money_interval(difficulty):

    c = CurrencyConverter()
    usd_price = c.convert(1, "USD", "ILS")
    randoms = random.randint(1, 101)
    t = c.convert(randoms, "USD", "ILS")
    d = int(difficulty)
    interval = (t - (5 - d), t +(5 - d))
    amount_dollar = (t / usd_price)
    print("amount of dollar", round(amount_dollar,2), )
    return interval



def get_guess_from_user():
    while True:
        try:
            user_input=float(input("enter amount of dollars in shekels:"))
        except ValueError:
            print("only digits allowed please type again")
            continue
        else:
            return user_input

def play(difficulty):

    random_money = get_money_interval(difficulty)

    money_from_user = float(get_guess_from_user())

    if random_money[0] <= money_from_user <= random_money[1]:
        print("Congratulations, you won!")
        return True
    else:
        print("Sorry, you lost.")
        print('The interval was {}'.format(random_money))
        return False


