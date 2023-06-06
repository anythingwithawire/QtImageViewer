import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from QtImageStackViewer import QtImageStackViewer

if __name__ == '__main__':
    # Create the QApplication.
    app = QApplication(sys.argv)

    # Create an image stack viewer widget.
    viewer = QtImageStackViewer()

    # Customize mouse interaction via the QtImageViewer widget.
    viewer.imageViewer.regionZoomButton = Qt.MouseButton.LeftButton  # set to None to disable
    viewer.imageViewer.zoomOutButton = Qt.MouseButton.RightButton  # set to None to disable
    viewer.imageViewer.wheelZoomFactor = 1.25  # Set to None or 1 to disable
    viewer.imageViewer.panButton = Qt.MouseButton.MiddleButton  # set to None to disable

    # Load an image stack file to be displayed (will popup a file dialog).
    viewer.open()

    # Show the viewer and run the application.
    viewer.show()
    sys.exit(app.exec())

