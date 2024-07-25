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
def add_user():
    try:
        a=input("NAME")
        b=input("MOBILE-NO")
        q="insert into user value('{}',{});".format(a,b)
        cursor.execute(q)
        conn.commit()
        print("USER ADDED")
    except:
        print("WRONG VALUE")       
def add_manager():
    try:
        a=input("ENTER NAME")
        b=input("ENTER BRANCH")
        q="insert into manager value('{}','{}');".format(a,b,)
        cursor.execute(q)
        conn.commit()
        print("WELCOME MANAGER",a)
    except:
        print("WRONG VALUE ENTERED")
def add_row():
    try:
        a=input("ENTER MODEL")
        b=input("ENTER AREA")
        c=int(input("ENTER YEAR"))
        d=int(input("ENTER SALES IN JAUARY"))
        e=int(input("ENTER SALES IN FEBRUARY"))
        f=int(input("ENTER SALES IN  MARCH"))
        g=int(input("ENTER SALES IN APRIL"))
        h=int(input("ENTER SALES IN MAY"))
        i=int(input("ENTER SALES IN  JUNE"))
        j=int(input("ENTER SALES IN JULY"))
        k=int(input("ENTER SALES IN AUGUST"))
        l=int(input("ENTER SALES IN SEPTEMBER"))
        m=int(input("ENTER SALES IN OCTUBER"))
        n=int(input("ENTER SALES IN NOVEMBER"))
        o=int(input("ENTER SALES IN DECEMBER"))
        q="insert into sales_report value('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{});".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        cursor.execute(q)
        conn.commit()
        print("DATA ADDED")
        z="select * from sales_report where year='{}' and model='{}' and area='{}';".format(c,a,b)
        df=pd.read_sql(z,conn)
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    except:
        print("RE ENTER THE VALUE")
def delete_row():
    a=input("ENTER MODEL")
    b=input("ENTER AREA")
    c=int(input("ENTER YEAR"))
    z="select * from sales_report where year={} and model='{}' and area='{}';".format(c,a,b)
    df=pd.read_sql(z,conn)
    q="select*from sales_report where model='{}' and area='{}' and year={};".format(a,b,c)
    cursor.execute(q)
    if cursor.fetchone:
        cursor.execute("delete from sales_report where AREA= '{}'and year={} and Model='{}';".format(b,c,a))
        conn.commit()
        print("ROW DELETED")
        print(tabulate(df,headers="keys",tablefmt="psql",showindex=False))
    else:
        print("DATA NOT FIND")      
