import requests
from bs4 import BeautifulSoup

# Recetas locales 🍴
recetas_locales = {
    "Spaghetti Bolognesa": {
        "ingredientes": ["Spaghetti", "Carne molida", "Tomate", "Cebolla", "Ajo", "Aceite", "Sal", "Pimienta"],
        "pasos": [
            "Cocer el spaghetti en agua con sal.",
            "Sofreír cebolla y ajo en aceite.",
            "Agregar la carne molida y cocinar bien.",
            "Añadir el tomate y dejar cocinar la salsa.",
            "Servir la salsa sobre el spaghetti."
        ]
    },
    "Ensalada César": {
        "ingredientes": ["Lechuga romana", "Pollo a la plancha", "Pan tostado", "Queso parmesano", "Aderezo César"],
        "pasos": [
            "Lavar y cortar la lechuga.",
            "Cortar el pollo en tiras.",
            "Mezclar todos los ingredientes.",
            "Agregar el aderezo y espolvorear queso parmesano."
        ]
    },
    "Arepas con Queso": {
        "ingredientes": ["Harina de maíz precocida", "Agua", "Sal", "Queso rallado", "Mantequilla"],
        "pasos": [
            "Mezclar harina, agua y sal hasta formar una masa.",
            "Formar bolas y aplanarlas en forma de arepa.",
            "Asar en sartén hasta dorar.",
            "Abrir por la mitad y rellenar con queso y mantequilla."
        ]
    }
}

# Buscar recetas online 🌐
def buscar_recetas_online(ingrediente):
    url = f"https://www.recetasgratis.net/busqueda?q={ingrediente}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print("❌ No se pudo acceder a la página.")
        return []

    soup = BeautifulSoup(respuesta.text, "html.parser")
    recetas = soup.find_all("a", class_="resultado link")

    resultados = []
    for receta in recetas[:5]:  # Tomar solo las primeras 5
        titulo = receta.get("title")
        link = receta.get("href")
        resultados.append((titulo, link))

    return resultados

# Mostrar menú principal 📖
def mostrar_menu():
    print("\n📖 Bienvenido al Recetario Interactivo")
    print("Selecciona una opción:")
    print("1️⃣ Ver recetas locales")
    print("2️⃣ Buscar recetas en internet")
    print("3️⃣ Salir")

# Mostrar detalle de receta local
def mostrar_detalle(nombre):
    receta = recetas_locales.get(nombre)
    if receta:
        print(f"\n📌 Receta: {nombre}")
        print("🥗 Ingredientes:")
        for ing in receta["ingredientes"]:
            print(f"   - {ing}")
        print("\n👩‍🍳 Pasos:")
        for paso in receta["pasos"]:
            print(f"   ✅ {paso}")
    else:
        print("⚠️ Receta no encontrada.")

# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\n👉 Ingresa tu opción: ")

        if opcion == "1":
            print("\n🍴 Recetas locales disponibles:")
            for receta in recetas_locales.keys():
                print(f" - {receta}")
            seleccion = input("\n🔎 Escribe el nombre de la receta para ver más detalles: ")
            mostrar_detalle(seleccion)

        elif opcion == "2":
            ingrediente = input("\n🛒 Ingresa un ingrediente para buscar recetas online: ")
            recetas = buscar_recetas_online(ingrediente)

            if recetas:
                print(f"\n🍲 Recetas encontradas con '{ingrediente}':")
                with open("recetas_online.txt", "w", encoding="utf-8") as f:
                    for i, (titulo, link) in enumerate(recetas, 1):
                        print(f"{i}. {titulo} - {link}")
                        f.write(f"{i}. {titulo} - {link}\n")
                print("\n📁 Recetas guardadas en 'recetas_online.txt'")
            else:
                print("⚠️ No se encontraron recetas.")

        elif opcion == "3":
            print("👋 Gracias por usar el recetario. ¡Buen provecho!")
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")

