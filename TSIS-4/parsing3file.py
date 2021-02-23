import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    text = ''.join(f.readlines())

nameOfCompany = re.search(r'ДУБЛИКАТ\n(.+)\n', text).group(1)
#print("Name of the company: \n", nameOfCompany,sep=" ")

BINnumber = re.search(r'БИН \d(.+)\n', text).group(0)
#print("BIN number:", BINnumber)

products = re.findall(r'(\d+)\.\n(.+)\n([0-9, ]+) x ([0-9, ]+)\n', text)
x = 1
def numberfyCost(x):
    x = x.replace(',', '.')
    x = x.replace(' ', '')
    return float(x)
def numberfyCount(x):
    x = x.replace(',', '')
    x = x.replace(' ', '')
    return int(x)
'''for product in products:
    print(itr, end='.\n')
    print(' 1) ', product[1])
    print(' 2) ', product[2])
    print(' 3) ', product[3])
    cost = numberfyCount(product[2]) * numberfyCost(product[3])
    print(' 4) ', cost)

    itr += 1
'''
date = re.search(r'Время: (.+)\n', text).group(1)
#print('Date:', date)
adress = re.search(r'\nг. (.+)\n', text).group(1)
#print('Address:', adress) 

with open('outputraw.txt', 'w', encoding='utf-8') as d:
    d.write("Name of the company:\n")
    d.write(nameOfCompany)
    d.write("\nBIN number: ")
    d.write(BINnumber)
    for product in products:
        d.write('\n')
        itr = str(x)
        d.write(itr)
        d.write('\n 1) ')
        d.write(product[1])
        d.write('\n 2) ')
        d.write(product[2])
        d.write('\n 3) ')
        d.write(product[3])
        cost = str(numberfyCount(product[2]) * numberfyCost(product[3]))
        d.write('\n 4) ')
        d.write(cost)
        x += 1
    d.write('\nDate: ')
    d.write(date)
    d.write('\nAddress: ')
    d.write(adress)
