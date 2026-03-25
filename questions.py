import random
import string

lower = string.ascii_lowercase

categories = {
    "programacion": ["python", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "juegos": ["counter", "valorant", "minecraft", "terraria", "brawl"],
    "paises": ["argentina", "brasil", "uruguay", "francia", "colombia"]
}

print("¡Bienvenido al Ahorcado!")
print("-" * 20)

# Mostrar categorías disponibles
print("Categorías disponibles:")
for category in categories.keys():
    print(f"- {category.capitalize()}")

# Elección de categoría
while True:
    chosen_category = input("\nElegí una categoría: ").lower()
    if chosen_category in categories:
        break
    else:
        print("Categoría no encontrada.")

# Tomamos todos los elementos de la lista (len) de forma aleatoria. 
# Esto crea una lista nueva mezclada y garantiza que no se repitan.
words_to_play = random.sample(categories[chosen_category], k=len(categories[chosen_category]))

print(f"\n Jugaremos con: {chosen_category.capitalize()}")
print(f"Hay {len(words_to_play)} palabras en esta categoría.")

# Bucle principal para jugar varias rondas
for word in words_to_play:
    guessed = []
    attempts = 6
    points = 0
    
    print(f"NUEVA RONDA ")
    
    while attempts > 0:
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        
        print(progress)

        if "_" not in progress:
            points += 6
            print(f"Ganaste esta ronda.")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        user_input = input("Ingresá una letra: ").lower()
        
        if len(user_input) == 1 and user_input in lower:
            if user_input in guessed:
                print("Ya usaste esa letra.")
            elif user_input in word:
                guessed.append(user_input)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(user_input)
                attempts -= 1
                points -= 1
                print("Esa letra no está en la palabra.")
        else:
            print("Entrada no válida")
            
        print("-" * 10)

    else:
        print(f"¡Perdiste esta ronda! La palabra era: {word}")

    # Preguntar si quiere seguir jugando la siguiente palabra de la lista
    if word != words_to_play[-1]: # Si no es la última palabra
        continuar = input("\n¿Querés jugar con la siguiente palabra? (s/n): ").lower()
        if continuar != 's':
            break
    else:
        print("\n¡Te quedaste sin palabras en esta categoría!")
