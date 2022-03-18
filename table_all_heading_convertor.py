a = "DIVISION	DATE_	RSIH_CUST_N	RENTALS	SALES	DWAIVER	TOTAL	SERVICES	TAX	BILLCITY	BILLPROV	BILLPOSTAL	SHIPCITY	SHIPPROV	SHIPPOSTAL	SALESMAN	INVOICENUM	BILLNAME	SHIPNAME	OPERATOR	ID	REF"
a = a.split("\t")

ans = []
for i in a:
    if " " in i:
       i = "\"" + i + "\""
    ans.append(i + ",")

print("\n".join(ans))



