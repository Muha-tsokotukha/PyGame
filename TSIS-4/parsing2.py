import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    text = ''.join(f.readlines())

nameOfCompany = re.search(r'ДУБЛИКАТ\n(.+)\n', text).group(1)
print("Name of the company: \n", nameOfCompany,sep=" ")
BINnumber = re.search(r'БИН \d(.+)\n', text).group(0)
print("BIN number:", BINnumber)
products = re.findall(r'(\d+)\.\n(.+)\n([0-9, ]+) x ([0-9, ]+)\n', text)
itr = 1
def numberfyCost(x):
    x = x.replace(',', '.')
    x = x.replace(' ', '')
    return float(x)
def numberfyCount(x):
    x = x.replace(',', '')
    x = x.replace(' ', '')
    return int(x)
for product in products:
    print(itr, end='.\n')
    print(' 1) ', product[1])
    print(' 2) ', product[2])
    print(' 3) ', product[3])
    cost = numberfyCount(product[2]) * numberfyCost(product[3])
    print(' 4) ', cost)

    itr += 1
date = re.search(r'Время: (.+)\n', text).group(1)
print('Date:', date)
adress = re.search(r'\nг. (.+)\n', text).group(1)
print('Address:', adress) 

