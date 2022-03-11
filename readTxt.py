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