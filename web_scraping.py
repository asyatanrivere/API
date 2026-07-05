from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
dataset="dataset"
os.makedirs(dataset,exist_ok=True)
# import time
# import random
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
    "Referer":"https://www.google.com/",
    "Accept-Language":"tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"

}
# time.sleep(random.uniform(1,5))
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.text,"html.parser")

table=soup.find_all("table")[0]
titles=table.find_all("th")
table_titles=[item.text.strip() for item in titles]
print(table_titles) # ['Rank', 'Name', 'Industry', 'Revenue (USD millions)', 'Revenue growth', 'Employees', 'Headquarters']

df=pd.DataFrame(columns=table_titles)

print(df)
rows=table.find_all("tr")
print("-----------------------------------------------------------")
for row in rows[1:]:
    row_data=row.find_all("td")
    individual_row=[data.text.strip() for data in row_data]
    lenght=len(df)
    df.loc[lenght]=individual_row
print(df)
"""
   Rank                Name                    Industry Revenue (USD millions) Revenue growth  Employees              Headquarters
0     1             Walmart                      Retail                680,985           5.1%  2,100,000     Bentonville, Arkansas
1     2              Amazon  Retail and cloud computing                637,959          11.0%  1,556,000       Seattle, Washington
2     3  UnitedHealth Group                  Healthcare                400,278           7.7%    400,000     Minnetonka, Minnesota
3     4               Apple                  Technology                391,035           2.0%    164,000     Cupertino, California
4     5          CVS Health                  Healthcare                372,809           4.2%    259,500  Woonsocket, Rhode Island
..  ...                 ...                         ...                    ...            ...        ...                       ...
95   96    General Dynamics       Aerospace and defense                 47,716          12.9%    117,000          Reston, Virginia
96   97           Coca-Cola                    Beverage                 47,061           2.9%     69,700          Atlanta, Georgia
97   98                TIAA                  Financials                 46,946           2.6%     15,623   New York City, New York
98   99           Travelers                   Insurance                 46,423          12.2%     34,000   New York City, New York
99  100           Eli Lilly              Pharmaceutical                 45,043          32.0%     47,000     Indianapolis, Indiana"""

df.to_csv(f'{dataset}/companies.csv', index=False, encoding='utf-8')