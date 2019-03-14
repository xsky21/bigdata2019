import sqlite3
import pandas as pd
import MySQLdb

con = MySQLdb.connect(host='localhost',port=3306,db='student_info',user='xsky21',passwd='1111',charset='utf8mb4')
c = con.cursor()
#query = """CREATE TABLE student_info
#(student_ID VARCHAR(6),
#Name VARCHAR(10),
#Age int,
#Major VARCHAR(20),
#Practicable_computer_languages VARCHAR(20),
#High_level VARCHAR(10),
#Middle_level VARCHAR(10),
#Low_level VARCHAR(10));"""
#c.execute(query)
#con.commit()#파이썬 결측값

data_frame = pd.read_excel("Student_Info.xlsx",sheet_name = "info1")
row_range = len(data_frame["Student_ID"].array)
data = []
for a in range(row_range):
    data.append(tuple(data_frame.iloc[a, :].fillna("")))
print(data)
statement = """INSERT INTO student_info (student_ID, Name, Age, Major, Practicable_computer_languages, High_level, Middle_level, Low_level)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
c.executemany(statement, data)
con.commit()


