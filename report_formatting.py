import keyboard
import pyperclip
from readTxt import readTxt
from match_sqlquery_column_name import process_dynamic_report_sourcetable
import sys


def key_board_copy_paste(str, pos, heading_pos):
    '''
    Copy str to clip board by pressing ctrl-b, following up with a tab
    to end the function call
    '''

    while keyboard.read_key() != "ctrl":
        print("press ctrl please")
    pyperclip.copy(str)
    while keyboard.read_key() != "v":
        print("press ctrl-v to paste the heading")
    if heading_pos != pos:
        sys.exit("Error in pasting, please check")
    while keyboard.read_key() != "tab":
        print("press tab to continue")
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

    print(report_column_headings)

    report_column_value = []

    heading_pos = 0
    for pos in range(len(report_column_headings)):
        if report_column_headings[pos] == ' ' or report_column_headings[pos] == '':
            # this is to drop the copied filter, sort signs they were not readable which coverted to
            # an empty string when copied to txt doc
            heading_pos += 1
            continue
        key_board_copy_paste(report_column_headings[pos], pos, heading_pos)
        heading_pos += 1

        source_name = heading_to_source_column[report_column_headings[pos]]
        source_name = source_name.replace(" ", "_")
        source_name = source_name.replace("#", "_")
        source_name = source_name.replace("/", "_")
        source_name = "[" + source_name
        report_column_value.append(source_name)

    print(report_column_value)
    heading_pos = 0
    for pos in range(len(report_column_value)):
        key_board_copy_paste(report_column_value[pos], pos, heading_pos)
        heading_pos += 1

#if __name__ == '__main__':
 #   dynamic_report_column_format = "C:/Users/ZHou/Desktop/report column heading.txt"
  #  dynamic_report_filesource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale).txt"
   # report_formatting(dynamic_report_column_format, dynamic_report_filesource)
