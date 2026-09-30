import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import openai
import json
from core.security_manager import confirm_action
from core.state import state

def send_email(command):
    return "Email drafting and sending requires manual configuration."
