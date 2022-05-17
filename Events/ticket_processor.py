from unicodedata import name
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import get_object_or_404

import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import Order, OrderItem, Ticket, shippingDetails, PurchasedTicket
from .ticket_sending import bex

import secrets
import qrcode



class Ticket_processing():
    def ticket_image(self, customer):
        order = get_object_or_404(Order, customer=customer)
        details = get_object_or_404(shippingDetails, order=order)
        email = details.email
        name = details.name

        if not order.completed:
            orderitem = OrderItem.objects.filter(order=order)
            print(orderitem)
            for item in orderitem:
                quantities = item.quantity 
                type = item.ticket.id
                print(item)
                print(type)
                print('qty: ', quantities)
                bex(quantities,type,name,email)
                
                