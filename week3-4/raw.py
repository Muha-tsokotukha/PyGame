import re

file = open('raw.data', 'r')
txt = file.read()
Adresspattern = r"\nАдрес.*"
letsfind = re.search(Adresspattern,txt)
print(letsfind)
file.close()