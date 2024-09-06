import sys
import random


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, \
    QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6 import QtGui

from stores import data
from lib.signals import derived

def increment():
    data.jobs.value += 1


def decrement():
    data.jobs.value -= 1


def add_experiment():
    number = random.randrange(1, 10)
    data.experiments.value += [f"Experiment: {number}"]


def update_list(q_list: QListWidget):
    q_list.clear()
    for item in data.experiments.value:
        q_list.addItem(QListWidgetItem(item))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Application")
        self._center_window()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):

        # Add and Subtract
        add_button = QPushButton("Increment")
        subtract_button = QPushButton("Decrement")

        add_button.clicked.connect(increment)
        subtract_button.clicked.connect(decrement)

        # Reactive Labels
        label = QLabel()
        data.jobs += lambda: label.setText(f"Job Count: {data.jobs.value}")

        double = derived(lambda: data.jobs.value * 2)

        double_label = QLabel()
        double += lambda: double_label.setText(f"Job Count (Doubled): {double.value}")

        # Experiment stuff
        experiment_button = QPushButton("Add Experiment")
        experiment_button.clicked.connect(add_experiment)

        experiment_list = QListWidget()
        data.experiments += lambda: update_list(experiment_list)

        layout = QVBoxLayout(self.central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(add_button)
        layout.addWidget(subtract_button)
        layout.addWidget(label)
        layout.addWidget(double_label)
        layout.addWidget(experiment_button)
        layout.addWidget(experiment_list)
        self.setLayout(layout)

    def _center_window(self):
        desktop_dimensions = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        self.resize(desktop_dimensions.width(), desktop_dimensions.height())

        qt_rectangle = self.frameGeometry()
        center_point = desktop_dimensions.center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
