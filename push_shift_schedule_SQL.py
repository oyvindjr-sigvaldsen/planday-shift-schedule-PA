#!/usr/local/bin/python3

# imports
import sqlite3

import os, sys

absolute_path  = "/Users/o/Sites/github-repositories/planday-shift-schedule-PA"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_shift_schedule_planday as rssp

def main():

	def push_shift_schedule(path_db, monthly_shift_schedule):

		try:
			sqlite_connection = sqlite3.connect(path_db)
			cursor = sqlite_connection.cursor()

			cursor.execute("""DELETE FROM monthly_shift_schedule;""")

			for i in range(len(monthly_shift_schedule)):

				shift = monthly_shift_schedule[i]
				print(shift)

				cursor.execute("""INSERT OR IGNORE INTO monthly_shift_schedule VALUES(?, ?, ?, ?, ?, ?)""", (shift[0], shift[1], shift[2], shift[3], shift[4][0], shift[4][1]))
				sqlite_connection.commit()

		except sqlite3.Error as error:

			print("Failed to insert shift values into sqlite3 .db ERROR: ", error)
			return False

		finally:
			if (sqlite_connection):

				sqlite_connection.close()
				print("The SQLite3 connection is closed")

	monthly_shift_schedule = rssp.main()
	push_shift_schedule("planday_shift_schedule_PA.db", monthly_shift_schedule)

if __name__ == "__main__":
	main()
