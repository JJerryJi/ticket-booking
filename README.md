# Automatic Ticket Booking System of UCLA Badminton Court

## CONTENTS OF THIS FILE
---------------------

 * Introduction 
 * Installation
 * Instruction Handbook
 * Potential Troubleshooting Resources
 * Developer's Note


## INTRODUCTION
----------------
For badminton-lovers at UCLA, it is extremely hard to book the badminton field at John Wooden Center, UCLA Recreation. Typically, only few spots (typically two or three) are open for students at given time. Given the shear amount of UCLA students who also compete in field booking, many badminton enthusiasts are blocked from their favorite sports. I come across with a solution to help badminton lovers successfully spot the field. 

I utilize Selenium (Python) and Chrome-driver to implement auto-booking.I sincerely hope this program will help all badminton-lovers secure the field and enjoy practicing badminton with friends! 


## INSTALLATION
----------------

Selenium is a web automation tool, which enables user to create step-by-step interactions with a webpage and assess the browser's response.

In this program, Selenium is used to open Chrome's page, pinpoint HTML elements (namely "BOOK NOW" button), and async-wait until successfully booked the court.

First, Run the following command to set up selenium in your Terminal:
```
pip install selenium
```

Then, Download ChromeDriver through this link: https://sites.google.com/chromium.org/driver/

(Note: you may need to find the version of your Chrome. Either 108, 107, or earlier version)
<img width="569" alt="image" src="https://user-images.githubusercontent.com/106227061/203892710-dbad990e-1ac3-4894-a2ad-c3c16552ccba.png">



## Instruction Handbook
---------------
* Since JWC Badminton court enables all bookings in advance of exactly 24 hours, you just have to log in a few minutes earlier. For instance, if the reservation is open at 7:30 pm, Nov. 24th, you can start the server at around 7:25pm. It will automatically book the ticket (7:30pm, Nov.25th) for you.


* In the python file, you first need to mannually change your username and password of your UCLA Logon.
<img width="992" alt="image" src="https://user-images.githubusercontent.com/106227061/203894004-da07815c-110f-4a17-9c8b-bc6fc8a21e41.png">



* Once you run the program, it prompts user to type either 1 or 2 or 3, which corresponds to three badminton courts in JWC. 
<img width="1014" alt="image" src="https://user-images.githubusercontent.com/106227061/203893520-c74cefcb-c587-4291-9a4a-5aaa9b695cd1.png">


* You are good enough to run the program. The chrome-driver will auto-start, redirect to Duo Push page. You still need to enable login on your phone. Waiting for some time, the auto-driver will redirect to the website page. 


* The program is then set up to repeatedly execute "click" command until it successfully reserve the court. It will click every 10 milliseconds, which has a high success rate. If no spot is not currently available at this time (i.e. user use the program in a wrong time), it will print out error message: "No Spots Available at this time on this court." 



## Potential Troubleshooting Resources
----------------
The following websites are extremely helpful for potential troubleshooting: 

1. Selenium Webdriver: https://www.selenium.dev/documentation/webdriver/

2. Selenium-Python: https://selenium-python.readthedocs.io/



## Developer's note
----------------
The program only aims to assist badminton enthusiasts to secure badminton court. Please do not use the source code for any other purposes.

Also, if you happen to find something wrong in the code or have an optimized plan for the code, please do not hesitate to contact me!

Unoffically, the auto-ticket booking for Tennis Court at UCLA is currently underdeveloping ... 
Hope all of you enjoy this automation and enjoy badminton as well~~~



