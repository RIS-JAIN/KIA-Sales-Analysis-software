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
q="select * from sales_report;"
df=pd.read_sql(q,conn)
def new_column():
    a=input("ENTER NEW COLUMN NAME")
    b=input("ENTER DEFAULT  VALUE")
    df[a]=b
    print(df)
    engine=sq.create_engine('mysql+pymysql://root:123@localhost:3306/sales_analysis?charset=utf8')
    df.to_sql("sales_report2",engine,if_exists="replace",index=False)
def drop_column():
    q="select * from sales_report;"
    dh=pd.read_sql(q,conn)
    print(dh)
    a=input("ENTER THE COLUMN NAME YOU WANT TO DELETE :")
    dh=dh.drop(a,axis=1)
    print(dh)    

