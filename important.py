import pymysql
import pandas as pd
import sqlalchemy as sq
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
conn= pymysql.connect(user = 'root',
                              host = 'localhost',
                              passwd='123',    
                              charset='utf8')
cursor=conn.cursor()
def imp():
    cursor.execute('drop database if exists sales_analysis')
    cursor.execute('create database sales_analysis;')
    engine=sq.create_engine('mysql+pymysql://root:123@localhost:3306/sales_analysis?charset=utf8')
    df=pd.read_csv("Book1.csv", index_col=False, delimiter = ',')
    df.to_sql('sales_report',engine,if_exists="replace",index=False)
    df=pd.read_csv("Book2.csv", index_col=False, delimiter = ',')
    df.to_sql('cars_report',engine,if_exists="replace",index=False)
    cursor.execute('use sales_analysis;')
    cursor.execute('create table user(Name varchar(200),mobile_no bigint(12));')
    cursor.execute('create table manager(Name varchar(200),branch varchar(200));')

