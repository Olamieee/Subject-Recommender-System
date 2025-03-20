from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(email, otp):
    """Send OTP verification email"""
    subject = 'Your OTP Verification Code'
    message = f'''
    Thank you for registering with the Student Recommendation System.
    
    Your OTP verification code is: {otp}
    
    This code will expire in 10 minutes.
    
    Please do not share this code with anyone.
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)