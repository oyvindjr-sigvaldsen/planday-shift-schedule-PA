#!/usr/local/bin/python3

# imports
from selenium import webdriver
import numpy as np
import sqlite3, re, datetime, calendar

def main():

	def retrieve_login_credentials(path_db):

		try:
			sqlite_connection = sqlite3.connect(path_db)
			cursor = sqlite_connection.cursor()

			cursor.execute("SELECT * FROM planday_login_credentials;")
			credentials = cursor.fetchall()
			sqlite_connection.commit()

			return credentials[0][0], credentials[0][1]

		except sqlite3.Error as error:

			print("Failed to fetch https://www.planday.com login credentials from sqlite3 .db ERROR: ", error)
			return False, error

		finally:
			if (sqlite_connection):
				sqlite_connection.close()
				print("The SQLite3 connection is closed")

	def login_planday(driver, planday_schedule_URL, username, password):

		try:

			driver.get(planday_schedule_URL)
			username_field = driver.find_element_by_id("Username").send_keys(username)
			password_field = driver.find_element_by_id("Password").send_keys(password)

			driver.find_element_by_id("submitButton").click()
			return True

		except Exception as error:

			print("Error: ", repr(error))
			return False

	username, password = retrieve_login_credentials("planday_shift_schedule_PA.db")
	planday_schedule_URL = "https://ssk.planday.com/Pages/PortalPage.aspx?PageId=82487&nav=menu"

	#chrome_options = Options()
	#chrome_options.add_experimental_option("detach", True)

	driver = webdriver.Chrome(executable_path="webdrivers/chromedriver_v80")
	login_planday(driver, planday_schedule_URL, username, password)

	def retrieve_shift_schedule(driver):

		shifts = []

		rg_rows = driver.find_elements_by_class_name("rgRow")
		rg_alt_rows = driver.find_elements_by_class_name("rgAltRow")

		# iterate over both rg_rows && rg_alt_rows concurrently
		for row_elements in zip(rg_rows, rg_alt_rows):

			# iterate over tuple list()
			for row_element in row_elements:

				child_elements = row_element.find_elements_by_tag_name("td")


				shift_date = child_elements[0].text
				shift_department = child_elements[1].text
				shift_function = child_elements[3].text
				shift_time_frame = child_elements[4].text

				shift_group = (re.sub(r".*-", "-", shift_function)).lstrip(" - ")

				shift_information = [
										re.findall(r'\d+', shift_date), # extract all int() from string var
										shift_department.replace("Avd.", ""),
										shift_group,
										(shift_function.replace(shift_group, "")).replace("-", ""),
										re.findall(r'\d+', shift_time_frame) # seperate time frame into ["00", "30"] -> ["hr", "min"]
									]

				shifts.append(shift_information)

		return shifts

	def assimilate_retrieved_info(shift_schedule):

		for i in range(len(shift_schedule)):

			shift = shift_schedule[i]

			# modify shift_time_frame from [hr, min] -> [0000]
			shift_time_frame = [
								shift[4][0] + shift[4][1],
								shift[4][2] + shift[4][3]
								]

			# assimilate scraped information
			now = datetime.datetime.today()
			shift_date = datetime.datetime(
												int(shift[0][1]),
												now.month,
												int(shift[0][0])
											)

			shift_day = calendar.day_name[shift_date.weekday()]

			# replace existing records with assimilated records
			shift_schedule[i][0] = shift_date
			shift_schedule[i][4] = shift_time_frame
			shift_schedule[i].insert(0, shift_day)

		return shift_schedule

	shift_schedule = retrieve_shift_schedule(driver)
	monthly_shift_schedule = assimilate_retrieved_info(shift_schedule)

	return monthly_shift_schedule

if __name__ == "__main__":
	main()
