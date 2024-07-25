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
def hist_full():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTUBER','NOVEMBER','DECEMBER'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_january():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','JANUARY'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_february():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','FEBRUARY'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_march():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','MARCH'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_april():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','APRIL'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_may():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','MAY'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_june():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','JUNE'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_july():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','JULY'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_august():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','AUGUST'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_september():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','SEPTEMBER'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_octuber():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','OCTUBER'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_november():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','NOVEMBER'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
def hist_december():
    df=pd.read_csv("Book1.csv", usecols=['MODEL','DECEMBER'],index_col=False, delimiter = ',')
    df.plot(kind='hist',edgecolor='indigo',linewidth=2,linestyle=':',fill=False,hatch='o')
    plt.show()
