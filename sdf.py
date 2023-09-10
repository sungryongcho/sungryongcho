import re

str1 = "In the year 2021, the company achieved a revenue growth of 15%, reaching a total of $1.5 million. This increase in revenue was attributed to the success of their new product launch, which saw a 25% increase in customer adoption. Over the course of the year, the company hired 50 new employees, bringing the total workforce to 300. Additionally, they expanded their market presence to cover 10 new countries, resulting in a significant global impact."
eleven = re.findall('\bs\w*s\b', str1, re.I)
print("11",eleven)
seven = re.findall('s\ws\b', str1, re.I)
print("7", seven)
years = re.findall('suc+', str1, re.I)

two = re.findall('\w*\d+\.?\d+\w*', str1, re.I)
three = re.findall('\wa\w*', str1, re.I)
four = re.findall('\ba\w*', str1, re.I)
five = re.findall('\wed\w', str1, re.I)
six = re.findall('\bed\w*', str1, re.I)

eight = re.findall('a\w*', str1, re.I)
nine = re.findall('\b\d+\.?\d+\w', str1, re.I)
ten = re.findall('\w*ed\w*', str1, re.I)

tweleve = re.findall('\w\d+\.?\d+\w', str1, re.I)

print("Years:", years)
print("2",two)
print("3",three)
print("4",four)
print("5",five)
print("6",six)

print("8",eight)
print("9",nine)
print("10",ten)

print("12",tweleve)