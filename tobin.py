import csv
import string

alfanum = [x for x in string.ascii_uppercase]+[x for x in range(10)]

with open('bin.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Char', 'Bin 2^6'])
    for x in range(36):
        result = bin(x)[2:]
        while len(result) < 6:
            result = '0'+result
        employee_writer.writerow([alfanum[x],result])