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
engine=sq.create_engine('mysql+pymysql://root:123@localhost:3306/sales_analysis?charset=utf8')
def pie_january():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='JANUARY',legend=True,autopct="%.2f")
    plt.show()  
def pie_february():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','FEBRUARY'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='FEBRUARY',legend=True,autopct="%.2f")
    plt.show()
def pie_march():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','MARCH'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='MARCH',legend=True,autopct="%.2f")
    plt.show()
def pie_april():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','APRIL'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='APRIL',legend=True,autopct="%.2f")
    plt.show()
def pie_may():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','MAY'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='MAY',legend=True,autopct="%.2f")
    plt.show()
def pie_june():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JUNE'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='JUNE',legend=True,autopct="%.2f")
    plt.show()
def pie_july():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JULY'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='JULY',legend=True,autopct="%.2f")
    plt.show()
def pie_august():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','AUGUST'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='AUGUST',legend=True,autopct="%.2f")
    plt.show()
def pie_september():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','SEPTEMBER'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='SEPTEMBER',legend=True,autopct="%.2f")
    plt.show()
def pie_octuber():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','OCTUBER'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='OCTUBER',legend=True,autopct="%.2f")
    plt.show()
def pie_november():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','NOVEMBER'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='NOVEMBER',legend=True,autopct="%.2f")
    plt.show()
def pie_december():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','DECEMBER'],index_col=False, delimiter = ',')
    df.set_index('MODEL',inplace=True)
    a=int(input("ENTER THE YEAR"))
    df2=df[df.YEAR==a]
    df2.plot(kind='pie',y='DECEMBER',legend=True,autopct="%.2f")
    plt.show()
