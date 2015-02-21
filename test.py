import csv
from prettytable import from_csv

fp = open("entries.csv", "r")
pt = from_csv(fp)
fp.close()

f=open("entries.csv")
entries_arr = []
for row in csv.reader(f):
    entries_arr.append(row)
f.close()

#print pt.get_string(fields=["id"])
#print pt[0]

#split input string
def split_input(inn):
    for delim in ', ':
        inn = inn.replace(delim, ' ')
    return inn.split()


print split_input("SELECT   id  ,   LIMIT 1")

# input_command = ""
#
# while True:
#     input_command = raw_input("query>")
#     #print "query>" + input_command
#     if input_command == "SELECT":
#         print pt
#     elif input_command == "SHOW":
#         print ", ".join(entries_arr[0])
#     elif input_command == "exit":
#         break
#     else:
#         print "Not a valid query.."
