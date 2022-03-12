import keyboard
import pyperclip
import pyautogui
from readTxt import readTxt
from match_sqlquery_column_name import process_dynamic_report_sourcetable
import sys


def key_board_copy_paste(str):
    '''
    Copy str to clip board by pressing ctrl-b, following up with a tab
    to end the function call
    '''

    pyperclip.copy(str)

    pyautogui.press("s") #select the box
    pyautogui.keyDown("Ctrl")
    pyautogui.press("a") #select all value in the box
    pyautogui.keyUp("Ctrl")

    pyautogui.keyDown("Ctrl")
    pyautogui.press("v") #paste
    pyautogui.keyUp("Ctrl")

    print(f"You have pasted the heading {str}")


def report_formatting(dynamic_report_column_format, dynamic_report_filesource):
    '''
    Copy each column heading to the clipboard for the SSRS column heading.
    Then process the column heading to find the corresponding external column
    id.
    Next, copy each external column id for the SSRS column value

    report_formatting: filename -> None
    '''

    heading_to_source_column = process_dynamic_report_sourcetable(
        readTxt(dynamic_report_filesource))

    report_column_headings = readTxt(dynamic_report_column_format)

    for pos in range(len(report_column_headings)):
        report_column_headings[pos] = report_column_headings[pos][0]

   # print(report_column_headings)

    report_column_value = []

    start_pasting = "f12"

    print(f"move your cursor to the first box for column heading, and press {start_pasting} key to start")
    while keyboard.read_key() != start_pasting:
        print(f"move your cursor to the first box for column heading, and press {start_pasting} key to start")

    for pos in range(len(report_column_headings)):
        if report_column_headings[pos] == ' ' or report_column_headings[pos] == '':
            # this is to drop the copied filter, sort signs they were not readable which converted to
            # an empty string when copied to txt doc
            continue
        key_board_copy_paste(report_column_headings[pos])
        if pos != len(report_column_headings) - 1:
            pyautogui.press("tab")
            print("You have pressed tab to continue")

        source_name = heading_to_source_column[report_column_headings[pos]]
        source_name = source_name.replace(" ", "_")
        source_name = source_name.replace("#", "_")
        source_name = source_name.replace("/", "_")
        source_name = "[" + source_name
        report_column_value.append(source_name)

    #print(report_column_value)

    #print(f"move your cursor to the first box for column value, and press {start_pasting} key to start")
    #while keyboard.read_key() != start_pasting:
     #   print(f"move your cursor to the first box for column value, and press {start_pasting} key to start")

    pyautogui.press("esc")
    pyautogui.press("down")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("left")
    pyautogui.keyUp("ctrl")

    for pos in range(len(report_column_value)):
        key_board_copy_paste(report_column_value[pos])
        pyautogui.press("]")
        pyautogui.press("tab")
        print("You have pressed tab to continue")

#if __name__ == '__main__':
 #   dynamic_report_column_format = "C:/Users/ZHou/Desktop/report column heading.txt"
  #  dynamic_report_filesource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale).txt"
   # report_formatting(dynamic_report_column_format, dynamic_report_filesource)
