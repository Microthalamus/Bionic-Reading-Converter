import pyttsx3
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget


def convert_to_bionic():
    # Converts entered text into the bionic format
    text = input_text.toPlainText().strip()
    converted_text = ''
    
    words = text.split()
    for word in words:
        if len(word) <= 3:
            converted_text += word + " "
            output_text.insertPlainText(word + " ")
        else:
            mid_index = len(word) // 2
            converted_text += word[:mid_index] + word[mid_index:].upper() + " "
            formatted_text = ''
            for i, char in enumerate(word):
                if i < mid_index:
                    formatted_text += f"<b>{char}</b>"
                else:
                    formatted_text += char
            output_text.insertHtml(formatted_text + " ")

    output_text.moveCursor(output_text.textCursor().Start)
    output_text.ensureCursorVisible()


def text_to_speech():
    # Preforms text-to-speech using pyttsx3
    text = input_text.toPlainText().strip()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def clear_text():
    # Clears text from both input and output box
    input_text.clear()
    output_text.clear()


def copy_text():
    # Copies text so that it can be pasted
    text = output_text.toPlainText().strip()
    pyperclip.copy(text)


# Create the application
app = QApplication([])

# Create the main window
window = QMainWindow()
window.setWindowTitle("Bionic Reading Converter")

# Create the input text box
input_text = QTextEdit(window)
input_text.setPlaceholderText("Enter your text here...")
input_text.setFixedHeight(100)

# Create the convert button
convert_button = QPushButton("Convert", window)
convert_button.clicked.connect(convert_to_bionic)

# Create the text-to-speech button
tts_button = QPushButton("Text to Speech", window)
tts_button.clicked.connect(text_to_speech)

# Create the clear button
clear_button = QPushButton("Clear", window)
clear_button.clicked.connect(clear_text)

# Create the copy button
copy_button = QPushButton("Copy", window)
copy_button.clicked.connect(copy_text)

# Create the output text box
output_text = QTextEdit(window)
output_text.setReadOnly(True)
output_text.setLineWrapMode(QTextEdit.WidgetWidth)

# Sets up window layout
layout = QVBoxLayout()
layout.addWidget(input_text)
layout.addWidget(convert_button)
layout.addWidget(tts_button)
layout.addWidget(clear_button)
layout.addWidget(copy_button)
layout.addWidget(output_text)

# Set the central widget and layout
central_widget = QWidget(window)
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Show the window
window.show()

# Run the application
app.exec_()









