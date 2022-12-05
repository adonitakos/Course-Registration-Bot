# Course Registration Bot
The following is a script I wrote for my univeristy's (SJU) course registration
portal using Python and the Selenium web-automation framework.

## About
Registering for your next semester's courses is important, and part of that is choosing classes that best fit your schedule and academic needs. However, student seats are limited and one might find themselves in a situation in which a specific class for a course has already been filled. In many cases, this is because the student did not register promptly enough (even if it is just by a matter of minutes). However, there is also the issue that many students are unable to register simply because they are preoccupied with other important matters (lectures, exams, driving, etc.). <br>

With these problems in mind, and my desire to learn automation using Python, I decided to take on this little project.

## Program
You will be prompted to enter necessary values:
 - Login
 - Semester
 - Priority Registration

along with the unique CRNs. From there, the Python script will use the functions from the Selenium framework to quickly register for those courses you specified. To do this manually could take about a few minutes, where this script will turn that into a few seconds. <br><br>
You will be given the option to either run the script immediately or have it run at at a time & date of your choosing (likely when your Priority Registration opens). Note that in order to choose a specific time and date, the program will have to be running, so I would not recommend running it more than 24 hours prior.

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

4). In a terminal and while in the directory of this folder, type: <br>
`pip install -r requirements.txt`

5). Run the code by typing: <br />
`python registration.py`

6). Follow the on-screen instructions **carefully** and you should be good to go!
