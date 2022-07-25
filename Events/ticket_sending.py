from re import template
from unicodedata import category, name
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import get_object_or_404

import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import  Ticket, PurchasedTicket, Event

import secrets
import qrcode

def send_ticket(quantities, id, name, email):
    for quantity in range(quantities):

        ticket = Ticket.objects.filter(id=id)
        code_condition = False
        #let's create a ticket code and check if exist
        #if it exist then we create another code and check
        #once it dosen't exist then we move to the next line of code
        # O complexity is O(N) there would take n amount of time to achive it 

        while not code_condition:

            code = secrets.token_urlsafe(10)
            purchase_code = PurchasedTicket.objects.filter(code=code)
            if not purchase_code:
                code_condition = True
        #then this code value we would use to design the ticket

        for tick in ticket:

            event_name = Event.objects.get(name=tick.event)
            #event_name_upper  = event_name.upper()
            event_name_string = event_name.name
            date = event_name.date
            type_ticket = tick.type
            cost = tick.cost

            img = Image.open('ticket/template/template.jpg')
            img_edit = ImageDraw.Draw(img)
            mini_font= ImageFont.truetype('data-latin.ttf', 15)
            my_font= ImageFont.truetype('data-latin.ttf', 30)
            my_font1= ImageFont.truetype('data-latin.ttf', 40)
            my_font2= ImageFont.truetype('data-latin.ttf', 60)
            img_edit.text((500,50), event_name_string, font=my_font2, fill=(0, 0, 0))
            img_edit.text((80,150), 'Name', font=my_font1, fill=(70, 70, 70))
            img_edit.text((80,200), name, font=my_font1, fill=(0, 0, 0))
            img_edit.text((80,250), 'Email',font=my_font1, fill=(70, 70, 70))
            img_edit.text((80,300), email,font=my_font1, fill=(0, 0, 0))
            img_edit.text((500,150), 'Category',font=my_font1, fill=(70, 70, 70))
            img_edit.text((510,200), type_ticket,font=my_font1, fill=(0, 0, 0))
            img_edit.text((1050,550), code,font=my_font1, fill=(0, 0, 0))
            img_edit.text((700,600), 'fibblebox.com',font=mini_font, fill=(70, 70, 70))
            img_edit.text((80,500), f'Date of event: {date}',font=my_font, fill=(0, 0, 0))
            img.save("ticket/ticket.jpg")


            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=3
            )

            data = f'https://www.fibblebox.com/events/check-ticket/{code}'
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            img.save('ticket/link.png')

            image = Image.open('ticket/ticket.jpg')

            image2 = Image.open('ticket/link.png')
            image_copy2 = image2.copy()

            image.paste(image_copy2, (1000,100))
            image3 = Image.open('static/logos/fibble_box_logo.png')

            logo_image = image3.resize((200,200))
            logo_copy = logo_image.copy()

            image.paste(logo_copy,(650,250))
            image.save('ticket/ticket.jpg')


            receiver_email = email

            subject = "An email with attachment from Fibble Box"
            body = "This is an email with attachment of your ticket purchased from Fibblebox"
            sender_email = 'fibblebox@gmail.com'
            password = 'pnzygxgtykewwfow'

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "ticket/ticket.jpg"  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            #get the event for the ticket
            event_name = Event.objects.get(name=tick.event)
            type_ticket = tick.type
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
                condition = True

                print('has sent the email')

                PurchasedTicket.objects.create(code=code, name=name,cost=cost, event=event_name, type=type_ticket)
                return condition