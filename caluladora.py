import re
from tkinter import Tk, Text, Button, END

class Interfaz:
    def __init__(self, ventana):
        # Iniciar ventana
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Crear la pantalla de la calculadora
        self.pantalla = Text(ventana, state="disabled", width=40, height=3, font=("Helvetica", 15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Iniciar la operación como string vacío
        self.operacion = ""

        # Crear los botones
        botones = [
            self.crearBoton(7), self.crearBoton(8), self.crearBoton(9), self.crearBoton(u"\u232B", escribir=False),
            self.crearBoton(4), self.crearBoton(5), self.crearBoton(6), self.crearBoton(u"\u00F7"),
            self.crearBoton(1), self.crearBoton(2), self.crearBoton(3), self.crearBoton("*"),
            self.crearBoton("."), self.crearBoton(0), self.crearBoton("+"), self.crearBoton("-"),
            self.crearBoton("=", escribir=False, ancho=20, alto=2)
        ]

        # Posicionar los botones en la cuadrícula
        contador = 0
        for fila in range(1, 5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1

        # Posicionar el botón "=" al final
        botones[16].grid(row=5, column=0, columnspan=4)

        # Vincular teclas del teclado
        self.ventana.bind("<Key>", self.tecla_presionada)

    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15),
                      command=lambda: self.click(valor, escribir))

    def evaluar_operacion(self, operacion_str):
        """Evalúa la operación matemática de forma manual y segura"""
        try:
            # Limpiar y preparar la operación
            operacion_str = operacion_str.replace(" ", "")
            operacion_str = re.sub(u"\u00F7", "/", operacion_str)
            
            # Si no hay operadores, es solo un número
            if not any(op in operacion_str for op in ['+', '-', '*', '/']):
                return float(operacion_str)
            
            # Dividir en números y operadores
            numeros = []
            operadores = []
            numero_actual = ""
            
            for i, char in enumerate(operacion_str):
                if char in "+-*/":
                    # Manejar números negativos al inicio o después de un operador
                    if char == '-' and (i == 0 or operacion_str[i-1] in "+-*/"):
                        numero_actual += char
                    else:
                        if numero_actual:
                            numeros.append(float(numero_actual))
                            numero_actual = ""
                        operadores.append(char)
                else:
                    numero_actual += char
            
            # Agregar el último número
            if numero_actual:
                numeros.append(float(numero_actual))
            
            # Si no hay suficientes números u operadores
            if len(numeros) == 0:
                return 0
            if len(numeros) == 1:
                return numeros[0]
            if len(operadores) == 0:
                return numeros[0]
            
            # Procesar multiplicación y división primero
            i = 0
            while i < len(operadores):
                if operadores[i] in ['*', '/']:
                    if operadores[i] == '*':
                        resultado = numeros[i] * numeros[i + 1]
                    else:  # división
                        if numeros[i + 1] == 0:
                            raise ValueError("División por cero")
                        resultado = numeros[i] / numeros[i + 1]
                    
                    # Reemplazar los dos números y el operador con el resultado
                    numeros[i] = resultado
                    numeros.pop(i + 1)
                    operadores.pop(i)
                else:
                    i += 1
            
            # Procesar suma y resta de izquierda a derecha
            resultado = numeros[0]
            for i, operador in enumerate(operadores):
                if operador == '+':
                    resultado += numeros[i + 1]
                elif operador == '-':
                    resultado -= numeros[i + 1]
            
            return resultado
            
        except (ValueError, IndexError, ZeroDivisionError) as e:
            raise ValueError(f"Error en la operación: {str(e)}")

    def click(self, texto, escribir):
        if not escribir:
            if texto == "=" and self.operacion:
                try:
                    resultado = self.evaluar_operacion(self.operacion)
                    # Formatear el resultado (quitar .0 si es entero)
                    if resultado.is_integer():
                        resultado_str = str(int(resultado))
                    else:
                        resultado_str = str(round(resultado, 8))  # Limitar decimales
                    
                    self.operacion = resultado_str
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(resultado_str)
                except Exception as e:
                    self.limpiarPantalla()
                    self.mostrarEnPantalla("Error")
                    
            elif texto == u"\u232B":  # Botón de borrar
                self.operacion = self.operacion[:-1]
                self.limpiarPantalla()
                self.mostrarEnPantalla(self.operacion)
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")

    def tecla_presionada(self, event):
        """Maneja las teclas del teclado"""
        tecla = event.keysym

        if tecla.isdigit() or tecla in ["plus", "minus", "asterisk", "slash", "period"]:
            conversion = {"plus": "+", "minus": "-", "asterisk": "*", "slash": "/", "period": "."}
            valor = conversion.get(tecla, tecla)
            self.click(valor, escribir=True)

        elif tecla == "Return":
            self.click("=", escribir=False)

        elif tecla == "BackSpace":
            self.click(u"\u232B", escribir=False)

        elif tecla == "Escape":
            self.limpiarPantalla()
            self.operacion = ""

# Iniciar la aplicación
if __name__ == "__main__":
    ventana_principal = Tk()
    calculadora = Interfaz(ventana_principal)
    ventana_principal.mainloop()