# Calculadora con Python - Tkinter

## 📸 Vista previa

![alt text](Imagen.png)

# 🧮 Calculadora en Python con Tkinter

Una calculadora gráfica construida con `Tkinter`, la biblioteca estándar de interfaces gráficas en Python. Soporta operaciones básicas y puede ser usada tanto con el ratón como con el teclado.

## 🚀 Características

- Interfaz gráfica sencilla y moderna
- Operaciones básicas: suma, resta, multiplicación, división
- Soporte completo para teclado:
  - Enter (`Return`) para calcular
  - Backspace para borrar
  - Escape para limpiar pantalla
- Botón de retroceso (`⌫`) para borrar el último carácter
- Evaluación de expresiones usando `eval()` (controlada con validación)

## 🧠 Estructura del código

La lógica está contenida dentro de la clase `Interfaz`, que maneja la creación de la ventana, los botones y la interacción con el usuario.

### Componentes clave:

| Método                | Función                                        |
| --------------------- | ---------------------------------------------- |
| `crearBoton()`        | Crea un botón con un valor específico          |
| `click()`             | Maneja los clics y evalúa operaciones          |
| `mostrarEnPantalla()` | Muestra texto en la pantalla de la calculadora |
| `limpiarPantalla()`   | Limpia el área de visualización                |
| `tecla_presionada()`  | Soporta entradas desde el teclado              |

## 🧰 Requisitos

- Python 3.x
- Biblioteca estándar (`tkinter`, `re`)

No se requieren dependencias externas.

## 🖥️ Instalación y ejecución

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/calculadora-tkinter.git
   cd calculadora-tkinter
   ```

2. Ejecuta el archivo:
   ```bash
   python calculadora.py
   ```

> Asegúrate de tener `Tkinter` habilitado en tu instalación de Python.

## 📦 Archivo principal

`calculadora.py`: contiene toda la lógica de la aplicación.

## 📚 Notas técnicas

- Usa `eval()` para evaluar expresiones matemáticas. Aunque está limitado a entradas internas, no se recomienda para aplicaciones web o no confiables sin sanitización estricta.
- Los símbolos como `÷` son convertidos internamente a `/` antes de la evaluación.
- La pantalla se mantiene en estado `disabled` para evitar edición manual directa.
