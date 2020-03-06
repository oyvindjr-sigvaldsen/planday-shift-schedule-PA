#!/usr/local/bin/python3

# imports
from selenium import webdriver
import numpy as np
import sqlite3, re

def main():

	def retrieve_login_credentials(path_db):

		try:
			sqlite_connection = sqlite3.connect(path_db)
			cursor = sqlite_connection.cursor()

			cursor.execute("SELECT * FROM planday_login_credentials")
			credentials = cursor.fetchall()
			sqlite_connection.commit()

			return credentials[0][0], credentials[0][1]

		except sqlite3.Error as error:

			print("Failed to fetch https://www.planday.com login credentials from sqlite3 .db")
			return False

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

	username, password = retrieve_login_credentials("../shift_schedule_PA.db")
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
				shift_group = child_elements[2].text
				shift_function = child_elements[3].text
				shift_time_frame = child_elements[4].text

				shift_information = [
										re.findall(r'\d+', shift_date), # extract all int() from string var
										shift_department,
										shift_group,
										shift_function,
										shift_time_frame
									]

				shifts.append(shift_information)

		return shifts

	#monthly_shift_schedule = retrieve_shift_schedule(driver)
	#print(monthly_shift_schedule)

	months = driver.find_elements_by_class_name("nav_blue_month")
	print(len(months))

	months[1].click()

	anchor = driver.find_elements_by_tag_name("p")
	for a in anchor:
		print(a)


if __name__ == "__main__":
	main()
