from assgnopts import *
import pandas

data = Assgn(range(2),name="olakase")
data.input()
print(pandas.read_csv(data.save()))