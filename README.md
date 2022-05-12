# NBCares/ParaDYM Website
Authors: ChenYang Lin, Michael Bienasz, Jonathan Kryzanski, Lirim Mehmeti
## Main Features of System
The main functionality of this site for most users is a mobile-responsive calendar which hosts community support events. This site is designed so that 3rd-party organizations that have been created by the admin account can submit events to be added to the calendar. This is designed so that any 3rd party that may want to sign up must contact NB Cares to request an account. This gives NB Cares the ultimate decision-making power over which organizations are allowed to submit events, cutting down on irrelevant event submissions. Once an event has been submitted, the admin has the ability to approve or deny each individual event. Only once an event has been approved by the admin, it becomes publicly viewable. 

<br />

> Technologies Used
- HTML, CSS, Javascript (JQuery)
- Python (Django)
- Databases: SQL Lite, PostGreSQL (Easily migratable for personal use)
- Hosting: PythonAnywhere
- Packages and Software Used: **[FullCalender](https://fullcalendar.io/)** - For calender functionality. Refer to Requirements.txt of packages used.

<br />

> Funtionality
- Admin can approve, delete and update events
- Admin can create organizations
- Admin can edit organization information
- Admin can delete resources
- Admin can create, edit and delete blog posts
- Admin can send email notifications to all registered users on the day of the event
- Organizations can submit events
- Organizations can view their own events
- Organizations can add resources
- Unsigned users can view events
- Unsigned users can view the blog page
- Unsigned users can view the resources page
- Residents can register for events
- Residents can add events to their google calendar
- Residents can request a service
- Residents can view their registered events on their profile page

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

![Home](https://user-images.githubusercontent.com/79949410/167721144-d9301723-eb22-487e-8dad-f44deb6d1b7d.png)

## Login Page

![Login](https://user-images.githubusercontent.com/79949410/167720932-84ea8752-6564-4b96-b089-d21fb4cdf6cc.png)

## Calendar Page

![calendar-view](https://user-images.githubusercontent.com/79949410/168122388-5eacac26-195e-4182-9526-a9d0d9bf3eed.png)

## Resources Page

![resource-view](https://user-images.githubusercontent.com/79949410/168122856-aca4d229-9055-4182-9276-f3a0ace63c58.png)

## Blog Page

![blog-view](https://user-images.githubusercontent.com/79949410/168123585-4b73f3f5-aef0-48d7-99d0-130211732498.png)

## Tutorials page

![how-to-view](https://user-images.githubusercontent.com/79949410/168123914-223cc7a9-84f3-498a-b521-3992cc494734.png)

## Spanish View

![spanish-view](https://user-images.githubusercontent.com/79949410/168124074-f33abd26-2f74-4101-a0c7-9a4579c564d3.png)

## Admin Panel

![panel](https://user-images.githubusercontent.com/79949410/168128268-c0316067-76b9-4bb5-b6ee-64a6ced3dc6d.png)


