def readTxt(filesource):
    '''
    Reads in file from filesource and returns the file content as lists
    with double space to split each element.

    requires: the file for dynamic report sql query should be formatted as
    column1_name,
    column2_name,
    column3_name,
    ....(one column on each line with no prior spaces)
    '''
    data = []
    with open(filesource, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split("  ")
            data.append(line)
    return data


def read_dynamic_report_query(filesource):
    '''



    '''
    data = []
    with open(filesource, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split(",")
            for s in line:
                data.append(s.strip(" "))
    return data

print(read_dynamic_report_query("C:/Users/ZHou/Desktop/invoice detail (rental & sale) sql query.txt"))
