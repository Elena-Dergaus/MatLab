



equation = 'y = -12x + 11111140.2121'
x = 2.5
k=int(equation[equation.find('=')+2:equation.find('x')])
b=float(equation[equation.find('+')+2:])
print('k=',k, type(k),'','b=', b,type(b))
y=k*x+b
print('y= ',y)
