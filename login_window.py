import sys
import os
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QMessageBox, QCheckBox, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont
from database import register_user, verify_login

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VantXploit2000 - Login")
        self.setFixedSize(420, 520)
        self.setStyleSheet("""
            QWidget { 
                background-color: #080808; 
                color: #d1d1d1; 
                font-family: 'Segoe UI', Tahoma, sans-serif; 
            }
        """)
        
        # === CONTENEDOR CENTRAL (igual que tu QFrame#container) ===
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)
        
        card = QFrame()
        card.setObjectName("container")
        card.setStyleSheet("""
            QFrame#container {
                background-color: #0c0c0c;
                border: 1px solid #181818;
                border-radius: 16px;
                padding: 30px;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(18)
        
        # === LOGO + TÍTULO (exacto estilo hero de tu app) ===
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Iconos")
        logo_label = QLabel()
        logo_pixmap = QPixmap(os.path.join(icon_path, "Logo.png"))
        if not logo_pixmap.isNull():
            logo_label.setPixmap(logo_pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(logo_label)
        
        title = QLabel("VANTXPLOIT")
        title.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        title.setStyleSheet("color: #fff; letter-spacing: 2px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(title)
        
        subtitle = QLabel("Inicia sesión para continuar")
        subtitle.setStyleSheet("color: #555; font-size: 14px;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(subtitle)
        
        # === CAMPOS DE TEXTO ===
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(self.input_style())
        card_layout.addWidget(self.email_input)
        
        # Password + botón ojo
        pass_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())
        pass_layout.addWidget(self.password_input)
        
        self.toggle_btn = QPushButton("👁")
        self.toggle_btn.setFixedSize(40, 40)
        self.toggle_btn.setStyleSheet("""
            QPushButton { background-color: #121212; border: 1px solid #222; border-radius: 8px; }
            QPushButton:hover { border-color: #3d5afe; }
        """)
        self.toggle_btn.clicked.connect(self.toggle_password)
        pass_layout.addWidget(self.toggle_btn)
        
        card_layout.addLayout(pass_layout)
        
        # Recordarme
        self.remember = QCheckBox("Recordarme")
        self.remember.setStyleSheet("color: #777; font-size: 13px;")
        card_layout.addWidget(self.remember)
        
        # === BOTONES ===
        btn_login = QPushButton("INICIAR SESIÓN")
        btn_login.setFixedHeight(48)
        btn_login.setStyleSheet(self.button_style())
        btn_login.clicked.connect(self.login)
        card_layout.addWidget(btn_login)
        
        btn_signup = QPushButton("CREAR CUENTA")
        btn_signup.setFixedHeight(48)
        btn_signup.setStyleSheet(self.button_style(secondary=True))
        btn_signup.clicked.connect(self.signup)
        card_layout.addWidget(btn_signup)
        
        main_layout.addWidget(card)
        self.setLayout(main_layout)
    
    # Estilos reutilizables (copiados de tu app)
    def input_style(self):
        return """
            QLineEdit {
                background-color: #121212;
                border: 1px solid #222;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
            }
            QLineEdit:focus {
                border-color: #3d5afe;
                background-color: #1a1a1a;
            }
        """
    
    def button_style(self, secondary=False):
        base = """
            QPushButton {
                background-color: #121212;
                border: 1px solid #222;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
                font-weight: 600;
                color: #efefef;
            }
            QPushButton:hover {
                background-color: #1a1a1a;
                border-color: #3d5afe;
                color: #3d5afe;
            }
        """
        if secondary:
            return base.replace("#121212", "#0c0c0c")  # un poco más oscuro
        return base
    
    def toggle_password(self):
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_btn.setText("🙈")
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_btn.setText("👁")
    
    def login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text()
        
        if not email or not password:
            QMessageBox.warning(self, "Error", "Completa todos los campos")
            return
        
        if verify_login(email, password):
            QMessageBox.information(self, "¡Bienvenido!", f"Acceso concedido\nHola de nuevo 👋")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Email o contraseña incorrectos")
    
    def signup(self):
        email = self.email_input.text().strip()
        password = self.password_input.text()
        
        if not email or not password:
            QMessageBox.warning(self, "Error", "Completa todos los campos")
            return
        
        if register_user(email, "Usuario", password):
            QMessageBox.information(self, "¡Cuenta creada!", "Ahora inicia sesión")
        else:
            QMessageBox.warning(self, "Error", "El email ya está registrado")