# views.py (in one of your apps)

from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent from a Django application.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['recipient@example.com',]  # Replace with the recipient's email address
    send_mail(subject, message, email_from, recipient_list)
    
    return HttpResponse("Email sent successfully!")
