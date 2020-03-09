#!/usr/local/bin/python3

# imports
import os, sys, re
import numpy as np

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA/misc"
sys.path.append(os.path.abspath(absolute_path))

import master_schedule as ms

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA/SQL-modules"
sys.path.append(os.path.abspath(absolute_path))

import fetch_shift_schedule_SQL as fsss

def main():

	def retrieve_schedule_dict_keys(master_schedule):

		try:
			schedule_dict_keys = []

			for i in range(len(master_schedule)):
				schedule_dict_keys.append([*master_schedule[i]])

			# ravel nD python3 list to 1d array
			schedule_dict_keys = list(np.reshape(np.asarray(schedule_dict_keys), (np.product(np.asarray(schedule_dict_keys).shape),)))
			return schedule_dict_keys

		except Exception as error:
			print("could not retrieve master_schedule dict keys ERROR ", error)
			return False

	monthly_shift_schedule = fsss.main("planday_shift_schedule_PA.db")

	master_schedule_dict_keys = retrieve_schedule_dict_keys(ms.master_schedule)

	for i in range(len(monthly_shift_schedule)):

		shift = monthly_shift_schedule[i]
		shift_group = shift[3]

		for key in master_schedule_dict_keys:
			print(key)

			print(ms.master_schedule[0]["Kannik"])
			print("\n")

if __name__ == "__main__":
	main()
