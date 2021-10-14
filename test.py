from assgnopts import *
import urllib.request
import pandas as pd
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/knadh/xmlutils.py/master/samples/fruits.csv', 
    'fruits.csv')

data = pd.read_csv ("fruits.csv")   
df = pd.DataFrame(data, columns= ['Apple'])
fruits = ['Apple']+df['Apple'].tolist()
MyStuff = Assgn(Ar2Dict(fruits,"kilos"),conj="as")
MySecondStuff = Assgn(Ar2Dict(fruits,"units"),conj="as")
MyStuff.input()
MySecondStuff.input()