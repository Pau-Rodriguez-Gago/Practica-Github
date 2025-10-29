import turtle

def dibujar():
    # Configuración de la ventana
    pantalla = turtle.Screen()
    pantalla.title("Dibujo con Turtle en Python")
    pantalla.bgcolor("lightblue")

    # Crear la tortuga
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("darkgreen")
    t.pensize(3)
    t.speed(3)  # Velocidad de dibujo (1-10)

    # Dibujar un cuadrado
    for _ in range(4):
        t.forward(100)  # Avanza 100 píxeles
        t.right(90)     # Gira 90 grados a la derecha

    # Mover sin dibujar
    t.penup()
    t.goto(150, 0)
    t.pendown()

    # Dibujar un círculo
    t.color("red")
    t.circle(50)  # Radio de 50 píxeles

    # Esperar a que el usuario cierre la ventana
    pantalla.mainloop()

if __name__ == "__main__":
    try:
        dibujar()
    except turtle.Terminator:
        print("Ventana cerrada por el usuario.")