import pyautogui
import keyboard
import PySimpleGUI as sg

# Store previous mouse position
previous_position = pyautogui.position()

# Function to get coordinates
def get_coordinates():
    global previous_position
    print("Move the mouse to the desired position and press 'Enter'...")
    input()  # Wait for user to press Enter
    x, y = pyautogui.position()
    previous_position = (x, y)
    print(f"Coordinates saved: ({x}, {y})")

# Function to paste at coordinates
def paste_at_coordinates(coordinates):
    pyautogui.click(coordinates)
    pyautogui.hotkey('command', 'v')

# Define the layout for the GUI
layout = [
    [sg.Text('Press the buttons to set coordinates for pasting:')],
    [sg.Button('Set Coordinates A', key='COORD_A'), sg.Button('Set Coordinates B', key='COORD_B')],
    [sg.Text('Press the buttons to paste at the saved coordinates:')],
    [sg.Button('Paste at Coordinates A', key='PASTE_A'), sg.Button('Paste at Coordinates B', key='PASTE_B')],
    [sg.Button('Exit')]
]

# Create the GUI window
window = sg.Window('PyAutoGUI Script with GUI', layout)

# Event loop to handle GUI events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'COORD_A':
        get_coordinates()
    elif event == 'COORD_B':
        get_coordinates()
    elif event == 'PASTE_A':
        paste_at_coordinates(previous_position)
    elif event == 'PASTE_B':
        paste_at_coordinates(previous_position)

window.close()
