# Calculate number of new non-international cases per day based on NZ COVID data.
# Author: Patrick Lam
# Released to public domain

import csv
from datetime import date, datetime

count = {}
count_intl = {}
running_total = 0

with open ('covid-8-apr.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        report = row['Date of report']
        r_date_obj = datetime.strptime(report, '%d/%m/%Y')
        ro = date.toordinal(r_date_obj)
        intl = row["International travel"]

        count[ro] = count.get(ro, 0) + 1
        if intl == "Yes":
            count_intl[ro] = count_intl.get(ro, 0) + 1
        else:
            count_intl[ro] = count_intl.get(ro, 0)

print ('"Date of report","Cumulative","New cases","% new","New international cases","New non-international cases","% new non-intl cases"')
cum = 0
alldays = sorted(list(count.keys()))
for day in alldays:
    cum += count[day]
    print ("{},{},{},{:.2%},{},{},{:.2%}".format(datetime.fromordinal(day).strftime("%m/%d/%Y"), cum, count[day], count[day]/cum, count_intl[day], count[day]-count_intl[day], (count[day]-count_intl[day])/cum))
