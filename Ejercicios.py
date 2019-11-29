import re

path = "Prueba.txt"

try:
    archivo = open(path, 'r')
except:
    print ("El Archivo No Se Encuentra En Esta Carpeta")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print (texto)


patron = r"[a-z]+[0-9]{1,8}"
result = re.findall(patron,texto)


print"\n"


patron2 = r"[a-z]"
result2 = re.findall(patron2,texto)

print"\n"

patronDEC = r"([0-9]+\.[0-9]+([eE][+\-]?[0-9]+)?/g"


resultDEC = re.findall(patron,texto)
print"\n"


patronEnT = r"/([0-9]{0,9})/g"
resultEnT = re.findall(patronEnT,texto)

print("\n", resultEnT)
print"\n"


patronOPERARIT = r"(\w+[+|-|*|/])\w+/g"
resultOPERSRTI = re.findall(patronOPERARIT,texto)


print("\n", resultOPERSRTI)
print"\n"


patronOPERREL = r"\w+[!]|[/<>=]\w+/g"
resultOPERREL = re.findall(patronOPERREL,texto)

print("\n", resultOPERREL)
print"\n"


patronPALRES = r"(program|var|const|begin|end|Writeln|if|then|else|end|Mayor|Menor)\b"
resultPALRES = re.findall(patronPALRES,texto)

print("\n", resultPALRES)