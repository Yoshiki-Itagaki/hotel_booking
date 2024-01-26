import pandas as pd
from pdf_code import PdfData
from article import Article

df = pd.read_csv("articles.csv", dtype={"id": str})
print(df)

article_ID = input("Enter the ID of the article you want.")
article = Article(article_ID, df)

result = article.search()

if result is None:
    print(result)
    print("NO ARTICLE FOUND.")
else:
    name = result[0]
    price = result[1]
    pdf = PdfData()
    pdf.generate(article_ID, name, price)




