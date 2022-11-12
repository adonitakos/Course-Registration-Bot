# Course Registration Bot
The following is a script I wrote for my univeristy's (SJU) course registration
portal using Python and the Selenium web framework.

## About
Registering for your next semester's courses is important, and part of that is choosing classes that best fit your schedule and academic needs. However, student seats are limited and one might find themselves in a situation in which a specific class for a course has already been filled; and in many cases, this is because the student did not register promptly enough (even if it is just by a matter of minutes). <br>
<br>
That's where this Python script comes in! With it, you will be prompted to enter necessary values:
 - Login
 - Semester
 - Priority Registration

Along with the unique CRNs, and then from there, the Python script will use the Selenium framework to quickly register for those courses you specified. To do this manually could take about a few minutes, where this script will turn that into a few seconds

## Instructions
0). Before using this, PLAN! Go through the course catalog, see what courses you're planning to take, and write down the CRN numbers.

1). Make sure you have **Python** and **pip** installed. You can grab the latest version from
their official download page: <br />
https://www.python.org/downloads/

2). For this program, you will need to use the **Google Chrome** browser. If you do not already have that installed, navigate to their official page to download the latest version (for Windows, macOS, or Linux): <br />
https://www.google.com/chrome/dr/download/ <br />
You always want to make sure your Chrome browswer is on the latest up-to-date version.

3). In order to use this program on your computer, open up a terminal and type: <br>
`git clone https://github.com/adonitakos/Course-Registration-Bot.git` <br />
If you do not have git installed, you can either download it from here: https://git-scm.com/downloads <br />
Or you can just click the green Code button, Download ZIP, and then extract the folder.

4). Download the latest driver from **ChromeDriver** site (for your given operating system) and extract the .exe file into this directory: <br />
https://chromedriver.chromium.org/downloads
I have provided a Windows compatible driver for Chrome version 107, and in the future I will try to keep this up-to-date (however, there is no guarantee)

5). In a terminal and while in the directory of this folder, type: <br>
`python registration.py`

6). Follow the on-screen instructions **carefully** and you should be good to go!
