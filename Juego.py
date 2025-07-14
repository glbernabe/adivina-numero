import random

def jugar():
    while True:
        numero_secreto = random.randint(1, 50)
        intentos = 0
        vidas = 7
        print("Esto es un juego de adivinar el número entre el 1 y el 50, tienes 7 vidas")

        while vidas > 0:
            try:
                numelegido = int(input("Elige un número: "))
                intentos += 1
                vidas -= 1
                diferencia = abs(numelegido - numero_secreto)

                if numelegido == numero_secreto:
                    print(f"Has adivinado el número: {numero_secreto}")
                    print(f"Con {intentos} intentos")
                    print(f"Y con {vidas} vidas restantes")
                    break
                elif diferencia <= 1:
                    print("Estás a un número de adivinarlo")
                elif diferencia <= 5:
                    print("Estás cerca")
                elif numelegido < numero_secreto:
                    print("Muy bajo")
                else:
                    print("Muy alto")
            except ValueError:
                print("Eso no es un número válido.")

        if vidas == 0:
            print(f"Te has quedado sin vidas. El número era {numero_secreto}")

        otra = input("¿Quieres jugar otra vez? ").lower()
        if otra not in ["si", "sí", "s"]:
            print("Gracias por jugar.")
            break

jugar()
