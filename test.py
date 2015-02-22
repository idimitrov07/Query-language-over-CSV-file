import csv
from prettytable import from_csv

fp = open("entries.csv", "r")
pt = from_csv(fp)
fp.close()

f=open("entries.csv")

#build list of all the rows in the csv file
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

#limit method
def limit_method(inn):
    input_arr = split_input(inn)
    num_rows = len(entries_arr)
    if "LIMIT" in input_arr and input_arr.index("LIMIT") < len(input_arr) - 1:
        num_rows = int(input_arr[-1])
    return num_rows

#print limit_method("LIMIT 2", pt)

#select method
def select_columns(inn):
    input_arr = split_input(inn)
    if len(input_arr) == 1:
        return pt
    else:
        fields_arr = []
        for col in input_arr:
            if col in entries_arr[0]:
                fields_arr.append(col)
        #new_pt = pt.get_string(fields=fields_arr)
        num_rows = limit_method(inn)
        return pt.get_string(fields=fields_arr, start=0, end=num_rows)


#print select_columns("SELECT name, hometown LIMIT 4")



#show available columns
def show_columns():
    return ", ".join(entries_arr[0])

#sum integers in given column
def sum_column(col):
    if col in entries_arr[0]:
        col_id = entries_arr[0].index(col)
    else:
        return "No column: '%s'\nAvailable columns are: %s" % (col, show_columns())
    col_sum = 0
    for row in entries_arr:
        if row[col_id].isdigit() == True:
            col_sum = col_sum + int(row[col_id])
    if col_sum == 0:
        return "No integers in column: '%s'" % col
    return col_sum

#print(sum_column('names'))




#print split_input("SELECT   id  ,   LIMIT 1")

# input_command = ""
#
# while True:
#     input_command = raw_input("query>")
#     #print "query>" + input_command
#     if input_command == "SELECT":
#         print pt
#     elif input_command == "SHOW":
#         print show_columns()
#     elif input_command == "exit":
#         break
#     else:
#         print "Not a valid query.."
