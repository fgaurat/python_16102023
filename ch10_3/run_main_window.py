from PySide6.QtWidgets import QApplication, QMainWindow

from main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Connecter le bouton à la fonction
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
    #     # Lire la valeur de 'name'
        name_value = self.lineEdit.text()
        print(name_value)

    #     # Afficher la valeur dans 'hello'
        self.hello.setText(f"Hello {name_value}")


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
