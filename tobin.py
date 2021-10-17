import csv

with open('bin.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in range(36):
        employee_writer.writerow([bin(x)[2:]])