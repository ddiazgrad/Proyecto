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
        self.layout.addWidget(lbl_vuelos)

        # Tabla de vuelos activos
        # ... (El código de la tabla sigue igual)
        # ...

        # Mapa de ubicación de la aeronave
        web_view = QWebEngineView()
        web_view.load(QUrl.fromLocalFile(QDir.current().absoluteFilePath("mapa.html")))
        web_view.setFixedSize(450, 450)
        self.layout.addWidget(web_view)

        # Etiquetas de información de la aeronave
        # ... (El código de las etiquetas sigue igual)
        # ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Interfaz()
    ex.show()
    sys.exit(app.exec_())
