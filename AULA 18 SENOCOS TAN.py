import math
angulo=float(input("qual o valor do cateto oposto? "))
#ca=float(input("qual o valor do cateto adjacente? "))
seno=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tan=math.tan(math.radians(angulo))
print('O seno do angulo {} é : {:.2f}'.format(angulo,seno))
print('O seno do angulo {} é : {:.2f}'.format(angulo,cos))
print('O seno do angulo {} é : {:.2f}'.format(angulo,tan))