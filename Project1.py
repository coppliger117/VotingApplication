from gui1 import *
from Logic1 import *
import csv

def main():
    import sys
    app = QApplication([])
    Dialog = Logic()
    Dialog.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()