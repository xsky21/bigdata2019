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
#con.commit()

data_frame = pd.read_excel("Student_Info.xlsx",sheet_name = "info1")
row_range = len(data_frame["Student_ID"].array)
data = []
for a in range(row_range):
    data.append(tuple(data_frame.iloc[a, :].array))
print(data)
#완전히 포매팅 기법으로, execute로 돌린다.
statement = """INSERT INTO student_info VALUES('%s','%s',%s,'%s','%s','%s','%s',%s');"""
c.execute(statement, data)
c.commit()


