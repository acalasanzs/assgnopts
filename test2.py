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
Kilos = Assgn(Ar2Dict(fruits,"kilos"),conj="as")
Units = Assgn(Ar2Dict(fruits,"units"),conj="as")

# Set the two object's values (random answers)
Kilos.array = [random.choice(list(range(1,1000))) for x in range(len(fruits))]
Units.array = [random.choice(list(range(1,100))) for x in range(len(fruits))]

# Display values
Kilos.dispValues()
print("--------------------------------------")
Units.dispValues()

# Convert to a x,y 2D array
x = np.array(Kilos.array)
y = np.array(Units.array)

# Divide both 1D arrays and truncate It and pass to a dictionary
results = np.array([truncate(i,3) for i in np.divide(x,y)])
dictionary = Ar2Dict2(Ar2List(results,"kilos/unit"))

# Print dictionary
print(dictionary)

# Display "fruits: dictionary"
dispDict(fruits,dictionary)

# Combine both 1-dimensional arrays
""" xy = np.array([x,y])
test = results.reshape(len(fruits),1)
print(test) """
