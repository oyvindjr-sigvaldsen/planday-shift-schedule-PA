#!/usr/local/bin/python3

# imports
from selenium import webdriver
import numpy as np

def main():

	planday_admin_URL = "https://ssk.planday.com/Login/Login.aspx?ReturnUrl=%2fPages%2fPortalPage.aspx%3fPageId%3d2713158&PageId=2713158#/dashboard/kpi-frontpage"
	planday_schedule_URL = "https://ssk.planday.com/Pages/PortalPage.aspx?PageId=82487&nav=menu"
	username = ""
	password = ""

	driver = webdriver.Chrome(executable_path="webdrivers/chromedriver_v80")
	driver.get(planday_schedule_URL)

	username_field = driver.find_element_by_id("Username")
	password_field = driver.find_element_by_id("Password")

	username_field.send_keys(username)
	password_field.send_keys(password)

	driver.find_element_by_id("submitButton").click()

	# find shift schedule
	monthly_shifts = driver.find_elements_by_tag_name("tr")

	for i in monthly_shifts:

		print(i.text)
		#row_elements = i.find_elements_by_tag_name("td")
		#print(row_elements[4].text)
		#print("\n")





if __name__ == "__main__":
	main()
