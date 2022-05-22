from unicodedata import name
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import get_object_or_404

import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import  Ticket, PurchasedTicket

import secrets
import qrcode

def send_ticket(quantities, type, name, email):
    for quantity in range(quantities):
        ticket = Ticket.objects.filter(id=type)
        print('remmy',quantity)
        code_condition = False
        while not code_condition:
            code = secrets.token_urlsafe(5)
            purchase_code = PurchasedTicket.objects.filter(code=code)
            if not purchase_code:
                code_condition = True
                print(code)

        for tick in ticket:
            img = Image.open(tick.image_URL[1:])
            img_edit = ImageDraw.Draw(img)
            img_edit.rectangle((5,40,1000,200), fill="white")
            #font = ImageFont.truetype('\FreeMono.ttf', 100)
            
            img_edit.text((10,52), name, fill=(225,135,132))
            img_edit.text((20,52), email, fill=(225,135,132))
            img_edit.text((10,500), code, fill=(225,135,132))
            img.save("ticket.jpg")


            qr = qrcode.QRCode(
                version=1,
                box_size=5,
                border=3
            )

            data = 'https://www.fibblebox.com'
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            img.save('link.png')

            image = Image.open('ticket.jpg')

            image2 = Image.open('link.png')
            image_copy2 = image2.copy()

            image.paste(image_copy2, (10,10))

            image.save('ticket.jpg')


            receiver_email = 'chrisroyalty127@gmail.com'

            

            subject = "An email with attachment from Fibble Box"
            body = "This is an email with attachment of your coupon codes sent from Fibblebox"
            sender_email = "christianezekwem101@gmail.com"
            password = "gipymqhbsghieelq"

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "ticket.jpg"  # In same directory as script

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
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
                condition = True

                print('has sent the email')

                PurchasedTicket.objects.create(code=code, name=name)
                return condition