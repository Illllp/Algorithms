import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QLineEdit, QPushButton, QMessageBox

# Define the list of values
values = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8', 'value9', 'value10']

# Create the PyQt5 UI
app = QApplication(sys.argv)
window = QWidget()

# Create a layout for the UI
layout = QVBoxLayout()

# Create a label and a QLineEdit for the password
password_label = QLineEdit("Password:")
layout.addWidget(password_label)
password_entry = QLineEdit()
layout.addWidget(password_entry)

# Create a QListView and populate it with the values
listview = QListView()
listview_model = listview.model()
for value in values:
    listview_model.insertRow(0)
    index = listview_model.index(0, 0)
    listview_model.setData(index, value)
layout.addWidget(listview)

# Create a button to reverse the list and a function to reverse the list and verify the password
def reverse_list():
    password = password_entry.text()
    if password == 'mypassword':
        selected_indices = listview.selectedIndexes()
        selected_values = [listview_model.data(index) for index in selected_indices]
        for i, index in enumerate(selected_indices):
            listview_model.setData(index, selected_values[len(selected_values)-i-1])
    else:
        QMessageBox.warning(window, "Error", "Incorrect password")

reverse_button = QPushButton("Reverse List")
reverse_button.clicked.connect(reverse_list)
layout.addWidget(reverse_button)

# Set the layout for the window and display it
window.setLayout(layout)
window.show()

# Start the event loop
sys.exit(app.exec_())
