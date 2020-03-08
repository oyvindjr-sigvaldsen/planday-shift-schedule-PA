#!/usr/local/bin/python3

# imports
import os, sys, re

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA/misc"
sys.path.append(os.path.abspath(absolute_path))

import master_schedule as ms

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA/SQL-modules"
sys.path.append(os.path.abspath(absolute_path))

import fetch_shift_schedule_SQL as fsss

def main():

	monthly_shift_schedule = fsss.main("planday_shift_schedule_PA.db")

	for i in range(len(monthly_shift_schedule)):

		shift = monthly_shift_schedule[i]
		shift_group = (re.sub(r".*-", "-", shift[4])).lstrip(" - ")
		print(shift_group)



	#print(ms.master_schedule[0]["Monday"][2]["Hundvåg"])

if __name__ == "__main__":
	main()
