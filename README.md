# Data munging on NZ covid stats

I wanted to know two things about the NZ COVID counts, which are released by the government at

  https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases/covid-19-current-cases-details#download

Here's the result of my data analysis as of April 9.

1. How many days between arrival date and report date? To calculate this, I just added a calculation to the XLS:

>     A2-MAX(I2, H2)

and did standard analyses on the numbers. I manually fixed cases where the date reported was before the date arrived;
in those cases it looks like the month was incorrectly entered.

> count	487
> mean	7.04
> median	6
> mode	4
> max	26
> stdev	4.2
> days > 14	26
> % days > 14	5.34%

2. How many of the new cases per day are made-in-NZ? The government used to report international vs close contacts vs community transmission, but now it only reports international-or-not. But that's still enough data to figure out how many cases per day are not international.

The spreadsheet also includes percentages. The Python code `perday.py` calculates all of this given a .csv that merges the confirmed and probable sheets of the government spreadsheet. Spreadsheet:

  https://docs.google.com/spreadsheets/d/1PVFcO0du5zNqrKoxmA9SzzfKSKrewUZw/edit#gid=319944801

The % new non-international cases has never been above 12% since March 12, and is near 5% now.