import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import sqlalchemy as sq
import warnings
warnings.filterwarnings('ignore')
conn= pymysql.connect(user = 'root',
                              host = 'localhost',
                              password='123',
                              database = 'sales_analysis',
                              charset='utf8')
cursor=conn.cursor()
engine=sq.create_engine('mysql+pymysql://root:123@localhost:3306/sales_analysis?charset=utf8')


def _plot(usecols, **plot_kwargs):
    df = pd.read_csv("Book1.csv", usecols=usecols, index_col=False, delimiter=',')
    defaults = dict(kind='hist', edgecolor='indigo', linewidth=2, linestyle=':', fill=False, hatch='o')
    defaults.update(plot_kwargs)
    df.plot(**defaults)
    plt.show()


def hist_full():
    cols = ['MODEL', 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTUBER', 'NOVEMBER', 'DECEMBER']
    _plot(cols)


def _make_month_func(month):
    def fn():
        _plot(['MODEL', month])
    fn.__name__ = f'hist_{month.lower()}'
    return fn


hist_january = _make_month_func('JANUARY')
hist_february = _make_month_func('FEBRUARY')
hist_march = _make_month_func('MARCH')
hist_april = _make_month_func('APRIL')
hist_may = _make_month_func('MAY')
hist_june = _make_month_func('JUNE')
hist_july = _make_month_func('JULY')
hist_august = _make_month_func('AUGUST')
hist_september = _make_month_func('SEPTEMBER')
hist_octuber = _make_month_func('OCTUBER')
hist_november = _make_month_func('NOVEMBER')
hist_december = _make_month_func('DECEMBER')
