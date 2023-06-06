import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from QtImageViewer import QtImageViewer


# Custom slot for handling mouse clicks in our viewer.
# This example just prints the (row, column) matrix index
# of the image pixel that was clicked on.
def handleLeftClick(x, y):
    row = int(y)
    column = int(x)
    print("Pixel (row=" + str(row) + ", column=" + str(column) + ")")


if __name__ == '__main__':
    # Create the QApplication.
    app = QApplication(sys.argv)

    # Create an image viewer widget.
    viewer = QtImageViewer()

    # Set viewer's aspect ratio mode.
    # !!! ONLY applies to full image view.
    # !!! Aspect ratio always ignored when zoomed.
    #   Qt.AspectRatioMode.IgnoreAspectRatio: Fit to viewport.
    #   Qt.AspectRatioMode.KeepAspectRatio: Fit in viewport using aspect ratio.
    #   Qt.AspectRatioMode.KeepAspectRatioByExpanding: Fill viewport using aspect ratio.
    viewer.aspectRatioMode = Qt.AspectRatioMode.KeepAspectRatio

    # Set the viewer's scroll bar behaviour.
    #   Qt.ScrollBarPolicy.ScrollBarAlwaysOff: Never show scroll bar.
    #   Qt.ScrollBarPolicy.ScrollBarAlwaysOn: Always show scroll bar.
    #   Qt.ScrollBarPolicy.ScrollBarAsNeeded: Show scroll bar only when zoomed.
    viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    viewer.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    # Allow zooming by draggin a zoom box with the left mouse button.
    # !!! This will still emit a leftMouseButtonReleased signal if no dragging occured,
    #     so you can still handle left mouse button clicks in this way.
    #     If you absolutely need to handle a left click upon press, then
    #     either disable region zooming or set it to the middle or right button.
    viewer.regionZoomButton = Qt.MouseButton.LeftButton  # set to None to disable

    # Pop end of zoom stack (double click clears zoom stack).
    viewer.zoomOutButton = Qt.MouseButton.RightButton  # set to None to disable

    # Mouse wheel zooming.
    viewer.wheelZoomFactor = 1.25  # Set to None or 1 to disable

    # Allow panning with the middle mouse button.
    viewer.panButton = Qt.MouseButton.MiddleButton  # set to None to disable

    # Load an image file to be displayed (will popup a file dialog).
    viewer.open()

    # Handle left mouse clicks with your own custom slot
    # handleLeftClick(x, y). (x, y) are image coordinates.
    # For (row, col) matrix indexing, row=y and col=x.
    # QtImageViewer also provides similar signals for
    # left/right mouse button press, release and doubleclick.
    # Here I bind the slot to leftMouseButtonReleased only because
    # the leftMouseButtonPressed signal will not be emitted due to
    # left clicks being handled by the regionZoomButton.
    viewer.leftMouseButtonReleased.connect(handleLeftClick)

    # Show the viewer and run the application.
    viewer.show()
    sys.exit(app.exec())
