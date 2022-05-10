# NBCares/ParaDYM Website
## Main Features of System
The main functionality of this site for most users is a mobile-responsive calendar which hosts community support events. This site is designed so that 3rd-party organizations that have been created by the admin account can submit events to be added to the calendar. This is designed so that any 3rd party that may want to sign up must contact NB Cares to request an account. This gives NB Cares the ultimate decision-making power over which organizations are allowed to submit events, cutting down on irrelevant event submissions. Once an event has been submitted, the admin has the ability to approve or deny each individual event. Only once an event has been approved by the admin, it becomes publicly viewable. 

<br />

> Technologies Used
- HTML, CSS, Javascript (JQuery)
- Python (Django)
- Databases: SQL Lite, PostGreSQL (Easily migratable for personal use)
- Hosting: PythonAnywhere, AWS LightSail (Networking for Static IPs, RDS-like Database storage, Ubuntu Env for managing of interpreter, packages, and deployment of files)
- Packages and Software Used: **[FullCalender](https://fullcalendar.io/)** - For calender functionality. Refer to Requirements.txt of packages used.

<br />

> Funtionality
- Admins can Approve Event
- Admins can Delete Event
- Admins can Update Event
- Admins can Create Organizations
- Admins can Edit Organization Information
- Organizations can Submit Events
- Organizations can View Their Own Events
- Unsigned users can View Events

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/LEE-RUM/nbcares-498.git
$ cd nbcares-498
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/

$ # Deployment on PythonAnywhere
$ pip3.7 install pythonanywhere --user
$ pa_autoconfigure_django.py --python=3.7 https://github.com/LEE-RUM/nbcares-498 --branch=master --nuke
```

<br />

## Home Page
Showcasing the look of the Home Page

![Home](https://user-images.githubusercontent.com/79949410/167721144-d9301723-eb22-487e-8dad-f44deb6d1b7d.png)

## Login Page
Showcasing the look of the Login Page

![Login](https://user-images.githubusercontent.com/79949410/167720932-84ea8752-6564-4b96-b089-d21fb4cdf6cc.png)

