class Article:

    def __init__(self, article_id, data):
        self.article_id = article_id
        self.data = data

    def search(self):

        record_id = self.data.loc[self.data["id"] == self.article_id, "id"].any()
        print(record_id)

        if not record_id:
            return None

        else:
            name = self.data.loc[self.data["id"] == self.article_id, "name"].squeeze()
            price = self.data.loc[self.data["id"] == self.article_id, "price"].squeeze()

            return [name, price]



    def available(self):
        count = self.data.loc[self.data["id"] == self.article_id, "in stock"].squeeze()

        if count > 0:
            return True
        else:
            return False