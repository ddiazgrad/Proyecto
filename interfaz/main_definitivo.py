import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTreeView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from ipyleaflet import Map, Marker, FullScreenControl
from ipywidgets import Widget, Layout
from IPython.display import display
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTreeView, QTableWidget, QTableWidgetItem,
                             QHBoxLayout)

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()

        # Crear mapa y marcador
        lat = 37.7749
        lon = -122.4194

        m = folium.Map(location=[lat, lon], zoom_start=13)
        folium.Marker(location=[lat, lon]).add_to(m)

        # Guardar mapa como archivo HTML
        m.save("mapa.html")

        # Configurar ventana y layout principal
        self.setWindowTitle("Interfaz del Piloto")
        self.setGeometry(100, 100, 1200, 600)
        self.layout = QVBoxLayout()

        # Agregar widgets al layout principal
        self.init_ui()
        self.setLayout(self.layout)

    def init_ui(self):
        # Etiquetas de título
        lbl_vuelos = QLabel("Vuelos Activos", self)
        lbl_vuelos.setFont(QFont("TkDefaultFont", 12, QFont.Bold))

        # Tabla de vuelos activos
        headers = ["Identificación", "Ubicación", "Distancia", "Azimuth", "Elevation", "Tipo de Aeronave"]
        self.table = QTableWidget(3, len(headers), self)
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setDefaultSectionSize(120)  # Cambia 120 al tamaño deseado de las celdas
        self.table.horizontalHeader().setStretchLastSection(True) # Ajustar la última columna al espacio disponible
        self.table.verticalHeader().setVisible(False)             # Ocultar encabezado vertical
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setShowGrid(True)
        self.table.setAlternatingRowColors(True)
        self.table.resizeColumnsToContents()
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        self.table.setItem(0, 0, QTableWidgetItem("AA123"))
        self.table.setItem(0, 1, QTableWidgetItem("37.7749° N, 122.4194° W, 100m"))
        self.table.setItem(0, 2, QTableWidgetItem("5,000 m"))
        self.table.setItem(0, 3, QTableWidgetItem("45°"))
        self.table.setItem(0, 4, QTableWidgetItem("15°"))
        self.table.setItem(0, 5, QTableWidgetItem("Avión"))

        # Crear layout para la sección de vuelos activos
        left_layout = QVBoxLayout()
        left_layout.addWidget(lbl_vuelos)
        left_layout.addWidget(self.table)

        # Mapa de ubicación de la aeronave
        web_view = QWebEngineView()
        web_view.load(QUrl.fromLocalFile(QDir.current().absoluteFilePath("mapa.html")))
        web_view.setFixedSize(450, 450)

        # Crear layout horizontal para mostrar la tabla y el mapa
        map_layout = QHBoxLayout()
        map_layout.addLayout(left_layout)
        map_layout.addWidget(web_view)

        # Agregar el layout horizontal al layout principal
        self.layout.addLayout(map_layout)
        
        # Etiquetas de información de la aeronave
        lbl_velocidad = QLabel("Velocidad: 100 m/s", self)
        lbl_altitud = QLabel("Altitud: 5000 m", self)
        lbl_latitud = QLabel("Latitud: 37.7749° N", self)
        lbl_longitud = QLabel("Longitud: 122.4194° W", self)
        lbl_tipo = QLabel("Tipo de Aeronave: Avión", self)

        # Ajustar la fuente de las etiquetas
        font = QFont("TkDefaultFont", 10)
        lbl_velocidad.setFont(font)
        lbl_altitud.setFont(font)
        lbl_latitud.setFont(font)
        lbl_longitud.setFont(font)
        lbl_tipo.setFont(font)

        # Agregar las etiquetas al layout principal
        info_layout = QVBoxLayout()
        info_layout.addWidget(lbl_velocidad)
        info_layout.addWidget(lbl_altitud)
        info_layout.addWidget(lbl_latitud)
        info_layout.addWidget(lbl_longitud)
        
        
        info_layout.addWidget(lbl_tipo)

        self.layout.addLayout(info_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Interfaz()
    ex.show()
    sys.exit(app.exec_())
