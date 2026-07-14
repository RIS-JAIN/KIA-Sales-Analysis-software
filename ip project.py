import design
import important
import add
import search
import update
import analysis
import pie
import bar
import histogram
import line
import column

def prompt_int(prompt="", valid=None):
    while True:
        try:
            value = int(input(prompt))
            if valid is None or value in valid:
                return value
        except Exception:
            pass
        design.pattern()
        print("INVALID INPUT. TRY AGAIN")


def manager_update_menu():
    fields = {
        1: update.update_1,
        2: update.update_2,
        3: update.update_3,
        4: update.update_4,
        5: update.update_5,
        6: update.update_6,
        7: update.update_7,
        8: update.update_8,
        9: update.update_9,
        10: update.update_10,
        11: update.update_11,
        12: update.update_12,
        13: update.update_13,
        14: update.update_14,
        15: update.update_15,
    }
    while True:
        design.pattern()
        print("PLS ENTER THE FIELD YOU WANT TO UPDATE")
        print("ENTER YOUR CHOICE :-  \n1.MODEL\n2.AREA\n3.YEAR\n4.JANUARY\n5.FEBRUARY\n6.MARCH\n7APRIL\n8.MAY\n9.JUNE\n10.JULY\n11.AUGUST\n12.SEPTEMBER\n13.OCTUBER\n14.NOVEMBER\n15.DECEMBER\n16.EXIT")
        choice = prompt_int("")
        if choice == 16:
            break
        action = fields.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def line_menu():
    actions = {
        1: line.line_full,
        2: line.line_2016,
        3: line.line_2017,
        4: line.line_2018,
        5: line.line_2019,
        6: line.line_2020,
    }
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.LINE CHART ON FULL DATASET \n2.LINE CHART ON YEAR 2016\n3.LINE CHART ON YEAR 2017\n4.LINE CHART ON YEAR 2018")
        print("5.LINE CHART ON YEAR 2019\n6.LINE CHART ON YEAR 2020\n7.EXIT")
        choice = prompt_int("")
        if choice == 7:
            break
        action = actions.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def bar_menu():
    actions = {
        1: bar.bar_model,
        2: bar.bar_2016,
        3: bar.bar_2017,
        4: bar.bar_2018,
        5: bar.bar_2019,
        6: bar.bar_2020,
    }
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.BAR CHART ON MODLE \n2.BAR CHART ON YEAR 2016\n3.BAR CHART ON YEAR 2017\n4.BAR CART ON YEAR 2018")
        print("5.BAR CHART  ON YEAR 2019\n6.BAR CHART ON YEAR 2020\n7.EXIT")
        choice = prompt_int("")
        if choice == 7:
            break
        action = actions.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def histogram_menu():
    actions = {
        1: histogram.hist_full,
        2: histogram.hist_january,
        3: histogram.hist_february,
        4: histogram.hist_march,
        5: histogram.hist_april,
        6: histogram.hist_may,
        7: histogram.hist_june,
        8: histogram.hist_july,
        9: histogram.hist_august,
        10: histogram.hist_september,
        11: histogram.hist_octuber,
        12: histogram.hist_november,
        13: histogram.hist_december,
    }
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.HISTOGRAM CHART FULL ANALYSIS\n2.HISTOGRAM CHART ON JANUARY SALES\n3.HISTOGRAM CHART ON FEBRUARY SALES\n4.HISTOGRAM CHART ON MARCH SALES\n5.HISTOGRAM CHART ON APRIL SALES")
        print("6.HISTOGRAM CHART ON MAY SALES\n7.HISTOGRAM CHART ON JUNE SALES\n8.HISTOGRAM CHART ON JULY SALES\n9.HISTOGRAM CHART ON AUGUST SALES\n10.HISTOGRAM CHART ON SEPTEMBER SALES")
        print("11.HISTOGRAM CHART ON OCTUBER SALES\n12.HISTOGRAM CHART ON NOVEMBER SALES\n13.HISTOGRAM CHART ON DECEMBER SALES\n14.EXIT")
        choice = prompt_int("")
        if choice == 14:
            break
        action = actions.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def pie_menu():
    actions = {
        1: pie.pie_january,
        2: pie.pie_february,
        3: pie.pie_march,
        4: pie.pie_april,
        5: pie.pie_may,
        6: pie.pie_june,
        7: pie.pie_july,
        8: pie.pie_august,
        9: pie.pie_september,
        10: pie.pie_octuber,
        11: pie.pie_november,
        12: pie.pie_december,
    }
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE \n1.PIE CHART ON JANUARY SALES\n2.PIE CHART ON FEBRUARY SALES\n3.PIE CHART ON MARCH SALES\n4.PIE CHART ON APRIL SALES")
        print("5.PIE CHART ON MAY SALES\n6.PIE CHART ON JUNE SALES\n7.PIE CHART ON JULY SALES\n8.PIE CHART ON AUGUST SALES\n9.PIE CHART ON SEPTEMBER SALES")
        print("10.PIE CHART ON OCTUBER SALES\n11.PIE CHART ON NOVEMBER SALES\n12.PIE CHART ON DECEMBER SALES\n13.exit")
        choice = prompt_int("")
        if choice == 13:
            break
        action = actions.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def graphical_menu():
    while True:
        design.pattern()
        print("ENTER  YOUR CHOICE \n1.LINE CHART\n2.BAR CHART\n3.HISTOGRAM CHART\n4.PIE CHART\n5.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            line_menu()
        elif choice == 2:
            design.pattern()
            bar_menu()
        elif choice == 3:
            design.pattern()
            histogram_menu()
        elif choice == 4:
            design.pattern()
            pie_menu()
        elif choice == 5:
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


def tabular_menu():
    while True:
        design.pattern()
        search.search_cars_report()
        print("ENTER YOUR CHOICE\n1.SEARCH BY MODEL \n2.SEARCH MODEL BY YEAR\n3.SEARCH MODEL BY AREA")
        print("4.SEARCH MODEL BY YEAR AND AREA\n5.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            search.search_by_model()
        elif choice == 2:
            design.pattern()
            search.search_model_by_year()
        elif choice == 3:
            design.pattern()
            search.search_model_by_area()
        elif choice == 4:
            design.pattern()
            search.search_model_by_year_and_area()
        elif choice == 5:
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


def deep_analysis_menu():
    actions = {
        1: analysis.report_summary,
        2: analysis.search_index,
        3: analysis.search_columns,
        4: analysis.search_datatypes,
        5: analysis.search_values,
        6: analysis.search_shape,
        7: analysis.search_size,
        8: analysis.search_transpose,
        9: analysis.search_head,
        10: analysis.search_tail,
        11: analysis.search_empty,
    }
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.REPORT SUMMARY\n2.SHOW INDEX\n3.SHOW COLUMNS\n4.SHOW DATATYPES\n5.SHOW VALUES")
        print("6.SHOW SHAPE\n7.SHOW SIZE\n8.SHOW TRANSPOSE\n9.SHOW N ROES FROM TOP\n10.SHOW N ROWS FROM BOTTEM\n11.SHOW EMPTY\n12.EXIT")
        choice = prompt_int("")
        if choice == 12:
            break
        action = actions.get(choice)
        if action:
            design.pattern()
            action()
        else:
            design.pattern()
            print("INVALID CHOICE")


def user_menu():
    design.pattern()
    add.add_user()
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.TABULAR ANALYSIS \n2.GRAPHICAL ANALYSIS\n3.READ CSV\n4.DEEP ANALYSIS\n5.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            tabular_menu()
        elif choice == 2:
            design.pattern()
            graphical_menu()
        elif choice == 3:
            design.pattern()
            search.read_file()
        elif choice == 4:
            design.pattern()
            deep_analysis_menu()
        elif choice == 5:
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


def admin_menu():
    if prompt_int("PLS ENTER PASSWORD TO CONTINUE") != 54321:
        design.pattern()
        print("WRONG!! PASSWORD")
        return
    design.pattern()
    print("WELCOME BOSS")
    while True:
        design.pattern()
        print("ENTER YOUR CHOICE \n1.MANAGER ENTRY LIST\n2.USER ENTRY LIST\n3.ADD COLUMN\n4.DELETE COLUMN\n5.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            search.search_manager_list()
        elif choice == 2:
            design.pattern()
            search.search_user_list()
        elif choice == 3:
            design.pattern()
            column.new_column()
        elif choice == 4:
            design.pattern()
            column.drop_column()
        elif choice == 5:
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


def manager_menu():
    if prompt_int("PLS ENTER PASSWORD  TO CONTINUE ...") != 12345:
        design.pattern()
        print("WORNG!! PASSWORD")
        return
    design.pattern()
    add.add_manager()
    while True:
        design.pattern()
        print("ENTER  YOUR  CHOICE \n1.NEW DATA\n2.UPDATE DATA \n3.DELETE DATA\n4.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            add.add_row()
        elif choice == 2:
            design.pattern()
            manager_update_menu()
        elif choice == 3:
            design.pattern()
            add.delete_row()
        elif choice == 4:
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


def main():
    print("WELCOME")
    print("PLS TRUN YOUR CAPSLOCK ON")
    print("ARE YOU A USING IT ON THIS SYSTEM FIRST TIME \n1.YES \n2.NO")
    if prompt_int("=>", valid={1, 2}) == 1:
        important.imp()
        design.pattern()
        print("WELCOME TO KIA SALES MANAGEMENT SYSTEM")
    else:
        print("WELCOME BACK")

    while True:
        design.pattern()
        print("ENTER YOUR CHOICE\n1.MANAGER\n2.USER\n3.ADDMINISTRATION\n4.EXIT")
        choice = prompt_int("")
        if choice == 1:
            design.pattern()
            manager_menu()
        elif choice == 2:
            design.pattern()
            user_menu()
        elif choice == 3:
            design.pattern()
            admin_menu()
        elif choice == 4:
            design.pattern()
            print("THANK YOU......")
            break
        else:
            design.pattern()
            print("INVALID CHOICE")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        design.pattern()
        print("SORRY!!! SERVER ERROR PLS TRY AGAIN LATER")
