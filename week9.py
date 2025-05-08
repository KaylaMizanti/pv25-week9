from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout,
    QTabWidget, QPushButton, QLineEdit, QTextEdit, QFileDialog,
    QMenuBar, QMenu, QAction, QFontDialog, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - F1D022127")
        self.setGeometry(100, 100, 600, 450)

        # ==== Menu Bar ====
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        fitur_menu = menubar.addMenu("Fitur")

        keluar_action = QAction("Keluar", self)
        keluar_action.triggered.connect(self.close)
        file_menu.addAction(keluar_action)

        input_nama_action = QAction("Input Nama", self)
        input_nama_action.triggered.connect(lambda: self.tabs.setCurrentIndex(0))
        fitur_menu.addAction(input_nama_action)

        pilih_font_action = QAction("Pilih Font", self)
        pilih_font_action.triggered.connect(lambda: self.tabs.setCurrentIndex(1))
        fitur_menu.addAction(pilih_font_action)

        buka_file_action = QAction("Buka File", self)
        buka_file_action.triggered.connect(lambda: self.tabs.setCurrentIndex(2))
        fitur_menu.addAction(buka_file_action)

        # ==== Tab Widget ====
        self.tabs = QTabWidget()
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.tabs)

        # Tab 1: Input Nama
        tab1 = QWidget()
        vbox1 = QVBoxLayout()
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Input Nama")
        self.result_label = QLabel("Nama:")
        btn_submit = QPushButton("Input Nama")
        btn_submit.setStyleSheet("background-color: #d63384; color: white;")
        btn_submit.clicked.connect(self.display_name)
        vbox1.addWidget(btn_submit)
        vbox1.addWidget(self.input_line)
        vbox1.addWidget(self.result_label)
        tab1.setLayout(vbox1)

        # Tab 2: Pilih Font
        tab2 = QWidget()
        vbox2 = QVBoxLayout()
        self.font_display = QLineEdit("Pilih Font")
        btn_font = QPushButton("Pilih Font")
        btn_font.setStyleSheet("background-color: #d63384; color: white;")
        btn_font.clicked.connect(self.choose_font)
        vbox2.addWidget(btn_font)
        vbox2.addWidget(self.font_display)
        tab2.setLayout(vbox2)

        # Tab 3: Buka File
        tab3 = QWidget()
        vbox3 = QVBoxLayout()
        self.file_display = QLineEdit("Buka File .txt")
        self.text_area = QTextEdit()
        btn_file = QPushButton("Buka File")
        btn_file.setStyleSheet("background-color: #d63384; color: white;")
        btn_file.clicked.connect(self.open_file)
        vbox3.addWidget(btn_file)
        vbox3.addWidget(self.file_display)
        vbox3.addWidget(self.text_area)
        tab3.setLayout(vbox3)

        # Tambah semua tab
        self.tabs.addTab(tab1, "Input Nama")
        self.tabs.addTab(tab2, "Pilih Font")
        self.tabs.addTab(tab3, "Buka File")

        # ==== Label Identitas ====
        self.identity_label = QLabel("Nama: Kayla Mizanti | NIM: F1D022127")
        self.identity_label.setAlignment(Qt.AlignCenter)
        self.identity_label.setStyleSheet("color: gray; font-style: italic; margin-top: 10px;")
        self.main_layout.addWidget(self.identity_label)

        self.setCentralWidget(self.central_widget)

    def display_name(self):
        name = self.input_line.text()
        self.result_label.setText(f"Nama: {name}")

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_display.setFont(font)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open TXT", "", "Text Files (*.txt)")
        if file_path:
            self.file_display.setText(file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.setText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
