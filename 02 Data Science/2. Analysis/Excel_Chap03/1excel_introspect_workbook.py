# xlrd 모듈 설치
# py -m pip install xlrd
import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print("Number of worksheets: ", workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name: ", worksheet.name, "\tRows: ", worksheet.nrows, "\tColumns: ", worksheet.ncols)


# 실행인자
# sales_2013.xlsx
#
# sales_2013.xlsx output_files/2e_output.xls
#
# sales_2013.xlsx output_files/3e_output.xls
# sales_2013.xlsx output_files/3p_output.xls
#
# sales_2013.xlsx output_files/4e_output.xls
# sales_2013.xlsx output_files/4p_output.xls
#
# sales_2013.xlsx output_files/5e_output.xls
# sales_2013.xlsx output_files/5p_output.xls
#
# sales_2013.xlsx output_files/6e_output.xls
# sales_2013.xlsx output_files/6p_output.xls
#
# sales_2013.xlsx output_files/7e_output.xls
# sales_2013.xlsx output_files/7p_output.xls
#
# sales_2013.xlsx output_files/8e_output.xls
# sales_2013.xlsx output_files/8p_output.xls
#
# sales_2013.xlsx output_files/9e_output.xls
# sales_2013.xlsx output_files/9p_output.xls
#
# sales_2013.xlsx output_files/10e_output.xls
# sales_2013.xlsx output_files/10p_output.xls
#
# sales_2013.xlsx output_files/11e_output.xls
# sales_2013.xlsx output_files/11p_output.xls
#
# 12번째 실행인자
# .
#
# 13번째 실행인자
# . output_files/13e_output.xls
# . output_files/13p_output.xls
#
# 14번째 실행인자
# . output_files/14e_output.xls
# . output_files/14p_output.xls
