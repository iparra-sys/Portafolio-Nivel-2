import tkinter as tk
from tkinter import messagebox
import json
import os

ARCHIVO = "tareas.json"

# -------------------------------
# Funciones
# -------------------------------
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_tareas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        tareas.append({"tarea": tarea, "completada": False})
        entrada.delete(0, tk.END)
        actualizar_lista()
        guardar_tareas()
    else:
        messagebox.showwarning("⚠️ Atención", "Ingrese una tarea.")

def marcar_completada():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = not tareas[index]["completada"]
        actualizar_lista()
        guardar_tareas()

def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tarea_eliminada = tareas.pop(index)
        actualizar_lista()
        guardar_tareas()
        messagebox.showinfo("🗑️ Eliminada", f"Tarea eliminada: {tarea_eliminada['tarea']}")

def actualizar_lista():
    lista.delete(0, tk.END)
    for t in tareas:
        estado = "✔️" if t["completada"] else "❌"
        lista.insert(tk.END, f"{estado} {t['tarea']}")

# -------------------------------
# Interfaz gráfica
# -------------------------------
ventana = tk.Tk()
ventana.title("📝 Gestor de Tareas")
ventana.geometry("450x500")
ventana.config(bg="#e6f0fa")

# Título
titulo = tk.Label(
    ventana,
    text="Gestor de Tareas",
    font=("Comic San MS", 15, "bold"),
    bg="#004080",
    fg="white",
    pady=10
)
titulo.pack(fill="x")

# Entrada de texto
entrada_frame = tk.Frame(ventana, bg="#e6f0fa")
entrada_frame.pack(pady=10)

entrada = tk.Entry(entrada_frame, width=30, font=("Arial", 12))
entrada.grid(row=0, column=0, padx=5)

btn_agregar = tk.Button(
    entrada_frame,
    text="➕ Agregar",
    command=agregar_tarea,
    bg="#007acc",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
btn_agregar.grid(row=0, column=1)

# Lista de tareas
lista_frame = tk.Frame(ventana, bg="#e6f0fa")
lista_frame.pack(pady=10)

lista = tk.Listbox(
    lista_frame,
    width=50,
    height=12,
    font=("Arial", 11),
    selectbackground="#80c1ff"
)
lista.pack()

# Botones de acción
btn_frame = tk.Frame(ventana, bg="#e6f0fa")
btn_frame.pack(pady=15)

btn_completar = tk.Button(
    btn_frame,
    text="✔️ Completar",
    command=marcar_completada,
    bg="#28a745",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
btn_completar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(
    btn_frame,
    text="🗑️ Eliminar",
    command=eliminar_tarea,
    bg="#dc3545",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
btn_eliminar.grid(row=0, column=1, padx=5)

# Cargar tareas
tareas = cargar_tareas()
actualizar_lista()

ventana.mainloop()
