import pandas as pd,xlrd
empdata=[(1001,'Ganesh Rao',10000.00,'2000-10-10'),
         (1002,'Anil Kumar',23000.50,'2002-03-20'),
         (1003,'Gaurav Gupta',18000.33,'2002-02-03'),
         (1004,'Hema Chandra',16500.50,'2000-09-10'),
         (1005,'Laxmi Prassana',12000.75,'2000-10-08'),
         (1006,'Anant Nag',9999.99,'1999-09-09')]
df=pd.DataFrame(empdata,columns=['eno','ename','doj','sal'])
print(df)
