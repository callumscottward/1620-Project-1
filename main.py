from controller import *


def main():
    app = QApplication([])
    window = Television()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
