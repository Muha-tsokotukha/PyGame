import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    text = ''.join(f.readlines())

nameOfCompany = re.search(r'ДУБЛИКАТ\n(.+)\n', text).group(1)

BINnumber = re.search(r'БИН \d(.+)\n', text).group(0)

products = re.findall(r'(\d+)\.\n(.+)\n(.+)\n(.+)\n', text)

date = re.search(r'Время: (.+)\n', text).group(1)

adress = re.search(r'\nг. (.+)\n', text).group(1) 

