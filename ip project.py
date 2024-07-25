import design
import important
print("WELCOME")
print("PLS TRUN YOUR CAPSLOCK ON")
print("ARE YOU A USING IT ON THIS SYSTEM FIRST TIME \n1.YES \n2.NO")
r=int(input("=>"))
if r==1:
    important.imp()
    design.pattern()
    print("WELCOME TO KIA SALES MANAGEMENT SYSTEM")
elif r==2:
    print("WELCOME BACK")
import add
import search
import update
import analysis
import pie
import bar
import histogram
import line
import column
try:
    while(True):
        design.pattern()
        print("ENTER YOUR CHOICE\n1.MANAGER\n2.USER\n3.ADDMINISTRATION\n4.EXIT")
        ch=int(input())
        if ch==1:
            design.pattern()
            print("PLS ENTER PASSWORD  TO CONTINUE ...")
            a=int(input())
            if a==12345:
                design.pattern()
                add.add_manager()
                try:
                    while(True):
                        design.pattern()
                        print("ENTER  YOUR  CHOICE \n1.NEW DATA\n2.UPDATE DATA \n3.DELETE DATA\n4.EXIT")
                        a=int(input(""))
                        if a==1:
                            design.pattern()
                            add.add_row()
                        elif a==2:
                            design.pattern()
                            print("PLS ENTER THE FIELD YOU WANT TO UPDATE")
                            print("ENTER YOUR CHOICE :-  \n1.MODEL\n2.AREA\n3.YEAR\n4.JANUARY\n5.FEBRUARY\n6.MARCH\n7APRIL\n8.MAY\n9.JUNE\n10.JULY\n11.AUGUST\n12.SEPTEMBER\n13.OCTUBER\n14.NOVEMBER\n15.DECEMBER\n16.EXIT")
                            g=int(input())
                            if g==1:
                                design.pattern()
                                update.update_1()
                            elif g==2:
                                design.pattern()
                                update.update_2()
                            elif g==3:
                                design.pattern()
                                update.update_3()
                            elif g==4:
                                design.pattern()
                                update.update_4()
                            elif g==5:
                                design.pattern()
                                update.update_5()
                            elif g==6:
                                design.pattern()
                                update.update_6()
                            elif g==7:
                                design.pattern()
                                update.update_7()
                            elif g==8:
                                design.pattern()
                                update.update_8()
                            elif g==9:
                                design.pattern()
                                update.update_9()
                            elif g==10:
                                design.pattern()
                                update.update_10()
                            elif g==11:
                                design.pattern()
                                update.update_11()
                            elif g==12:
                                design.pattern()
                                update.update_12()
                            elif g==13:
                                design.pattern()
                                update.update_13()
                            elif g==14:
                                design.pattern()
                                update.update_14()
                            elif g==15:
                                design.pattern()
                                update.update_15()
                            elif g==16:
                                design.pattern()
                                break
                        elif a==3:
                            design.pattern()
                            add.delete_row()
                        elif a==4:
                            design.pattern()
                            break
                except:
                    design.pattern()
                    print("SORRY!!!! SERVER ERROR PLLS TRY AGAIN LATER")
            else:
                design.pattern()
                print("WORNG!! PASSWORD")
        elif ch==2:
            design.pattern()
            add.add_user()
            try:
                while(True):
                    design.pattern()
                    print("ENTER YOUR CHOICE\n1.TABULAR ANALYSIS \n2.GRAPHICAL ANALYSIS\n3.READ CSV\n4.DEEP ANALYSIS\n5.EXIT")
                    z=int(input())
                    if z==1:
                        design.pattern()
                        search.search_cars_report()
                        print("ENTER YOUR CHOICE\n1.SEARCH BY MODEL \n2.SEARCH MODEL BY YEAR\n3.SEARCH MODEL BY AREA")
                        print("4.SEARCH MODEL BY YEAR AND AREA\n5.EXIT")
                        b=int(input())
                        if b==1:
                            design.pattern()
                            search.search_by_model()
                        elif b==2:
                            design.pattern()
                            search.search_model_by_year()
                        elif b==3:
                            design.pattern()
                            search.search_model_by_area()
                        elif b==4:
                            design.pattern()
                            search.search_model_by_year_and_area()
                        elif b==5:
                            design.pattern()
                            break
                    elif z==2:
                        design.pattern()
                        print("ENTER  YOUR CHOICE \n1.LINE CHART\n2.BAR CHART\n3.HISTOGRAM CHART\n4.PIE CHART\n5.EXIT")
                        f=int(input(""))
                        if f==1:
                            design.pattern()
                            print("ENTER YOUR CHOICE\n1.LINE CHART ON FULL DATASET \n2.LINE CHART ON YEAR 2016\n3.LINE CHART ON YEAR 2017\n4.LINE CHART ON YEAR 2018")
                            print("5.LINE CHART ON YEAR 2019\n6.LINE CHART ON YEAR 2020\n7.EXIT")
                            u=int(input(""))
                            if u==1:
                                design.pattern()
                                line.line_full()
                            elif u==2:
                                design.pattern()
                                line.line_2016()
                            elif u==3:
                                design.pattern()
                                line.line_2017()
                            elif u==4:
                                design.pattern()
                                line.line_2018()
                            elif u==5:
                                design.pattern()
                                line.line_2019()
                            elif u==6:
                                design.pattern()
                                line.line_2020()
                            elif u==7:
                                design.pattern()
                                break
                        elif f==2:
                            design.pattern()
                            print("ENTER YOUR CHOICE\n1.BAR CHART ON MODLE \n2.BAR CHART ON YEAR 2016\n3.BAR CHART ON YEAR 2017\n4.BAR CART ON YEAR 2018")
                            print("5.BAR CHART  ON YEAR 2019\n6.BAR CHART ON YEAR 2020\n7.EXIT")
                            u=int(input(""))
                            if u==1:
                                design.pattern()
                                bar.bar_model()
                            elif u==2:
                                design.pattern()
                                bar.bar_2016()
                            elif u==3:
                                design.pattern()
                                bar.bar_2017()
                            elif u==4:
                                design.pattern()
                                bar.bar_2018()
                            elif u==5:
                                design.pattern()
                                bar.bar_2019()
                            elif u==6:
                                design.pattern()
                                bar.bar_2020()
                            elif u==7:
                                design.pattern()
                                break
                        elif f==3:
                            design.pattern()
                            print("ENTER YOUR CHOICE\n1.HISTOGRAM CHART FULL ANALYSIS\n2.HISTOGRAM CHART ON JANUARY SALES\n3.HISTOGRAM CHART ON FEBRUARY SALES\n4.HISTOGRAM CHART ON MARCH SALES\n5.HISTOGRAM CHART ON APRIL SALES")
                            print("6.HISTOGRAM CHART ON MAY SALES\n7.HISTOGRAM CHART ON JUNE SALES\n8.HISTOGRAM CHART ON JULY SALES\n9.HISTOGRAM CHART ON AUGUST SALES\n10.HISTOGRAM CHART ON SEPTEMBER SALES")
                            print("11.HISTOGRAM CHART ON OCTUBER SALES\n12.HISTOGRAM CHART ON NOVEMBER SALES\n13.HISTOGRAM CHART ON DECEMBER SALES\n14.EXIT")
                            p=int(input(""))
                            if p==1:
                                design.pattern()
                                histogram.hist_full()
                            elif p==2:
                                design.pattern()
                                histogram.hist_january()
                            elif p==3:
                                design.pattern()
                                histogram.hist_february()
                            elif p==4:
                                design.pattern()
                                histogram.hist_march()
                            elif p==5:
                                design.pattern()
                                histogram.hist_april()
                            elif p==6:
                                design.pattern()
                                histogram.hist_may()
                            elif p==7:
                                design.pattern()
                                histogram.hist_june()
                            elif p==8:
                                design.pattern()
                                histogram.hist_july()
                            elif p==9:
                                design.pattern()
                                histogram.hist_august()
                            elif p==10:
                                design.pattern()
                                histogram.hist_september()
                            elif p==11:
                                design.pattern()
                                histogram.hist_octuber()
                            elif p==12:
                                design.pattern()
                                histogram.hist_november()
                            elif p==13:
                                design.pattern()
                                histogram.hist_december()
                            elif p==14:
                                design.pattern()
                                break
                        elif f==4:
                            design.pattern()
                            print("ENTER YOUR CHOICE \n1.PIE CHART ON JANUARY SALES\n2.PIE CHART ON FEBRUARY SALES\n3.PIE CHART ON MARCH SALES\n4.PIE CHART ON APRIL SALES")
                            print("5.PIE CHART ON MAY SALES\n6.PIE CHART ON JUNE SALES\n7.PIE CHART ON JULY SALES\n8.PIE CHART ON AUGUST SALES\n9.PIE CHART ON SEPTEMBER SALES")
                            print("10.PIE CHART ON OCTUBER SALES\n11.PIE CHART ON NOVEMBER SALES\n12.PIE CHART ON DECEMBER SALES\n13.exit")
                            j=int(input(""))
                            if j==1:
                                design.pattern()
                                pie.pie_january()
                            elif j==2:
                                design.pattern()
                                pie.pie_february()
                            elif j==3:
                                design.pattern()
                                pie.pie_march()
                            elif j==4:
                                design.pattern()
                                pie.pie_april()
                            elif j==5:
                                design.pattern()
                                pie.pie_may()
                            elif j==6:
                                design.pattern()
                                pie.pie_june()
                            elif j==7:
                                design.pattern()
                                pie.pie_july()
                            elif j==8:
                                design.pattern()
                                pie.pie_august()
                            elif j==9:
                                design.pattern()
                                pie.pie_september()
                            elif j==10:
                                design.pattern()
                                pie.pie_octuber()
                            elif j==11:
                                design.pattern()
                                pie.pie_november()
                            elif j==12:
                                design.pattern()
                                pie.pie_december()
                            elif j==13:
                                design.pattern()
                                break
                        elif f==5:
                            break
                    elif z==3:
                        design.pattern()
                        search.read_file()
                    elif z==4:
                        while(True):
                            design.pattern()
                            print("ENTER YOUR CHOICE\n1.REPORT SUMMARY\n2.SHOW INDEX\n3.SHOW COLUMNS\n4.SHOW DATATYPES\n5.SHOW VALUES")
                            print("6.SHOW SHAPE\n7.SHOW SIZE\n8.SHOW TRANSPOSE\n9.SHOW N ROES FROM TOP\n10.SHOW N ROWS FROM BOTTEM\n11.SHOW EMPTY\n12.EXIT")
                            x=int(input())
                            if x==1:
                                design.pattern()
                                analysis.report_summary()
                            elif x==2:
                                design.pattern()
                                analysis.search_index() 
                            elif x==3:
                                design.pattern()
                                analysis.search_columns()
                            elif x==4:
                                design.pattern()
                                analysis.search_datatypes()
                            elif x==5:
                                design.pattern()
                                analysis.search_values()
                            elif x==6:
                                design.pattern()
                                analysis.search_shape()
                            elif x==7:
                                design.pattern()
                                analysis.search_size()
                            elif x==8:
                                design.pattern()
                                analysis.search_transpose()
                            elif x==9:
                                design.pattern()
                                analysis.search_head()
                            elif x==10:
                                design.pattern()
                                analysis.search_tail()
                            elif x==11:
                                design.pattern()
                                analysis.search_empty()
                            elif x==12:
                                design.pattern()
                                break
                    elif z==5:
                        design.pattern()
                        break
            except:
                design.pattern()
                print("SORRY!!! SERVER ERROR PLS TRY AGAIN LATER")
        elif ch==3:
            design.pattern()
            print("PLS ENTER PASSWORD TO CONTINUE")
            a=int(input())
            if a==54321:
                design.pattern()
                print("WELCOME BOSS")
                try:
                    while(True):
                        design.pattern()
                        print("ENTER YOUR CHOICE \n1.MANAGER ENTRY LIST\n2.USER ENTRY LIST\n3.ADD COLUMN\n4.DELETE COLUMN\n5.EXIT")
                        a=int(input(""))
                        if a==1:
                            design.pattern()
                            search.search_manager_list()
                        elif a==2:
                            design.pattern()
                            search.search_user_list()
                        elif a==3:
                            design.pattern()
                            column.new_column()
                        elif a==4:
                            design.pattern()
                            column.drop_column()
                        elif a==5:
                            design.pattern()
                            break
                except:
                    design.pattern()
                    print("SORRY!!! SERVER ERROR PLS TRY AGAIN LATER")
            else:
                design.pattern()
                print("WRONG!! PASSWORD")
        elif ch==4:
            design.pattern()
            print("THANK YOU......")
            break
except:
    design.pattern()
    print("SORRY!!! SERVER ERROR PLS TRY AGAIN LATER")
