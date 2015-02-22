import csv
from prettytable import from_csv
from prettytable import PrettyTable

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
    for delim in ', "\'':
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

#find string in table method
def find_string(param):
    param = str(param)
    find_table = PrettyTable(entries_arr[0])
    x = 1
    while x < len(entries_arr):
        for cell in entries_arr[x]:
            if param in cell:
                find_table.add_row(entries_arr[x])
                break
        x = x + 1
    return find_table

#print find_string("a")


input_command = ""

while True:
    input_command = raw_input("query>")
    input_method = split_input(input_command)[0]
    if len(split_input(input_command)) > 1:
        second_param = split_input(input_command)[1]
    if input_method == "SELECT":
        print select_columns(input_command)
    elif input_method == "SHOW":
        print show_columns()
    elif input_method == "SUM":
        print sum_column(second_param)
    elif input_method == "FIND":
        print find_string(second_param)
    elif input_command == "exit":
        break
    else:
        print "Not a valid query.."
