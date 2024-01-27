import pandas as pd


class Hotel:

    def __init__(self, hotel_id):

        df = pd.read_csv("hotels.csv", dtype={"id": str})

        print(df)
        self.hotel_id = hotel_id
        self.df = df
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def match_id(self):

        hotel_id = self.df.loc[self.df["id"] == self.hotel_id, "id"].any()
        print(hotel_id)

        if not hotel_id:
            return False
        else:
            return True

    def available(self):

        availability = self.df.loc[self.df["id"] == self.hotel_id, "available"]
        print(availability)
        availability = self.df.loc[self.df["id"] == self.hotel_id, "available"].squeeze()
        print(availability)
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        self.df.loc[self.df["id"] == self.hotel_id, "available"] = "no"
        self.df.to_csv("hotels.csv", index=False)
