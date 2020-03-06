#!/usr/local/bin/python3

# imports
import sqlite3

import os, sys

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_shift_schedule_planday as rssp

def main(path_db):

	def fetch_shift_schedule(path_db):

		try:
			sqlite_connection = sqlite3.connect(path_db)
			cursor = sqlite_connection.cursor()

			cursor.execute("""SELECT * FROM monthly_shift_schedule;""")
			sqlite_connection.commit()

			table_rows = cursor.fetchall()

			shifts = []

			for r in table_rows:
				shift = list(r)
				shifts.append(shift)

				print(shift)

			return shifts

		except sqlite3.Error as error:

			print("Failed to fetch values from sqlite3 monthly_shift_schedule table ERROR: ", error)
			return False

		finally:
			if (sqlite_connection):

				sqlite_connection.close()
				print("The SQLite3 connection is closed")

	monthly_shift_schedule = fetch_shift_schedule(path_db)

	return monthly_shift_schedule

if __name__ == "__main__":
	main(path_db)
