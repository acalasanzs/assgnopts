from assgn import List2list,color,mess,os,List #Importar la llibreria assgn per a tindre un convertidor de arrays y altres

def opts(cls):
    #Retorna tots els directoris d'una class sense "__", e. g. __name__
    return [method for method in dir(cls) if method.startswith('__') is False] 
def optionsinclass(cls):
    #Indexa totes les dir d'un objecte i les passa per triar una per després retornarla amb getattr com un attr válid. El mateix que la funció de dalt.
    method_list = [method for method in dir(cls) if method.startswith('__') is False]

    #Converteix aquesta lista en colors i amb el index davant
    colored = ["{}{}. {}{}".format(color.b.green,i,color.b.blue,method) for i,method in enumerate(method_list)]
    print("Options in {}: {}{}".format(cls.__name__,List2list(colored,", "),color.end))

    #Si no hi ha res
    if len(method_list) < 1: mess.Empty()

    #Pregunta fins que doni un int
    while True:
        try:
            res = int(input("Index? "))
        except:
            print(mess.err)
            continue
        break
    #Mentres no sigui en el range de indexs de method_list
    while not(res in range(len(method_list))):
        try:
            if res == -1:
                return getattr(cls,method_list[-1])
            else:
                print(mess.err)
                res = int(input("Index? "))
        except:
            continue
    #retorna el dir triat
    return getattr(cls,method_list[res])



def classMehtod(cls):
    #Imprimex el nom del dir abans triat, i l'executa
    a = ": "
    if cls.__doc__ != None: a += cls.__doc__
    print(color.b.blue,cls.__name__,a,color.end)
    optionsinclass(cls)()
def options(cls,num=1,loop=True):
    #Per a un nombre de vegades, interroga el directori d'una class
    repeat = True
    while repeat:
        #"res" es el current de la class trobada
        res = cls
        for x in range(num):
            #si es l'ultim del range
            if x == range(num)[-1]:
                #si te dir(s)
                if opts(res):
                    return classMehtod(res)
            else:
                #indexa cada cop a sí mateix
                res = optionsinclass(res)
        #pausa
        os.system("pause")
        #Pregunta si tornar-hi un altre vegada
        if loop:
            repeat =  False if input("Repeat?(Anything,n)") == "n" else True
        else:
            repeat = False
def optionsAll(cls,loop=True):
    #Fins que no hi hagi res interroga el directori d'una class
    repeat = True
    while repeat:
        res = cls
        while True:
            #Si hi ha
            if opts(res):
                #Indexa cada vegada a sí mateix
                res = optionsinclass(res)
            #Si no hi ha, prova d'executar
            else:
                res()
                break
        #Pregunta si tornar-hi un altre vegada
        os.system("pause")
        if loop:
            repeat =  False if input("Repeat?(Anything,n)") == "n" else True
        else:
            repeat = False
if __name__ == "__main__":
    class demo:
        class five:
            class four:
                class three:
                    class two:
                        class one:
                            def zero():
                                def less():
                                    print("less")
                                print("zero")
    optionsAll(demo,True)