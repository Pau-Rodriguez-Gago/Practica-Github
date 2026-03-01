x=float(input(""))
import math
if x-math.floor(x)<math.ceil(x)-x:
    print(math.floor(x),math.ceil(x),math.floor(x))
elif x-math.floor(x)>math.ceil(x)-x:
    print(math.floor(x),math.ceil(x),math.ceil(x))
else:
    print(math.floor(x),math.ceil(x),math.ceil(x))
#Vaya un ejercicio, aquí también tuve que buscar en internet, pues sin conocer el math.floor y el math.ceil,
#es prácticamnente imposible de hacer. Pero bueno, una vez los usas, es bien facil.