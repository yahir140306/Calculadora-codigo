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

    def click(self, texto, escribir):
        if not escribir:
            if texto == "=" and self.operacion:
                try:
                    self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                    resultado = str(eval(self.operacion))  # Evaluar la operación
                    self.operacion = resultado  # Guardar el resultado para futuras operaciones
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(resultado)
                except:
                    self.limpiarPantalla()
                    self.mostrarEnPantalla("Error")
            elif texto == u"\u232B":  # Botón de borrar
                self.operacion = self.operacion[:-1]  # Borra último carácter
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
        # self.pantalla.delete("1.0", END)  # Borra antes de mostrar para evitar repetición
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")

    def tecla_presionada(self, event):
        """ Maneja las teclas del teclado """
        tecla = event.keysym  # Obtiene la tecla presionada

        # Si es un número, un operador, o un punto decimal, agrégalo a la operación
        if tecla.isdigit() or tecla in ["plus", "minus", "asterisk", "slash", "period"]:
            conversion = {"plus": "+", "minus": "-", "asterisk": "*", "slash": "/", "period": "."}
            valor = conversion.get(tecla, tecla)  # Reemplazar nombres de teclas por símbolos
            self.click(valor, escribir=True)

        elif tecla == "Return":  # Enter ejecuta la operación
            self.click("=", escribir=False)

        elif tecla == "BackSpace":  # Retroceso borra un carácter
            self.click(u"\u232B", escribir=False)

        elif tecla == "Escape":  # Escape limpia la pantalla
            self.limpiarPantalla()
            self.operacion = ""

# Iniciar la aplicación
ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
