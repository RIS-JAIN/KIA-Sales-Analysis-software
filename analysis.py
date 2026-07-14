import pymysql
import pandas as pd
from tabulate import tabulate
import warnings

warnings.filterwarnings('ignore')

conn = pymysql.connect(
    user='root', host='localhost', passwd='123', database='sales_analysis', charset='utf8'
)

_DF_CACHE = None


def _input_int(prompt: str, default: int = 5) -> int:
    try:
        val = int(input(prompt + ": ").strip())
        return max(0, val)
    except Exception:
        return default


def get_sales_df(refresh: bool = False) -> pd.DataFrame:
    global _DF_CACHE
    if _DF_CACHE is None or refresh:
        _DF_CACHE = pd.read_sql("SELECT * FROM sales_report", conn)
    return _DF_CACHE


def report_summary():
    df = get_sales_df()
    print(tabulate(df.describe(), headers="keys", tablefmt="psql"))


def search_index():
    df = get_sales_df()
    print(list(df.index))


def search_columns():
    df = get_sales_df()
    print(list(df.columns))


def search_datatypes():
    df = get_sales_df()
    print(df.dtypes)


def search_values():
    df = get_sales_df()
    print(df.values)


def search_shape():
    df = get_sales_df()
    print(df.shape)


def search_size():
    df = get_sales_df()
    print(df.size)


def search_transpose():
    df = get_sales_df()
    print(df.T)


def search_head():
    df = get_sales_df()
    a = _input_int("HOW MANY VALUES YOU WANT TO SEE", 5)
    print(tabulate(df.head(a), headers="keys", tablefmt="psql", showindex=False))


def search_tail():
    df = get_sales_df()
    a = _input_int("HOW MANY VALUES YOU WANT TO SEE", 5)
    print(tabulate(df.tail(a), headers="keys", tablefmt="psql", showindex=False))


def search_empty():
    df = get_sales_df()
    print(df.empty)
 
