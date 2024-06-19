Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import xlrd
>>> empdata={'empid':[1001,1002,1003,1004,1005,1006],
...          'ename':['Ganesh Rao','Anil Kumar','Gaurav Gupta','Hema Chandra','Laxmi Prassana','Anant Nag'],
...          'sal':[10000.00,23000.50,18000.33,16500.50,12000.75,9999.99],
...          'doj':['2000-10-10','2002-03-20','2002-02-03','2000-09-10','2000-10-08','1999-09-09']}
>>> df=pd.DataFrame(empdata)
>>> df
   empid           ename       sal         doj
0   1001      Ganesh Rao  10000.00  2000-10-10
1   1002      Anil Kumar  23000.50  2002-03-20
2   1003    Gaurav Gupta  18000.33  2002-02-03
3   1004    Hema Chandra  16500.50  2000-09-10
4   1005  Laxmi Prassana  12000.75  2000-10-08
5   1006       Anant Nag   9999.99  1999-09-09
