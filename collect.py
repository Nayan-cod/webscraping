from bs4 import BeautifulSoup
import pandas as pd
import os

d={'title':[],'price':[],'link':[]}

for file in os.listdir("data2"):
   
   with open(f"data2/{file}",encoding="utf-8") as f:
      
      try:

        html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        t=soup.find("h2")
        title=t.get_text()

        l=t.find("a")
        link="https://amazon.in/"+l['href']

        p=soup.find("span",attrs='a-price-whole')
        price=p.get_text()

        d["link"].append(link)
        d["title"].append(title)
        d["price"].append(price)
      except Exception as e:
         print(e)
         
df=pd.DataFrame(data=d)
df.to_csv("leptop.csv")