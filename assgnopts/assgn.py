"""
Assgnopts Assgn 2.0.0 CSV

Made with love by Albert Calasanz Sallen
TODO:
Load CSV
"""
import os
import csv
import string
import random, pandas
os.system("")
def List(list,load):                                     #Converteix un array en un string
    "Converts array to string"
    value = [x[1] for x in Dic2List(load)]
    temp = color.b.blue
    for i,j in enumerate(list):
        y = " "+color.end
        if i < len(load)-1:
            y = " & "
        temp += str(j) +" "+ str(value[i][1]) + y
    return temp
def Dic2List(dict):                                 #Aquesta funció converteix un dictionary en una array personalitzada
    "Dictionary to array"
    dictlist = []
    for key, value in dict.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist
def namestr(obj, namespace):
    "returns name string from object"
    return [name for name in namespace if namespace[name] is obj]
def List2list(list,co = " + "):
    "Converts array to string"
    temp = ""
    for i,item in enumerate(list):
        if(i>=len(list)-1):
            co = ""
        temp += str(list[i])+co
    return temp
def Ar2Dict(ar,ma = None):
    "Converts array to dict with key:*value"
    if ma is not None:
        r = []
        for x in ar:
            r.append((x,ma))
        dic = dict((key,r[key]) for key in range(len(ar)))
        return dic
    else:
        r = []
        for x in ar:
            r.append((x,x))
        dic = dict((key,r[key]) for key in range(len(ar)))
        return dic
def List2Dict(ar):
    "Converts list to dict"
    r = []
    for x in ar:
        r.append((x,x))
    dic = dict((key,r[key]) for key in range(len(ar)))
    return dic
def IterAr(iter,word):
    "Enumerates words"
    list = []
    for x in range(iter):
        list.append(word+" "+str(x+1))
    return list
def Ar4Ar2Dic(ar1:list,ar2:list):
    "Converts 2 arrays to dict with *key:*value"
    t = []
    for idx,i in enumerate(ar1):
        t.append((i,ar2[idx]))
    return dict((key[0],key[1]) for key in t)
def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class color:
    class t:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        end = "\033[0;m"
    class b:
        red = "\u001b[41m"
        green = "\u001b[42m"
        yellow = "\u001b[43m"
        blue = "\u001b[44m"
        purple = "\u001b[45m"
    end = "\033[0;m"
class mess:
    err = "{}No has introduït un nombre vàlid{}".format(color.b.red,color.end)
    def Valerr():
        print("{}An error ocurred when NaN/Invalid entry was given{}".format(color.b.red,color.end))                    #Els valors d'abans no eren números
        quit()
    def DictErr():
        print("{}An error ocurred when checking if dict{}".format(color.b.red,color.end))         
        quit()
    def Dict2ListErr():
        print("{}An error ocurred in Dic2List{}".format(color.b.red,color.end))
        quit()
    def InvalidOpt():
        print("{}Srry sir, there ins't that option{}".format(color.b.red,color.end))
        quit()
    def optionAsks():
        print("{}Dict not found{}".format(color.b.red,color.end))
        quit()
    def Empty():
        print("{}It's empty!!!!{}".format(color.b.red,color.end))
        quit()
    def InvalidInput():
        print("{}Invalid argument!!!!{}".format(color.b.red,color.end))
        quit()
class Assgn():
    """Makes n inputs and stores them into object list. Rules [A0,A-,OInt] or 'str'
        load:dict, rang:range, rules:boolarray, vals:(tuple,range) arrange
        
        Object:
        self.array returns inputs
        64 Bits: 9223372036854775807 max, 32 Bits: 2147483647 max
        """
    def __init__(self,load=None,rang=None,rules=None,conj="",vals=None,ui= True,no=True,name=None):
        self.AllowNegative = False
        self.Allow0 = False
        self.AllowStr = False
        self.OnlyInt = False
        self.name = name
        self.vals = False
        self.value = []
        self.title = ui
        self.no = no
        self.ln = None
        self.ans = None
        self.rules = rules
        if type(vals) in (tuple,range,list):
            self.vals = vals
        elif vals is not None:
            mess.InvalidInput()
     # Comprovar les rules
        self.conj = "" if type(conj) is not str else conj
        if type(load) is list:
            dic = dict.fromkeys(range(len(load)),"")
            for x in dic:
                dic[x] = load[x]
            load = dic
        elif type(load) is range:
            self.ln = True
        if rules is None:
            pass
        elif (type(rules) is list) and (len(rules) == 3):
            if all(i in(True,False) for i in rules):
                self.Allow0 = rules[0]
                self.AllowNegative = rules[1]
                self.OnlyInt = rules[2]
            else:
                print("Error on rules")
                mess.Valerr()
        if self.OnlyInt and not self.Allow0 and not self.AllowNegative:
            self.rules = None
        elif rules == "str":
            self.AllowStr = True
        else:
            pass
            #print(color.b.red+"Error in rules input\nAll will become false"+color.end)
        # Comprovar les rules
        self.ln = False if self.ln == None else True
        if load is None: self.ln = True
        if not(type(load) is dict) and not(self.ln):                                 #Verificar si load is dict
            print("Line 121")
            mess.DictErr()
        else:
            self.load = load
            if type(load) is dict:
                for j in list(self.load):
                    if not(type(self.load[j]) in (tuple,list)):
                        self.load[j] = (self.load[j],"")
                #print(self.load)
        #---------------------------------------------------------------------------------------
        if isinstance(rang,range):
            if not(len([x for x in rang]) > 0):
                mess.Valerr()
            else:
                self.rang = rang
            if self.ln:
                self.array = ["" for x in self.rang] if self.AllowStr else [0 for x in self.rang]
        elif rang is None:
            try:
                assert len(load)>0
            except:
                mess.Valerr()
            self.rang = range(len(load))
            self.array = [0 for x in self.rang]
        else:
            mess.Valerr()
        # self.input()
    def input(self):
        self.name = [objname for objname, oid in globals().items() if id(oid)==id(self)][0] if self.name is None else self.name
        # HEADER
        if self.title:
            print(color.t.OKGREEN+"Set of {} questions".format(len(self.array))+color.end)
        for i in self.rang:
            if i < 0:
                mess.Valerr()
            def whilefunct(vals):
                while True:
                    try:
                        global ans
                        magn = ":" 
                        a = "value "+str(i+1)
                        b = ""
                        self.value = [x+1 for x in self.rang]
                        if self.no:
                            self.no = str(i+1) + ". "
                        else:
                            self.no = ""
                        if not(self.ln):
                            self.value = [x[1] for x in Dic2List(self.load)]
                            b = self.value[i][1]
                            a = self.value[i][0]
                        if len(self.conj) > 0 and len(b) > 0: magn = " "+self.conj+" "+str(b)+" : "
                        if self.AllowStr:
                            ans = str(input(self.no+"Enter "+str(a)+magn))
                            self.array[i] = ans
                            result = self.array
                            if not(self.ln):
                                result = List(self.array,self.load)
                            print(result)
                        else:
                            if self.OnlyInt:
                                ans = int(input(self.no+"Enter "+str(a)+magn))
                            else:
                                ans = float(input(self.no+"Enter "+str(a)+magn)) #He convertit el dictionary loaded en un array de tuples: value[i+offset] i+ofsset és l'index del array de tuples => [0] o [1] és per establir si el primer valor del tuple o el segon.
                            try:
                                if (ans < 0 and not(self.AllowNegative)) or (ans == 0 and not(self.Allow0)) or (ans not in self.vals):
                                    print(mess.err)
                            except:
                                if (ans < 0 and not(self.AllowNegative)) or (ans == 0 and not(self.Allow0)):
                                    print(mess.err)
                                else:
                                    self.array[i] = ans
                                    # print(self.array)
                                    if not(len(self.array) > 50):
                                        result = self.array
                                        if not(self.ln):
                                            result = List(self.array,self.load)
                                        else:
                                            result = color.b.red+List2list(result,", ")+" "+color.end
                                    else:
                                        result = color.b.red+"Too many questions"+color.end
                                    print(result)
                    except ValueError:
                        print(mess.err)
                        continue
                    break
                self.ans = ans
            if self.rules is None:
                self.ans = -1
                while True:
                    whilefunct(self.vals)
                    if self.vals:
                        if not(self.ans <= 0) and (self.ans in self.vals):
                            break
                        else:
                            print(mess.err)
                    else:
                        if not(self.ans <= 0):
                            break
            else:
                if self.AllowStr:
                    self.ans = ""
                    while True:
                        whilefunct(self.vals)
                        if self.vals:
                            if len(self.ans)>0 and (self.ans in self.vals):
                                break
                            else:
                                print(mess.err)
                        else:
                            if len(self.ans)>0:
                                break
                else:
                    if self.AllowNegative and self.Allow0:
                        while True:
                            whilefunct(self.vals)
                            if self.vals:
                                if not(self.ans <= 0) and (self.ans in self.vals):
                                    break
                                else:
                                    print(mess.err)
                            else:
                                break
                    elif self.AllowNegative and not(self.Allow0):
                        self.ans = 0
                        while True:
                            whilefunct(self.vals)
                            if self.vals:
                                if not(self.ans == 0) and (self.ans in self.vals):
                                    break
                                else:
                                    print(mess.err)
                            else:
                                break
                    elif not(self.AllowNegative) and self.Allow0:
                        self.ans = -1
                        while True:
                            whilefunct(self.vals)
                            if self.vals:
                                if not(self.ans < 0) and (self.ans in self.vals):
                                    break
                                else:
                                    print(mess.err)
                            else:
                                break
    def dispValues(self):
        for i,j in enumerate(self.array):
            if not(self.ln):
                self.value = [x[1] for x in Dic2List(self.load)]
                b = self.value[i][1]
                a = self.value[i][0]
                print(a+":",j,b)
            else:
                print("Value",i,"=",j,";","Type: {}".format(type(j).__name__))
    def getValues(self):
        values = {}
        for i,j in enumerate(self.array):
            if not(self.ln):
                self.value = [x[1] for x in Dic2List(self.load)]
                b = self.value[i][1]
                a = self.value[i][0]
                values[a] = (j,b)
            else:
                values[i] = j
        return values
    def clear(self):
        self.array = [0 for x in self.rang]
    def save(self,filename=None,rndm=False):
        self.value = [x[1] for x in Dic2List(self.load)]
        it = self.name
        if not filename:
            if rndm:
                filename = id_generator() + "-" + it +".assgnopts"+ ".csv"
            else:
                filename = it +".assgnopts"+ ".csv"
                #
        with open(filename, mode='w',newline='') as csv_file:
            fieldnames = ["DATA"]+[i[0] for i in self.value]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            b = [x[0] for x in Dic2List(self.load)]
            dic = Ar4Ar2Dic(fieldnames,[it]+[(b[idx],self.value[idx][1]) for idx,i in enumerate(b)])
            writer.writeheader()
            writer.writerow(dic)
        return filename
    def loadcsv(self,file:str):
        self.value = [x[1] for x in Dic2List(self.load)]
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    row.pop("DATA",None)
                    array = [row[key] for key in row]
                    self.array = []
                    dic = {}
                    for idx,x in enumerate(array):
                        if x.replace("(","").replace(")","").split(", ")[0].isnumeric():
                            self.array.insert(idx,eval(x.replace("(","").replace(")","").split(", ")[0]))
                        else:
                            self.array.insert(idx,x.replace("(","").replace(")","").split(", ")[0])
                        x = eval(x)
                        dic[idx] = x
                    self.load = dic
                    line_count += 1
                line_count += 1
    def __str__(self):
        conj = self.conj
        if conj == "": conj = "<None>"
        return color.t.OKCYAN+"Rules\nA0{},A-{},AStr{},OnlInt{}".format(self.Allow0,self.AllowNegative,self.AllowStr,self.OnlyInt)+"\n"+color.end+"\nconj: {},\nrang: {},\n\nquestions: {},\n\nInputs: {}".format(conj,self.rang,self.value,self.array)
 #myobject = Assgn({0: ["jA","metres"],1:"d",2:"aa",3:"ff"},None,[False,True,True],"en")

if __name__ == "__main__":
    dic = {
        0: ("Peres","kilos"),
        1: ("Pomes","unitats")
    }
    #ElMeuObjecte = Assgn(dic)
    #print(ElMeuObjecte)
    """ MyObject = Assgn(Ar2Dict(IterAr(1,"Object"),"units"),conj="as",vals=range(1,10))
    MySecondObject = Assgn(dic)
    print("________________________________________")
    MyObject.dispValues()
    print("____________________")
    MySecondObject.dispValues() """
    """ MySecondObject = Assgn(dic)
    MyThirdObject =  Assgn(Ar2Dict(IterAr(3,"apples"), "units"),conj="as")
    MyThirdObject.input()
    print(MyThirdObject.getValues())
    MyThirdObject.dispValues() """
    data = Assgn(Ar2Dict(IterAr(5,"label"),"ACU(s)"),name="data")
    datafile = data.save()
    print(pandas.read_csv(datafile,header=0,index_col='DATA'),end="\n\n")
    data.loadcsv(datafile)