#!/usr/local/bin/python3

# imports
import sqlite3

def main():

	def push_shift_schedule(path_db):

		try:
			sqlite_connection = sqlite3.connect(path_db)
			cursor = sqlite_connection.cursor()

			#cursor.execute("""CREATE TABLE monthly_shift_schedule
			#					VALUES([date] text, [department] text, [group] text, [function] text, [time_frame] text);""")

			cursor.execute("""INSERT INTO monthly_shift_schedule""")

		except sqlite3.Error as error:

			print("Failed to insert shift values into sqlite3 .db")
			return False

		finally:
			if (sqlite_connection):
				sqlite_connection.close()
				print("The SQLite3 connection is closed")

	#push_shift_schedule("../shift_schedule_PA.db")

if __name__ == "__main__":
	main()
