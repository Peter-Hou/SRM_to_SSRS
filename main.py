# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import match_sqlquery_column_name as ma
import sqlquery_generator as gensql

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # write sql query needed
    dynamic_report_filesource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale).txt"
    dynamic_report_sqlsource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale) sql query.txt"
    dynamic_report_report_filter = "C:/Users/ZHou/Desktop/report filter.txt"
    dynamic_report_column_format = "C:/Users/ZHou/Desktop/report column heading.txt"

    filter_name_in_sql = []
    filter_condition_in_sql = []
    report_column_value = []

    ma.find_filter_in_sql(dynamic_report_filesource, dynamic_report_sqlsource,
                           dynamic_report_report_filter, dynamic_report_column_format,
                          filter_name_in_sql, filter_condition_in_sql, report_column_value)
    #print(filter_name_in_sql)
    #print(filter_condition_in_sql)

    #print(srm_to_sql_cond(var, condition, 'or'))

    print(gensql.process_and_merge(filter_name_in_sql, filter_condition_in_sql))

    # give me the corresponding column value for column formatting
    print("\n".join(report_column_value))




