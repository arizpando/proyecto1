import math
print ('Hallar area y perimetro de un rectangulo')
base = float(input('Base= '))
altura= float(input('Altura= '))
area= base*altura
perimetro= 2*(base+altura)
diagonal= math.sqrt(base**2+altura**2)
print('Area= ',area)
print('diagonal=', round(diagonal, 3))

