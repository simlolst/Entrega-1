import random
import string

lower = string.ascii_lowercase # Variable para tener las minúsculas
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Felicidades! Ganaste.")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    user_input = input("Ingresá una letra: ").lower() 
    
    # verificamos que sea 1 sola letra Y que esté en el abecedario
    if len(user_input) == 1 and user_input in lower:
        if user_input in guessed:
            print("Ya usaste esa letra.")
        elif user_input in word:
            guessed.append(user_input)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(user_input)
            attempts -= 1
            print("Esa letra no está en la palabra.")
    else:
        # Se ejecuta si ingresan números, símbolos o más de una letra junta
        print("Entrada no válida")
        
    print("-" * 20)

else:
    print(f"¡Perdiste! La palabra era: {word}")