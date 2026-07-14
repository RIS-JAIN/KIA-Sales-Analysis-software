import pymysql
import pandas as pd
from tabulate import tabulate
import warnings

warnings.filterwarnings('ignore')

conn = pymysql.connect(
    user='root', host='localhost', passwd='123', database='sales_analysis', charset='utf8'
)
cursor = conn.cursor(pymysql.cursors.DictCursor)


def _input_str(prompt: str) -> str:
    return input(prompt + ": ").strip()


def _input_int(prompt: str) -> int:
    while True:
        val = input(prompt + ": ").strip()
        try:
            return int(val)
        except ValueError:
            print("Please enter a valid integer.")


def add_user():
    name = _input_str("NAME")
    mobile = _input_str("MOBILE-NO")
    try:
        cursor.execute("INSERT INTO user VALUES (%s, %s)", (name, mobile))
        conn.commit()
        print("USER ADDED")
    except Exception as e:
        print("Error adding user:", e)


def add_manager():
    name = _input_str("ENTER NAME")
    branch = _input_str("ENTER BRANCH")
    try:
        cursor.execute("INSERT INTO manager VALUES (%s, %s)", (name, branch))
        conn.commit()
        print("WELCOME MANAGER", name)
    except Exception as e:
        print("Error adding manager:", e)


def add_row():
    model = _input_str("ENTER MODEL")
    area = _input_str("ENTER AREA")
    year = _input_int("ENTER YEAR")
    months = [
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    sales = []
    try:
        for m in months:
            sales.append(_input_int(f"ENTER SALES IN {m}"))

        placeholders = ",".join(["%s"] * (2 + 1 + len(sales)))
        sql = f"INSERT INTO sales_report VALUES ({placeholders})"
        params = tuple([model, area, year] + sales)
        cursor.execute(sql, params)
        conn.commit()
        print("DATA ADDED")

        select_sql = "SELECT * FROM sales_report WHERE year=%s AND model=%s AND area=%s"
        df = pd.read_sql(select_sql, conn, params=(year, model, area))
        print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
    except Exception as e:
        print("Error adding row:", e)


def delete_row():
    model = _input_str("ENTER MODEL")
    area = _input_str("ENTER AREA")
    year = _input_int("ENTER YEAR")

    select_sql = "SELECT * FROM sales_report WHERE year=%s AND model=%s AND area=%s"
    df = pd.read_sql(select_sql, conn, params=(year, model, area))

    try:
        cursor.execute(select_sql, (year, model, area))
        row = cursor.fetchone()
        if row:
            cursor.execute(
                "DELETE FROM sales_report WHERE year=%s AND model=%s AND area=%s",
                (year, model, area),
            )
            conn.commit()
            print("ROW DELETED")
            print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
        else:
            print("DATA NOT FOUND")
    except Exception as e:
        print("Error deleting row:", e)

