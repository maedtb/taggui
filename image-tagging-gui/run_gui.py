import sys

from PySide6.QtWidgets import QApplication

from widgets.main_window import MainWindow


def run_gui():
    app = QApplication([])
    # The application name is shown in the taskbar.
    app.setApplicationName('Image Tagging GUI')
    # The application display name is shown in the title bar.
    app.setApplicationDisplayName('Image Tagging GUI')
    app.setStyle('Fusion')
    main_window = MainWindow(app)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run_gui()
