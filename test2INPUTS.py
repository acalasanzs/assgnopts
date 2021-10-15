from typing import Dict
from assgnopts import *
import urllib.request
import pandas as pd
import numpy as np

# Import fruits.csv
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/knadh/xmlutils.py/master/samples/fruits.csv', 
    'fruits.csv')
data = pd.read_csv ("fruits.csv")

# Extract column Apple of fruits
df = pd.DataFrame(data, columns= ['Apple'])

# Convert it to a list
fruits = ['Apple']+df['Apple'].tolist()

# Make 2 objects with kilos and units magnitudes
MyStuff = Assgn(Ar2Dict(fruits,"kilos"),conj="as")
MySecondStuff = Assgn(Ar2Dict(fruits,"units"),conj="as",rules=[False,False,True])

# Set the two object's values via inputs
MyStuff.input()
MySecondStuff.input()
# Display values
MyStuff.dispValues()
print("--------------------------------------")
MySecondStuff.dispValues()

# Convert to a x,y 2D array
x = np.array(MyStuff.array)
y = np.array(MySecondStuff.array)

# Divide both 1D arrays and truncate It and pass to a dictionary
dictionary = Ar2Dict2(Ar2List([truncate(i,3) for i in np.divide(x,y)],"kilos/unit"))

# Print dictionary
print(dictionary)

# Display "fruits: dictionary"
dispDict(fruits,dictionary)