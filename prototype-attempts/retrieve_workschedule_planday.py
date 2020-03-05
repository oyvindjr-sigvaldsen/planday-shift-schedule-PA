#!/usr/local/bin/python3

# imports
from twill.commands import *
import twill.shell

def main():

	planday_login_URL = "https://ssk.planday.com/Login/Login.aspx?ReturnUrl=%2fPages%2fPortalPage.aspx%3fPageId%3d2713158&PageId=2713158#/dashboard/kpi-frontpage"

	#planday_dashboard_URL = "https://ssk.planday.com/Pages/PortalPage.aspx?PageId=2713158#/dashboard/kpi-frontpage"

	username = "oyvindjr.sigvaldsen@me.com"
	password = "GiorgioDamore123321"

	go(planday_login_URL)
	showforms()
	formclear("1")

	fv("1", "Username", username)
	fv("1", "Password", password)
	showforms()

	formaction(planday_login_URL, "Logon")
	submit(Logon)






if __name__ == "__main__":
	main()
