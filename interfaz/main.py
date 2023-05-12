import tkinter as tk
from tkinter import ttk
import folium

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz del Piloto")

        # Etiquetas de título
        lbl_vuelos = ttk.Label(self.root, text="Vuelos Activos", font=("TkDefaultFont", 12, "bold"))
        lbl_vuelos.place(x=20, y=20)
        lbl_info = ttk.Label(self.root, text="Información de la Aeronave", font=("TkDefaultFont", 12, "bold"))
        lbl_info.place(x=20, y=250)

        # Tabla de vuelos activos
        table = ttk.Treeview(self.root, columns=("id", "location", "distance", "azimuth", "elevation", "aircraft"), show="headings", selectmode="browse")
        table.heading("id", text="Identificación")
        table.heading("location", text="Ubicación")
        table.heading("distance", text="Distancia")
        table.heading("azimuth", text="Azimuth")
        table.heading("elevation", text="Elevation")
        table.heading("aircraft", text="Tipo de Aeronave")
        table.column("id", width=100, anchor="center")
        table.column("location", width=200, anchor="center")
        table.column("distance", width=100, anchor="center")
        table.column("azimuth", width=100, anchor="center")
        table.column("elevation", width=100, anchor="center")
        table.column("aircraft", width=100, anchor="center")
        table.insert("", "end", values=("AA123", "37.7749° N, 122.4194° W, 100m", "5,000 m", "45°", "15°", "Avión"))
        table.insert("", "end", values=("UA456", "39.7392° N, 104.9903° W, 150m", "8,000 m", "90°", "10°", "Avión"))
        table.insert("", "end", values=("DL789", "40.7128° N, 74.0060° W, 200m", "10,000 m", "180°", "20°", "Helicóptero"))
        table.place(x=20, y=50)
        

        # Etiquetas de información de la aeronave
        lbl_id = ttk.Label(self.root, text="Identificación: JJJJJ")
        lbl_id.place(x=20, y=280)
        lbl_type = ttk.Label(self.root, text="Tipo de Aeronave: Avión")
        lbl_type.place(x=20, y=310)
        lbl_speed = ttk.Label(self.root, text="Velocidad: 250 m/s")
        lbl_speed.place(x=20, y=340)
        lbl_freq = ttk.Label(self.root, text="Latitud: XX °")
        lbl_freq.place(x=20, y=370)
        lbl_time = ttk.Label(self.root, text="Longitud: YY °")
        lbl_time.place(x=20, y=400)
        lbl_time = ttk.Label(self.root, text="Altitud: ZZ m")
        lbl_time.place(x=20, y=430)

        # Configuración de la ventana
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        

root = tk.Tk()
ex = Interfaz(root)
root.mainloop()