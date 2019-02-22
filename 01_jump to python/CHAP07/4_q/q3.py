import re
number_list = "\npark 010-9999-9988\nkim 010-9909-7789\nlee 010-8789-7768\n"
m = re.sub("[-][\d]{4}\s","****",number_list)
print(m)


