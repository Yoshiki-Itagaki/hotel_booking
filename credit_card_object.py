import pandas as pd


class CreditCard:
    def __init__(self, number):

        self.df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
        self.number = number

    def validate(self, expiration, holder, cvc):
        print(self.number)
        print(type(self.number))
        print(self.df)
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "holder": holder,
                     "cvc": cvc}

        if card_data in self.df:
            return True
        else:
            return False


