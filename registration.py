#import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from datetime import datetime
import pause

def WelcomeBanner():
    print("==========================================================================================")
    print("|                        Adoni's Course Registration Bot                                 |")
    print("==========================================================================================")

def NowOrLater():
    print("Would you like to run this script now or at a specified time?")
    print("(1) Now \n(2) Choose a Time")
    choice = int(input())
    if choice == 1:
        Register()
    if choice == 2:
        print("\nChoose a time and date to register (perphaps according to your PRN)\n")
    
        global year, month, day, hour, minute
        print("Please specify the month, day, and time like your registration opens up")
        year = '2022'
        month = input("month (e.g. 5 for May): ")
        day = input("day: ")
        hour = input("hour (e.g.: 16 for 4:00 PM): ")
        minute = input("minute: ")
        print("\nPending script execution...\nPress CTRL + C to cancel. \nOtherwise, do NOT close the console window (leave it running)...")
        pause.until(datetime(int(year), int(month), int(day), int(hour), int(minute), 00))
        Register()

def Register():
    print("\nRegistering for courses...\n")
    
    # Initializes necessary Chrome driver for Selenium to use:
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.maximize_window
    
    # St. John's UIS login page:
    login_url = "https://banssb.stjohns.edu/ssb/twbkwbis.P_WWWLogin"
    driver.get(login_url)
    userID = driver.find_element(By.ID, 'UserID')
    PIN = driver.find_element(By.ID, 'PIN')
    userID.send_keys(X_number)
    PIN.send_keys(PIN_number)
    submitButton = driver.find_element(By.XPATH, "//input[@value='Login']")
    submitButton.click()

    # Semester selection page:
    semester_url = 'https://banssb.stjohns.edu/ssb/bwskfreg.P_AltPin'
    driver.get(semester_url)
    term_select = driver.find_element(By.TAG_NAME, "select")
    term_select.click()
    sem_select = driver.find_element(By.XPATH, f"//*[text()[contains(., '{semester}')]]")
    sem_select.click()
    sem_Submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
    sem_Submit.click()

    # Priority Registration Number page:
    prn_form = driver.find_element(By.ID, 'apin_id')
    prn_form.send_keys(PRN)
    prn_submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    prn_submit.click()

    # Places user-defined CRN numbers into corresponding crnid cells:
    crn_ids = ['crn_id1', 'crn_id2', 'crn_id3', 'crn_id4', 'crn_id5', 'crn_id6','crn_id7','crn_id8']
    print("\nThe CRN bars will be filled with the following CRN numbers")
    for i in range (len(courses)):
            print(f"{crn_ids[i]}: {courses[i]}")
            driver.find_element(By.ID, crn_ids[i]).send_keys(courses[i])
    print("\n(I don't know what's up with these outputs below :/ )\nPRESS CTRL + C if you wish to exit the program\n\n")
    courses_Submit = driver.find_element(By.XPATH, "//input[@value='Submit Changes']")
    courses_Submit.click()
    quit() # <--- will close the window when the script is finished executing (which I don't like, but it's there)
    
def main():
    WelcomeBanner()
    global courses, X_number, PIN_number, semester, PRN, num_of_courses
    # Defining a courses list that will store user-inputed CRN numbers:
    courses = []
    # Getting user-inputed data that will be inserted into the site pages:
    X_number = input("What is your X_Number?: ").upper()[:9]
    PIN_number = getpass("What is your pin?: ")
    semester = input("What semester are you applying for? (EXACTLY AS STATED ON UIS): ")
    PRN = input("What is your Priority Registration Number (for this upcoming semester)?: ")
    num_of_courses = int(input("How many courses are you going to take?: "))
    print(f"You are taking {num_of_courses} courses")
    for idx in range(num_of_courses):
        CRN = input('Enter the CRN number of each course: ')
        courses.append(CRN)
    print("\nYou are taking these courses\n" + str(courses) + "\n")

    NowOrLater()

if __name__ == '__main__':
    main()
