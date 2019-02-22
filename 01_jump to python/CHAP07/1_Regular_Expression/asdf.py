import re

file_name_list = ["foo.bar", "autoexe.bat","sendmail.cf"]
p = re.compile(".*[.](?!bat$ )")
for file_name in file_name_list:
    print(p.search(file_name))