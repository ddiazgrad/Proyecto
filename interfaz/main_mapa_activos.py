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
        left_layout.addWidget(self.table)  # Asegúrate de agregar la tabla al layout de la izquierda

        # Agregar layout de la sección de vuelos activos al layout principal
        self.layout.addLayout(left_layout)

        # Mapa de ubicación de la aeronave
        web_view = QWebEngineView()
        web_view.load(QUrl.fromLocalFile(QDir.current().absoluteFilePath("mapa.html")))
        web_view.setFixedSize(450, 450)
        self.layout.addWidget(web_view, 0, Qt.AlignTop | Qt.AlignRight)

        # Etiquetas de información de la aeronave
        # ... (El código de las etiquetas sigue igual)
        # ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Interfaz()
    ex.show()
    sys.exit(app.exec_())
