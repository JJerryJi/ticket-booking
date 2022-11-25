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

Run the following command to set up selenium in your Terminal:

  pip install selenium


