import pandas as pd


class CreditCard:
    def __init__(self, number):

        self.df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
        self.number = number

    def validate(self, expiration, holder, cvc):

        card_data = {"number": self.number,
                     "expiration": expiration,
                     "holder": holder,
                     "cvc": cvc}

        if card_data in self.df:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        df = pd.read_csv("card_security.csv", dtype=str)
        password = df.loc[df["number"] == self.number, "password"].squeeze()

        if password == given_password:
            return True
        else:
            return False
