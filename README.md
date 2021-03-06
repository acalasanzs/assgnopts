# Assgnopts, the best input class

# Overview
The Assgnopts is a module to create inputs via dicts and arrays with several input check parameters


## Usage
First create an dictionary
```Python
dic = {
    0: ("Apples","kilos"),
    1: ("Oranges","units")
}
```
or use my built-in functions (or use a range)
```Python
dict = Ar2Dict(IterAr(2,"Object"),"units")
{
    0: ("Object 1","units"),
    1: ("Object 2","units")
}
```
or
```Python
dict = Ar2Dict(["Apples","Oranges"],"units")
{
    0: ("Apples","units"),
    1: ("Oranges","units")
}
```
Then put it with all type of cutomizations and parameters:
```Python
MyObject = Assgn(dict,conj="as",vals=range(1,10))
```
you can als print the object's values/inputs from the user:
```Python
MyObject.dispValues()
```
or get values via 
```Python 
MyObject.getValues()
```

Here's an example of collectin apples, oranges and weirdos:
```Python
def main():
    MyObject = Assgn(Ar2Dict(["Apples","Oranges","Weirdos"],"kilos")) #Creating the object __init__
    MyObject.input() #Collecting inputs from user/terminal
    MyObject.dispValues()
```
###  CSV
Following the object we maked above, we can export the answers into a csv file, here's how:
```Python
MyObject = Assgn(Ar2Dict(["Apples","Oranges","Weirdos"],"kilos")) #Creating the object __init__
MyObject.input() #Collecting inputs from user/terminal
MyObject.save() #It will save the csv as: MyObject.assgnopts.csv
```
Then we can load It
```Python
MyObjectLoaded = Assgn() #Creating the object __init__
MyObjectLoaded.loadcsv("MyObject.assgnopts.csv") #It will save the csv as: MyObject.assgnopts.csv
```
One time we loaded It, we can re-ask the questions loaded:
```Python
MyObjectLoaded.input()
```

Here's an example of the entire code:
```Python
MyObject = Assgn(Ar2Dict(["Apples","Oranges","Weirdos"],"kilos")) #Creating the object __init__
MyObject.input() #Collecting inputs from user/terminal

#-------------------------------------------------------------

MyObjectLoaded = Assgn() #Creating the object __init__ of the second object
MyObjectLoaded.loadcsv(MyObject.save()) #The .save() method returns the filename
MyObjectLoaded.input() #Re-ask the questions
```
###  Getting it

To download assgnopts, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install assgnopts
```

### Using it

Assgnopts was programmed with ease-of-use in mind. First, import *

```Python
from assgnopts import *
```

And you're ready to go!

License
----

MIT License

Copyright (c) 2021 Albert Calasanz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Follow me: [Github](https://github.com/acalasanzs)!
