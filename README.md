# 🚀 Portafolio - Nivel 2: APIs, Web Scraping y GUI en Python

Este repositorio corresponde al **Nivel 2** de mi portafolio de aprendizaje en **Python**.  
En este nivel presento proyectos que integran consumo de **APIs**, **Web Scraping** y **aplicaciones gráficas (GUI)**, mostrando mayor versatilidad y práctica en programación.  

---

## 📂 Proyectos incluidos

| Proyecto | Descripción | Código |
|----------|-------------|--------|
| 🌦️ **Consultor de clima con API** | Consulta en tiempo real el clima de una ciudad usando una API pública (OpenWeatherMap). | `consultor_clima.py` |
| 🍳 **Recetario con Web Scraping** | Extrae recetas desde la web según ingrediente buscado. | `recetario_on_off.py` |
| 🖼️ **Gestor de tareas con GUI** | Aplicación gráfica para crear y gestionar tareas con interfaz en Tkinter. | `gestor_tareas.py` |

---

### 🌦️ 1. Consultor de clima con API (`consultor_clima.py`)
Un programa que se conecta a la API de **OpenWeatherMap** para obtener el clima actual de cualquier ciudad.  
- **Habilidades practicadas:** consumo de APIs, manejo de JSON, requests, formateo de datos.  
#### Uso:
1. Obtén una API Key gratuita en [OpenWeatherMap](https://openweathermap.org/).  
2. Reemplaza la variable `API_KEY` en el script.  
3. Ejecuta:  
   ```bash
   python consultor_clima.py
4. Ingresa una ciudad y recibirás temperatura, humedad y descripción del clima.

---

### 🍲 2. Recetario con web scraping (`recetario.py`)
Un script que busca recetas en línea según un ingrediente dado, usando scraping en la web de RecetasGratis.  
- **Habilidades practicadas:** web scraping con BeautifulSoup, manejo de cadenas de texto y archivos `.txt`.  
 1. Ejecutar el script:  
     ```bash
     python recetario_on_off.py
     ```
 2. Ingresar un ingrediente.  
 3. Se mostrarán las **5 primeras recetas encontradas** y se guardarán en `recetas.txt`.  

---

### ✅ 3. Gestor de tareas con GUI (`gestor_tareas.py`)
Una aplicación gráfica para organizar tareas pendientes.  
- **Habilidades practicadas:** GUI con Tkinter, persistencia con JSON, listas dinámicas.  
 1. Ejecutar el script:  
     ```bash
     python gestor_tareas.py
     ```
 2. Permite **agregar, completar y eliminar tareas**.  
 3. Las tareas se guardan en `tareas.json` para no perderse al cerrar el programa.  

---

## 🛠 Tecnologías usadas
- **Python**  
- Librerías: `requests`, `beautifulsoup4`, `tkinter`, `json`, `os`  

---

## 🎯 Habilidades desarrolladas
- Consumo de **APIs** y manejo de datos en formato JSON.  
- **Web Scraping** para obtener información desde páginas web.  
- Creación de **interfaces gráficas** con Tkinter.  
- Persistencia de datos con archivos `.txt` y `.json`.  

---

## 📌 Próximos pasos
En el siguiente nivel de mi portafolio incluiré:  
✅ Pequeñas aplicaciones de escritorio más avanzadas.  
✅ Uso de **bases de datos (SQLite, PostgreSQL)**.  
✅ Mini proyectos con **Flask/Django** para la web.  

---

👩‍💻 *Repositorio creado por [Iveth Parra](https://www.linkedin.com/in/iveth-parra-herrera-351a6a235).*  
