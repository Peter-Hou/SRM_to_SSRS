import keyboard
import pyperclip

pyperclip.copy('The text to be copied to the clipboard.')

while keyboard.read_key() != "esc":
    if keyboard.read_key() == "ctrl":
        print("You pressed ctrl")

    if keyboard.is_pressed("q"):
        print("You pressed q")

keyboard.on_press_key("r", lambda _: print("You pressed r"))

def report_formatting(dynamic_report_column_format):
    '''
    Copy each column heading to the clipboard for the SSRS column heading.
    Then process the column heading to find the corresponding external column
    id.
    Next, copy each external column id for the SSRS column value

    report_formatting: filename -> None
    '''

