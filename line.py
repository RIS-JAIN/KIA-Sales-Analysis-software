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
def line_full():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()    
def line_2016():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df2=df[df.YEAR==2016]
    df2.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()
def line_2017():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df2=df[df.YEAR==2017]
    df2.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()
def line_2018():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df2=df[df.YEAR==2018]
    df2.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()
def line_2019():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df2=df[df.YEAR==2019]
    df2.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()
def line_2020():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','YEAR','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df2=df[df.YEAR==2020]
    df2.plot(kind='line', marker='*', markersize='4',linewidth=2,linestyle='dashdot')
    plt.show()
