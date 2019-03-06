#목적 : csv 파일 읽고 쓰기
import sys
input_file = sys.argv[1] # supplier_data.csv
output_file = sys.argv[2] #output_files/1output.csv

with open(input_file,'r') as filereader:
    print(filereader)
    with open(output_file, 'w') as filewriter:
        header = filereader.readline() #헤더행
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(header_list)+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(row_list)+'\n')