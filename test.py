import csv
from prettytable import from_csv

fp = open("entries.csv", "r")
pt = from_csv(fp)
fp.close()
# f=open("entries.csv")
# for row in csv.reader(f):
#     print(row[0])

print pt
