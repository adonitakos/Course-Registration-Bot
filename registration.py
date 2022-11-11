import os
from selenium import webdriver
from selenium.webdriver.common.by import By

print("==========================================================================================")
print("|                        Adoni's Course Registration Bot                                 |")
print("==========================================================================================")

# Defining a courses list that will store user-inputed CRN numbers:
courses = []
# Getting user-inputed data that will be inserted into the site pages:
X_number = input("What is your X_Number?: ").upper()[:9]
PIN_number = input("What is your pin?: ")
semester = input("What semester are you applying for? (EXACTLY AS STATED ON UIS): ")
PRN = input("What is your Priority Registration Number (for this upcoming semester)?: ")
num_of_courses = int(input("How many courses are you going to take?: "))
print(f"You are taking {num_of_courses} courses")
for idx in range(num_of_courses):
    CRN = input('Enter the CRN number of each course: ')
    courses.append(CRN)
print("\nYou are taking these courses\n" + str(courses) + "\n")


# Initializes necessary Chrome driver for Selenium to use:
driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window

# St. John's UIS login screen:
login_url = "https://banssb.stjohns.edu/ssb/twbkwbis.P_WWWLogin"
driver.get(login_url)
userID = driver.find_element(By.ID, 'UserID')
PIN = driver.find_element(By.ID, 'PIN')
userID.send_keys(X_number)
PIN.send_keys(PIN_number)
submitButton = driver.find_element(By.XPATH, "//input[@value='Login']")
submitButton.click()

# Brings you to the URL of the latest (Fall or Spring) semester (MAYBE):
semester_url = 'https://banssb.stjohns.edu/ssb/bwskfreg.P_AltPin'
driver.get(semester_url)
term_select = driver.find_element(By.TAG_NAME, "select")
term_select.click()
#sem_select = driver.find_element(By.XPATH, "//*[text()[contains(., 'Spring 2023')]]")
sem_select = driver.find_element(By.XPATH, f"//*[text()[contains(., '{semester}')]]")
sem_select.click()
sem_Submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
sem_Submit.click()

# Inputs Priority Registration Number:
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
print() # <--- line break
courses_Submit = driver.find_element(By.XPATH, "//input[@value='Submit Changes']")
courses_Submit.click()
quit()