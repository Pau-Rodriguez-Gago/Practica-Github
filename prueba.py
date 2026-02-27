import time
import sys
def escribir_lento(texto, retraso=0.05):
    for x in texto:
        sys.stdout.write(x)
        sys.stdout.flush()          
        time.sleep(retraso)
escribir_lento("Bienvenido a la nueva edición de AHORCADO", retraso=0.1)