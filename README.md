# Overview

This is a dynamic web application using Django (Python). The program functions as a Event Booking System and allows users to:
* View events
* Register for events
* View a confirmation page with detail

To run the project, open the terminal (within the repository folder), and start the server using
`python manage.py runserver`
then open a browser and go to
`http://127.0.0.1:8000/`
This will load the events list home page.

[Software Demo Video](https://www.youtube.com/watch?v=-3roCThTi9A)

# Web Pages

I included 3 HTML web pages: The event list home page, a registration page, and a confirmation page.

The event list home page includes a list of events and a register button for each. This button will take you to the registration page which is dynamically created for that specific event. After the name and email is inputed and the registration button is pressed, you are taken to the confirmation page that includes details dynamically gathered from the event and user info.

# Development Environment
* VSCode
* Python 3.14.2
* Djagno 6.0.2
* HTML
* Git / GitHub
# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/6.0/)
* [W3 Schools](https://www.w3schools.com/)

# Future Work
* Make the pages more visually appealing
* Add a log-in option, so the user needs to be logged in in order to register
* Allow users to upload their own events