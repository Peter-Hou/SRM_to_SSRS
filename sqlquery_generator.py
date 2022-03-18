# Key Words
import sys

ncon = 'Not Containing'
con = 'Containing'
ne = 'Not Equal To'
eq = 'Equal To'
bg = 'Begins With'
dbg = "Doesn't Begin With"
dew = "Doesn't End With"
im = "Is Empty"
inm = "Is Not Empty"
gt = "Greater Than"
lt = "Less Than"

def general_filter(name, srm_cond, name_pos):
    '''
    Returns the sql query corresponding to the condition statement, srm_cond
    in dynamic report for the column, var. The srm_cond is for general case usually including
    and, or logic operator. If name_pos = 0, then the query starts with where. Otherwise, it
    starts with AND.

    srm_to_sql_cond: Str Str -> Str

    '''
    if srm_cond.count("or") > srm_cond.count("and"):
        logic = "or"
    else:
        logic = "and"
    split_cond = srm_cond.split(logic)
    #print(split_cond)
    result = []
    need_ltrim = input(f"Do you need ltrim for {name}, yes or no")
    while need_ltrim != "yes" and need_ltrim != "no":
        print(f"wrong data type, please input only yes or no")
        need_ltrim = input(f"Do you need ltrim for {name}, yes or no")
    for pos in range(len(split_cond)):
        if ncon in split_cond[pos]:
            value = f"NOT LIKE \'%{split_cond[pos][len(ncon) + 1:].strip()}%\'"
        elif ne in split_cond[pos]:
            value = f"<> \'{split_cond[pos][len(ne) + 1:].strip()}\'"
        elif eq in split_cond[pos]:
            value = f" = \'{split_cond[pos][len(eq) + 1:].strip()}\'"
        elif bg in split_cond[pos]:
            value = f"LIKE \'{split_cond[pos][len(bg) + 1:].strip()}%\'"
        elif dbg in split_cond[pos]:
            value = f"NOT LIKE \'{split_cond[pos][len(dbg) + 1:].strip()}%\'"
        elif con in split_cond[pos]:
            value = f"LIKE \'%{split_cond[pos][len(con) + 1:].strip()}%\'"
        elif dew in split_cond[pos]:
            value = f"NOT LIKE \'{split_cond[pos][len(dew) + 1:].strip()}%\'"
        elif im in split_cond[pos]:
            value = f"= ' '"
        elif inm in split_cond[pos]:
            value = f"<> ' '"
        elif gt in split_cond[pos]:
            value = f"> {split_cond[pos][len(gt) + 1:].strip()}"
        elif lt in split_cond[pos]:
            value = f"< {split_cond[pos][len(lt) + 1:].strip()}"
        else:
            value = "0"
            sys.exit((f"Error Error general keyword {split_cond[pos]} does not exist"))

        if need_ltrim == "yes":
            tv = "LTRIM(" + name + ") " + value
        else:
            tv = name + " " + value

        if pos == 0:
            if len(split_cond) != 1:
                tv = 'AND (' + tv + '\n ' + logic
            else:
                tv = 'AND (' + tv + ')\n '
        elif pos == len(split_cond) - 1:
            tv = tv + ')\n'
        else:
            tv = tv + '\n ' + logic
        result.append(tv)

    ans = " ".join(result)
    if name_pos == 0:
        ans = ans[4:]
        ans = "WHERE \n" + ans
    return ans


# Date Keyword

af = "After"
bf = "Before"
lm = "last month"
bt = "Between"
l = "last"
dni = "days not including today."
mtd = "Month to Date"
nit = "not including today"


def date_filter(name, cond, name_pos):
    '''
    Returns the sql query corresponding to the condition statement, srm_cond
    in dynamic report for the column, var. The srm_cond is for cases involving date
    comparision. If name_pos = 0, then the query starts with where. Otherwise, it
    starts with AND.

    srm_to_sql_cond: Str Str -> Str
    requires: name contain date or Date or DATE
    '''

    print(cond)
    if af in cond and bf in cond:
        cond = cond.split("and")
        ans = f"AND ({name} > TO_DATE(\'{cond[0][len(af) + 1:]}\', 'MM/DD/YYYY')\n AND " \
              f"{name}  < TO_DATE(\'{cond[1][len(bf) + 2:]}\', 'MM/DD/YYYY'))\n"
    elif af in cond:
        ans = f"AND ({name} > TO_DATE(\'{cond[len(af) + 1:]}\', 'MM/DD/YYYY'))\n"
    elif bf in cond:
        ans = f"AND ({name} < TO_DATE(\'{cond[len(bf) + 1:]}\', 'MM/DD/YYYY'))\n"
    elif lm in cond:
        ans = f"AND ({name} > Last_Day(ADD_MONTHS(current_date, -2))\n\
        AND {name} <= Last_Day(ADD_MONTHS(current_date, -1)))\n"
    elif bt in cond:
        cond = cond.split("And")
        ans = f"AND ({name} BETWEEN TO_DATE(\'{cond[0][len(bt) + 1:]}\', 'MM/DD/YYYY')\n AND " \
              f"TO_DATE(\'{cond[1][1:]}\', 'MM/DD/YYYY'))\n"
    elif l in cond and dni in cond:
        num = [int(n) for n in cond.split() if n.isdigit()][0]
        ans = f"AND ({name} >= TO_DATE(current_date - {num}) \n\
                AND {name} <= TO_DATE(current_date -1))\n"
    elif l in cond:
        num = [int(n) for n in cond.split() if n.isdigit()][0]
        ans = f"AND ({name} >= TO_DATE(current_date - {num}) \n\
                        AND {name} <= TO_DATE(current_date))\n"
    elif mtd in cond:
        if nit in cond:
            ans = f"AND({name} > LAST_DAY(ADD_MONTHS(current_date, -1)) AND \n\
            {name} < TO_DATE(current_date))"
        else:
            ans = f"AND({name} > LAST_DAY(ADD_MONTHS(current_date, -1)) AND \n\
                        {name} <= TO_DATE(current_date))"
    else:
        ans = "0"
        sys.exit("Error Error Date Key Word does not exist")
    if name_pos == 0:
        ans = ans[4:]
        ans = "WHERE \n" + ans
    return ans

def srm_to_sql_cond(name, cond, name_pos):
    '''
    Returns the sql query corresponding to the condition statement, srm_cond
    in dynamic report for the column, var.

    srm_to_sql_cond: Str Str -> Str
    '''

    datecases = ["Date", "date", "DATE", 'OPENED', 'opened', 'Opened']

    for date in datecases:
        if date in name:
            result = date_filter(name, cond, name_pos)
            return result

    result = general_filter(name, cond, name_pos)
    return result



def process_and_merge(filter_name_in_sql, filter_condition_in_sql):
    '''
    process the filter_condition_in_sql to be the appropriate sql query, and
    merge with filter_name_in_sql one by one and form a whole sql query. Then
    return this resulting sql query

    process_and_merge: (listof Str) (listof Str) -> Str
    '''

    if len(filter_name_in_sql) != len(filter_condition_in_sql):
        sys.exit("Error Error name and condition do not have same length")
    name_pos = 0
    final_sql_query = []
    for (name, cond) in zip(filter_name_in_sql, filter_condition_in_sql):
        final_sql_query.append(srm_to_sql_cond(name, cond, name_pos))
        name_pos += 1
    #print(final_sql_query)
    final_sql_query = "".join(final_sql_query)
    return final_sql_query

