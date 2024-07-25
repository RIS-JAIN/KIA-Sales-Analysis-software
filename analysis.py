import pymysql
import pandas as pd
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
conn= pymysql.connect(user = 'root',
                              host = 'localhost',
                              passwd='123',    
                              database = 'sales_analysis',
                              charset='utf8')
cursor=conn.cursor()
def report_summary():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.describe())
def search_index():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.index)
def search_columns():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.columns)
def search_datatypes():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.dtypes)
def search_values():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.values)
def search_shape():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.shape)
def search_size():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.size)
def search_transpose():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.T)
def search_head():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    a=int(input("HOW MANY VALUES YOU WANT TO SEE:"))
    print(df.head(a))          
def search_tail():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    a=int(input("HOW MANY VALUES YOU WANT TO SEE:"))
    print(df.tail(a))
def search_empty():
    q="select*from sales_report;"
    df=pd.read_sql(q,conn)
    print(df.empty)
 
