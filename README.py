# proyectopert2
El proyecto consiste en implementar un juego de recorrer laberintos, estará basado enteramente en la terminal y trabajaremos con caracteres ASCII.
import readchar

def main():
    print("Presiona las teclas del teclado. Para salir, presiona la tecla ↑ (flecha hacia arriba).")

    while True:
        # Lee un caracter del teclado
        key = readchar.readkey()

        # Imprime el caracter leído
        print(f"Tecla presionada: {key}")

        # Verifica si la tecla presionada es la flecha hacia arriba (↑)
        if key == '\x1b[A':
            print("¡Presionaste la flecha hacia arriba! Saliendo del bucle.")
            break

if __name__ == "__main__":
    main()
  
