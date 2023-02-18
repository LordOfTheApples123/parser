from Parser import Parser

parser = Parser('3*(1+3*4)*(1+3+4)/(2+3+5)+2/5+4')
res = parser.start()
print(str(res))
number = 3*(1+3*4)*(1+3+4)/(2+3+5)+2/5+4
print(str(number))
