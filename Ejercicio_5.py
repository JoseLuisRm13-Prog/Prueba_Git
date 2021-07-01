from typing import Dict
from Scripts.Funciones.funciones import Multi_Lista

Mi_dic = {"zapatos":"azules","camisa":"rosa","pantalon":"amarillo"}
Mi_dic2 = {1:"uno",3:"tres",2:"dos"}
lon_Mi_dic1 = len(Mi_dic)
lon_Mi_dic2 = len(Mi_dic2)
print("Longitud Dic #1 : ",lon_Mi_dic1)
print("Longitud Dic #2 : ",lon_Mi_dic2)
elem_3 = Mi_dic["camisa"]
elem_2 = Mi_dic2[2]
print("Elemento 3 Dic #1: ", elem_2)
print("Elemento 2 Dic #2: ", elem_3)
keys_1 = Mi_dic.keys()
keys_2 = Mi_dic2.keys()
print("Keys Dic #1: ", keys_1)
print("Keys Dic #2: ", keys_2)
Ordenar = sorted(Mi_dic2.keys())
print("Ordenamos Dic #2: ", Ordenar )
Copia_dic = Mi_dic2.copy()
print("Soy el nuevo diccionario: ", Copia_dic)



