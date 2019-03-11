import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
        (customer VARCHAR(20),
        product VARCHAR(40),
        amount FLOAT,
        date DATE);"""
con.execute(query)
con.commit()
# 휘발성

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 678.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print("Number of rows: {}" .format(row_counter))


# 2db_insert_rows 실행인자: supplier_data.csv
# 3db_update_rows 실행인자: data_for_updating.csv
# 4th => 첫번째 실행인자: supplier_data.csv
# 5th => 첫번째 실행인자: output_files/5output.csv
# 6th => 첫번째 실행인자: data_for_updating_mysql.csv