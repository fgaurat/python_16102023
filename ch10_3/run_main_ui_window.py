import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QLineEdit,QPushButton


def on_pushButton_clicked():
    name_value = name.text()
    hello.setText(name_value)


def main():
    app = QApplication(sys.argv)
    ui_file_name = "main_window.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    global name,hello
    name = window.findChild(QLineEdit,'lineEdit')
    hello = window.findChild(QLineEdit,'hello')
    pushButton = window.findChild(QPushButton,'pushButton')
    pushButton.clicked.connect(on_pushButton_clicked)

    window.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()
