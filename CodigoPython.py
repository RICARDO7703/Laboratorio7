import serial
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Declaración de constantes
ledRojo = 5
ledAmarillo = 6
ledVerde = 7
pb1 = 2
pb2 = 3
pb3 = 4
potenciometro = "A3"  # La entrada analógica en Arduino se mapea a A3 en PySerial

# Inicialización de la comunicación serial
arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' al puerto que estés utilizando

# Creación de la ventana de la aplicación
root = tk.Tk()
root.title("Lectura de potenciómetro y gráfico")

# Crear una etiqueta para mostrar el valor del potenciómetro
etiqueta_valor = tk.Label(root, text="Valor del potenciómetro: ")
etiqueta_valor.pack()

# Función para actualizar el valor del potenciómetro y la gráfica
def actualizar_datos():
    # Leer el valor del potenciómetro desde Arduino
    valor_potenciometro = int(arduino.readline().decode().strip())
    # Mostrar el valor en la etiqueta
    etiqueta_valor.config(text=f"Valor del potenciómetro: {valor_potenciometro}")
    # Agregar el valor a la lista de datos
    valores_potenciometro.append(valor_potenciometro)
    # Actualizar la gráfica
    grafica.clear()
    grafica.plot(valores_potenciometro, 'b-')  # 'b-' indica una línea azul sólida
    canvas.draw()

# Listas para almacenar los valores del potenciómetro
valores_potenciometro = []

# Configurar la ventana de la gráfica
figura = Figure(figsize=(6, 4), dpi=100)
grafica = figura.add_subplot(111)
grafica.set_xlabel('Tiempo')
grafica.set_ylabel('Valor del potenciómetro')
grafica.set_title('Gráfico del valor del potenciómetro en función del tiempo')

# Crear el lienzo de la gráfica
canvas = FigureCanvasTkAgg(figura, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Iniciar el bucle de actualización de datos
root.after(100, actualizar_datos)

# Iniciar la aplicación
root.mainloop()

# Cerrar la conexión serial al cerrar la ventana
arduino.close()
