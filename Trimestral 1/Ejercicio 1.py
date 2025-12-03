var_min=0
var_max=0
var_intervalo=0
#Inicializo las variables que voy a usar dándoles un valor numérico, en este caso: 0
concatenar=""
#Esta variable es crucial para el ejercicio pues permitirá al programa mostrar
#los resultados en una sola línea de texto. Por eso, la inicializo con ""
#para definirla como una variable de texto.
var_min=int(input("Introduce un inicio: "))
var_max=int(input("Introduce un final: "))
var_intervalo=int(input("Introduce un intervalo: "))
for x in range(var_min,var_max+1,var_intervalo):
    #Aquí uso el var_min como inicio del rango, el var_max como fin,
    #Y el var_intervalo como el intérvalo que va a ir saltando de números.
    #También, le sumo uno a var_max para que se muestre el número final.
    concatenar=concatenar+str(x)+","
    #Aquí sumo la x en forma de string pues así se une a concatenar, y
    #añado una coma textual para que sea una lista
print(concatenar[:-1])
#Y, por último es muy importante poner [:-1] ya que así no se muestra la última coma.
