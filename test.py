from assgnopts import *
import pandas

diccionari = {
    0: ("Perse","Kilos"),
    1: ("Pomes","unitats")
}
Les_meves_coses = Assgn(diccionari,conj="com a")
Les_meves_coses.input()
Les_meves_coses.dispValues()
Les_meves_coses.save()