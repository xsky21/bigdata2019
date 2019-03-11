# !/usr/bin/env python3
import csv
import MySQLdb
import sys

output_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3308, db='my_suppliers', user='bigdata', passwd='1111')
c = con.cursor()

# Create a file writer object and wrte the header row
filewrite = csv.writer(open(output_file, 'w', newline=''), delimiter = ',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', ' Cost', 'Purchase Date']
filewrite.writerow(header)

# Query the Suppliers table and write the output to a CSV file
c.execute("""SELECT *
            FROM Suppliers
            WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewrite.writerow(row)