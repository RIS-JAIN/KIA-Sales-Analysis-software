import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import sqlalchemy as sq
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
conn= pymysql.connect(user = 'root',
                              host = 'localhost',
                              passwd='123',    
                              database = 'sales_analysis',
                              charset='utf8')
cursor=conn.cursor()
def read_file():
    engine=sq.create_engine('mysql+pymysql://root:123@localhost:3306/sales_analysis?charset=utf8')
    df=pd.read_csv("Book1.csv", index_col=False, delimiter = ',')
    print(df)
def search_cars_report():
    q="select * from cars_report;"
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")
def search_user_list():
    q="select * from user;"
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")
def search_manager_list():
    q="select * from manager;"
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")        
def search_by_model():
    a=input("ENTER MODEL")
    q="select * from sales_report where model = '{}' ;".format(a)
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")        
def search_model_by_year():
    a=input("ENTER MODEL")
    b=input("ENTER  YEAR")
    q="select * from sales_report where model='{}' and year={};".format(a,b)
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")
def search_model_by_area():
    a=input("ENTER MODEL")
    b=input("ENTER AREA")
    q="select * from sales_report where model='{}' and area='{}';".format(a,b)
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")
def search_model_by_year_and_area():
    a=input("ENTER YEAR")
    b=input("ENTER MODEL")
    c=input("ENTER AREA")
    q="select * from sales_report where year={} and model='{}' and area='{}';".format(a,b,c)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")
def search_sales_report():
    q="select * from sales_report"
    cursor.execute(q)
    if cursor.fetchone():
        df=pd.read_sql(q,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))   
    else:
        print("DATA NOT FIND")
        
        
