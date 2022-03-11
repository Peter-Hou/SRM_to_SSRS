def readTxt(filesource):
    '''
    Reads in file from filesource and returns the file content as lists
    with double space to split each element.
    '''
    data = []
    with open(filesource, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split("  ")
            data.append(line)
    return data


def read_report_filter(reportfilter, filter_column_name, filter_condition):
    '''
    Reads in file from reportfilter and mutates filter_column_name to be
    a list of the column names that have filter on and filter_condition to
    be a list of all the conditions in the same order corresponding to
    the mutated filter_column_name

    read_report_filter: filename, (listof Str), (listof Str) -> Non
    requires: the places where there is a \t symbol in the file is to separate
                the column name with its filter condition, or at the very end of the
                entire filter
    '''
    data = []
    with open(reportfilter, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            data.append(line)

    found_tab_char = False
    condition = ""
    for char in data:
        if '\t' in char:
            if found_tab_char:
                filter_condition.append(condition)
                condition = ""
            filter_column_name.append(char[0:char.find("\t")])
            condition += char[char.find("\t") + 1:]
            found_tab_char = True
        else:
            condition += char
    filter_condition.append(condition.strip("\t"))


def process_dynamic_report_sourcetable(sourcetable):
    '''
    Returns a dictionary with keys being the column heading and the values being the
    corresponding source column id from sourcetable

    process_dynamic_source: (listof(listof Str)) -> Dict
    requires: sourcetable is formatted which the entries are in the format
                ['Column Heading\tSource Column Id\tExternal ID\tData Type']
                or ['Modify'] or ['Modify\tDelete'] or ['Calculated Columns']
    '''

    right_format = 4
    # we will only process  ['Column Heading\tSource Column Id\tExternal ID\tData Type'] which has exactly 4 \t in
    result_dic = {}
    for entry in sourcetable:
        if entry[0].count("\t") == right_format:
            split_lst = entry[0].split('\t')
            result_dic[split_lst[0]] = split_lst[1]
    return result_dic


def process_dynamic_report_sqlquery(sqlquery):
    '''
    Returns a dictionary which keys being the source column id in the dynamic report
    source table and the values are the corresponding sql query column name by processing
    data

    data: (listof(listof Str)) -> Dict
    Requires: each string in each entry in sqlquery should contain 'Sql query column AS Source Column ID'
                or 'Sql query column' which the second one refers to that Source Column ID is the same
                as the sql query column
    '''

    separator = "AS"
    result_dic = {}
    name_differs = 2  # source column id is different from the sql query column name

    for entry in sqlquery:
        str_for_process = entry[0]
        str_for_process = str_for_process.strip('\t, ')
        list_for_process = str_for_process.split(separator)
        if len(list_for_process) == name_differs:
            result_dic[list_for_process[0].strip("\" ")] = list_for_process[1].strip("\" ")
        else:
            result_dic[list_for_process[0].strip("\" ")] = list_for_process[0].strip("\" ")
    inv_result_dic = {value: key for key, value in result_dic.items()} #revert the values and keys in the dict
    return inv_result_dic

def find_filter_in_sql(dynamic_report_filesource, dynamic_report_sqlsource,
                       dynamic_report_report_filter, dynamic_report_column_format,
                       filter_name_in_sql, filter_condition_in_sql, report_column_value):
    '''
    Mutates filter_name_in_sql to be the sql query colume name needed corresponding to the
    report filter's column heading, and filter_condition_in_sql to be the required filter
    condition corresponding to each column heading. It also mutates report_column_value to
    get all the corresponding source column value for the column heading obtained from
    dynamic_report_column_format

    requires: filename, filename, filename, filename, [], [], [] -> None
    effects: mutates filter_name_in_sql and filter_condition_in_sql
    '''

    heading_to_source_column = process_dynamic_report_sourcetable(
        readTxt(dynamic_report_filesource))

    source_to_sql_column = process_dynamic_report_sqlquery(
        readTxt(dynamic_report_sqlsource))

    report_column_headings = readTxt(dynamic_report_column_format)

    read_report_filter(dynamic_report_report_filter, filter_name_in_sql, filter_condition_in_sql)

    # processing the sql query
    for pos in range(len(filter_name_in_sql)):
        source_name = heading_to_source_column[filter_name_in_sql[pos]]
        sql_query_name = source_to_sql_column[source_name]
        filter_name_in_sql[pos] = sql_query_name

    # processing for report format
    #print(report_column_headings)
    for heading in report_column_headings:
        if heading == [' ']:
            # this is to drop the copied filter, sort signs they were not readable which coverted to
            # an empty string when copied to txt doc
            continue
        source_name = heading_to_source_column[heading[0]]
        source_name = source_name.replace(" ", "_")
        source_name = source_name.replace("#", "_")
        source_name = source_name.replace("/", "_")
        source_name = "[" + source_name
        report_column_value.append(source_name)

    with open(dynamic_report_column_format, 'w') as f:
        f.write("\n".join(report_column_value))





#Tests
#dynamic_report_filesource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale).txt"
#dynamic_report_sqlsource = "C:/Users/ZHou/Desktop/invoice detail (rental & sale) sql query.txt"
# note this sql query should only include the output column, or the columns between select and from at the beginning

#a = []
#b = []
#print(read_report_filter("C:/Users/ZHou/Desktop/report filter.txt", a, b))
#print(a)
#print(b)


# print(process_dynamic_report_sourcetable(readTxt(dynamic_report_filesource)))
# print(process_dynamic_report_sqlquery(readTxt(dynamic_report_sqlsource)))