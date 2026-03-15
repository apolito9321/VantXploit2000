import sys
import os
import subprocess
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFrame, QGridLayout, QMessageBox)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
from login_window import LoginWindow  # ← Importamos la ventana de login

class VantXploit(QWidget):
    # ... (tu código original de __init__ y setup_ui se mantiene igual, solo cambiamos el lanzamiento)

    def __init__(self):
        super().__init__()
        # ... (todo tu código de dir_base, icon_path, etc. igual)

    # ... (todo tu setup_ui igual, con nav, hero, grid, etc.)

    # NO cambies nada más

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # === NUEVO: Mostramos login primero ===
    login = LoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:  # Solo si login OK
        window = VantXploit()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)  # Si cierra sin login, sale
