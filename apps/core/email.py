import os
import json

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    Attachment, BasicMessage, EmailAddress

from apps.accounts.models import User
from apps.core.models import Event
from datetime import datetime

class Email():
    def create_email(event_id, user_id):
        print(event_id)

        event = Event.objects.get(id=event_id)
        user = User.objects.get(id=user_id)

        print('This is the event info:',
              event.event_title, event.location,
              event.start_dt, event.end_dt, event.message,
              event.invitee_emails)

        print('This is the user info:',
              user.first_name, user.last_name, user.email)

        # invitees = Email.parse_invitees('ron@aol.com; ronv@aol.com, ronald@aol.com ronaldv@aol.com')
        invitees = Email.parse_invitees(event.invitee_emails)

        # build the message
        message = BasicMessage()

        message.subject = Email.create_subject(user)
        message.html_body = Email.create_body(user, event)
        message.plain_text_body = Email.create_plain_text_body(user, event)

        message.from_email_address = EmailAddress('no-reply@pencil-it-in.com', user.first_name + ' ' + user.last_name)
        for invitee in invitees:
            message.add_to_email_address(invitee)
            print(invitee)


        # Adding Attachments
        # ==========================
        # Add Attachment directly to the list
        #attachment = Attachment("email.PNG", "image/png", "/static/images/email.PNG")
        #attachment.content_id = "pencil_it_in_logo"

        #message.add_attachment(attachment)


        # get credentials from environment variables
        server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
        api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')
        # server_id = 'SOCKETLABS_SERVER_ID'
        # api_key = 'SOCKETLABS_INJECTION_API_KEY'

        # create the client
        client = SocketLabsClient(server_id, api_key)

        # send the message
        response = client.send(message)

        print(json.dumps(response.to_json(), indent=2))
        data = json.dumps(response.to_json(), indent=2)
        if 'Success' in data:
            print('Email successfully sent.')
            return True
        else:
            print('Email failed to send.')
            return False

    def create_subject(user):
        return "You're Invited!"  + ' Pencil It In Event from "' + user.first_name + ' ' + user.last_name + '"'

    def create_body(user, event):
        return "<html><body>" \
               "<br>" \
               "<p><img src='cid:pencil_it_in_logo' /></p>" \
               "<h2>You've Been Invited!</h2>" \
               "<p>" + Email.create_invite_line(user, event) + "</p>" \
               "<p>" + Email.create_message_line(user, event) + "</p>" \
               "<p>" + Email.create_href_line(event) + "</p>" \
               "<br>" \
               "<br>" \
               "<h5>**This is a no-reply email**</h5>" \
               "<h5>Copyright 2020, Pencil-It-In</h5>" \
               "</body></html>"

    def create_plain_text_body(user, event):
        return "You've Been Invited! " + user.first_name + ' ' + user.last_name + \
               "To view the invitation, go to http://www.pencilitin.herokuapp.com/event/" + \
                      str(event.id) + '/' \


    def create_invite_line(user, event):
        return user.first_name + ' ' + user.last_name + ' has invited you to ' + \
               event.event_title + ' on ' + event.start_dt.strftime('%m/%d/%Y') + \
               ' at ' + event.start_dt.strftime('%I:%M %p') + '.' \

    def create_message_line(user, event):
        return user.first_name + ' ' + user.last_name + ' said: ' + \
               event.message

    def create_href_line(event):
        # Change URL when hosted in Heroku
        # return 'Please click <a href="http://www.pencil-it-in.com/event/' + \
        return 'Please click <a href="https://pencilitin.herokuapp.com/event/' + \
               str(event.id) + '/"><strong>HERE</strong></a> to view!' \

    def parse_invitees(invitee_emails):
        invitee_emails_fixed = invitee_emails.replace(', ', ' ').replace('; ', ' ')
        invitees_parsed = invitee_emails_fixed.split(' ')
        print(invitees_parsed)
        return invitees_parsed
