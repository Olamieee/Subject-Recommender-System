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

# Add this to utils.py
def send_password_reset_email(email, token):
    """Send password reset email"""
    reset_url = f"{settings.SITE_URL}/reset-password/{token}/"
    
    subject = 'Reset Your Password'
    message = f'''
    You requested to reset your password for your Student Recommendation System account.
    
    Please click the link below to reset your password:
    
    {reset_url}
    
    This link will expire in 24 hours.
    
    If you did not request a password reset, please ignore this email.
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)

def send_reset_otp_email(email, otp):
    """Send OTP for password reset"""
    subject = 'Your Password Reset OTP'
    message = f'''
    You requested to reset your password for the Student Recommendation System.
    
    Your OTP verification code is: {otp}
    
    This code will expire in 10 minutes.
    
    Please do not share this code with anyone. If you did not request this, please ignore this email.
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)