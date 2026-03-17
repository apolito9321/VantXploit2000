# VantXploit creado por frostziadito (discord)
import sys
import os
import subprocess
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QScrollArea, QGridLayout, QGraphicsColorizeEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QLinearGradient

class ZenOsintPurple(QWidget):
    def __init__(self):
        super().__init__()

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(os.path.dirname(self.script_dir), "Iconos")
        
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("VantXploit The best")
        self.setFixedSize(960, 720)
        

        self.setStyleSheet("""
            QWidget { 
                background-color: #050505; 
                color: #e0e0e0; 
                font-family: 'Segoe UI', sans-serif; 
            }
            
            QScrollArea { border: none; background: transparent; }
            

            QScrollBar:vertical {
                border: none;
                background: #0a0a0a;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #A020F0;
                border-radius: 5px;
                min-height: 20px;
            }


            QPushButton#tool_btn {
                background-color: #0d0d0f;
                border: 1px solid #1c1c1e;
                border-radius: 12px;
                padding: 12px;
                text-align: left;
                font-size: 13px;
                font-weight: 600;
            }
            
            QPushButton#tool_btn:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A020F0, stop:1 #4B0082);
                border: 1px solid #D680FF;
                color: #ffffff;
            }

            QLabel { background: transparent; border: none; }
            
            QLabel#main_title {
                font-size: 26px;
                font-weight: 900;
                color: #ffffff;
                letter-spacing: 1px;
            }
        """)

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(40, 40, 40, 40) 
      
  title = QLabel("!!VantXploit The best!!")
        title.setObjectName("main_title")
        layout_principal.addWidget(title)
        
        layout_principal.addSpacing(30)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        container = QWidget()
        grid = QGridLayout(container)
        grid.setSpacing(15)
        grid.setContentsMargins(0, 0, 0, 0)


        tools = [
            ("Search by ip", "herramienta5.svg", "IP.py"),
            ("Phone number", "herramienta5.svg", "Telefono.py"),
            ("Email footprint", "Email_Footprint.svg", "Email_Footprint.py"),
            ("Search user", "user5.svg", "Usuario.py"),
            ("Web Information", "Web.svg", "Info_web.py"),
            
            ("Port scanning", "Escaneo.svg", "Puertos.py"),
            ("wifi test", "wifi5.svg", "Wifi.py"),
            ("Your IP", "TuIP.svg", "config5.py"),
            ("Server Response", "herramienta5.svg", "Servidor_respuesta.py"),
            ("YouTube Downloader", "youtube5.svg", "Youtube.py"),
            ("Discord Token", "discord5.svg", "Discord_token_info.py"),
            ("Server Discord", "discord5.svg", "Discord_servidor_info.py"),
            ("Spam Webhook", "Spam.svg", "Spam.py"),
            ("Roblox ID", "id5.svg", "Roblox.py"),
            ("User Roblox", "roblox5.svg", "Roblox.py"),
            ("SQL vulnerability", "config5.svg", "Sql.py"),
            ("Generate QR", "qr5.svg", "Qr.py"),
            ("Links", "links5.svg", "Links.py"),
            ("Decode base64", "herramienta5.svg", "Base.py"),
            ("Generate fake identity", "id5.svg", "ID.py"),
            ("W11 Optimization", "herramienta5.png", "TGO.bat"),
            ("Custom Notepad", "herramienta5.png", "Notepad/Notepad.py"),
          
            ("Page 2", "user5.png", "Herramientas2.py"),
        ]

        for i, (name, icon_file, script) in enumerate(tools):
            btn = QPushButton()
            btn.setObjectName("tool_btn")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            
            btn_layout = QHBoxLayout(btn)
            btn_layout.setContentsMargins(12, 8, 12, 8)
            btn_layout.setSpacing(15)


            icon_label = QLabel()
            pix = QPixmap(os.path.join(self.icon_path, icon_file))
            
            if not pix.isNull():

                icon_label.setPixmap(pix.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                

                color_effect = QGraphicsColorizeEffect()
                color_effect.setColor(QColor("#BF40FF")) 
                icon_label.setGraphicsEffect(color_effect)
            else:
                icon_label.setText("•")
            
            name_label = QLabel(name)
            name_label.setStyleSheet("font-size: 13px;")

            btn_layout.addWidget(icon_label)
            btn_layout.addWidget(name_label)
            btn_layout.addStretch()
            
            btn.clicked.connect(lambda ch, s=script: self.run_app(s))
            grid.addWidget(btn, i // 3, i % 3)

        scroll.setWidget(container)
        layout_principal.addWidget(scroll)

    def run_app(self, script_name):
        path = os.path.join(self.script_dir, script_name)
        if os.path.exists(path):
            if script_name.lower().endswith('.bat'):
                try:
                    os.startfile(path)          # Abre el .bat exactamente como si hicieras doble click
                except Exception as e:
                    print(f"Error al abrir el BAT: {e}")
            else:
                subprocess.Popen([sys.executable, path])
        else:
            print(f"[!] Archivo no encontrado: {path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZenOsintPurple()
    window.show()
    sys.exit(app.exec())
