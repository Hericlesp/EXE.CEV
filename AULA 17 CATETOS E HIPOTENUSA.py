#01
co=float(input("qual o valor do cateto oposto? "))
ca=float(input("qual o valor do cateto adjacente? "))
h1=(co**2+ca**2)**(1/2)
print('A hipotenuza vai medir {:.2f}'.format(h1))

#02
import math
o=float(input("qual o valor do cateto oposto? "))
ca=float(input("qual o valor do cateto adjacente? "))
h1=math.hypot(co,ca)
print('A hipotenuza vai medir {:.2f}'.format(h1))