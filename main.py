from match_sqlquery_column_name import find_filter_in_sql
from sqlquery_generator import process_and_merge
from report_formatting import report_formatting

if __name__ == '__main__':
    # write sql query needed
    dynamic_report_filesource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale).txt"
    dynamic_report_sqlsource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale) sql query.txt"
    dynamic_report_report_filter = "C:/Users/ZHou/Desktop/report filter.txt"
    dynamic_report_column_format = "C:/Users/ZHou/Desktop/report column heading.txt"

    filter_name_in_sql = []
    filter_condition_in_sql = []
    report_column_value = []



    find_filter_in_sql(dynamic_report_filesource, dynamic_report_sqlsource,
                               dynamic_report_report_filter,
                          filter_name_in_sql, filter_condition_in_sql)

    print(process_and_merge(filter_name_in_sql, filter_condition_in_sql))

    report_formatting(dynamic_report_column_format, dynamic_report_filesource)






