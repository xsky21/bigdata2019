fp = open("spss.txt",'r')
fp_save = open("coding.csv",'w')
for a in fp:
    a = a[3:]
    row = ",".join(a)
    fp_save.write(row+"\n")
fp.close()
fp_save.close()
