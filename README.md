![PencilItIn Logo](./apps/core/static/images/logo.PNG)

# Pencil It In

## About

This is a web application built as part of the [Kickstart Coding](http://kickstartcoding.com/) Backend project curriculum.

Developed by: Jeannie Halvorson, Deepinder Kaur, Zachary Lake & Ron Villena


### Features

* Users can signup for an account and log-in

* Account holders can view their profile and edit profile information

* Account holders can create an event specifying name, location, date, time, and event notes

* Events can be sent as invites to third parties via email

* Saved events are stored on the user's profile page

* Events can be edited (name, location, date/time, event notes) 

* Events can be viewed using a static url sent in the event invite


### Who this is for

* This is for people who want a quick-access way of creating a local event and sending invites to friends. It provides a simplified user interface to make creating and viewing events easy for users and invitees. 

## Development
 
* Built with Python, Django, HTML, CSS, Bootstrap
* Runs [Socket Labs](socketlabs.com) for email API
* Uses [Datepicker-Plus](https://pypi.org/project/django-bootstrap-datepicker-plus/) from PyPI
* Deployed on [Heroku](herokuapp.com)


## Running the application

* Visit ['Pencil It In'](https://pencilitin.herokuapp.com)

### Signing Up/Editing Profile

* Click "Sign Up" if you are a new user and enter the required information on the signup page. You will be routed to your profile page upon clicking "Sign Up"

* Click "Edit Profile" to edit name and email address

### Creating an Event

* While on your profile page, click "Create an Event"

* Fill in the required fields and click "Create Your Event!" button
  * Invites are sent directly to email addresses listed in "Invitee(s) Email Addresses" field

### Viewing/Editing Events

* Events are listed on your profile page. Clicking on any specific event will direct you to the event page.

* Saved events can be edited by clicking the "Edit" link for the specific event on your profile page
