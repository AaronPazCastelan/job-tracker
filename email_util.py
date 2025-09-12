from imap_tools import MailBox
import os
from dotenv import load_dotenv

load_dotenv()

IMAP_SERVER = "imap.gmail.com"
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def fetch_app_status (email:str):
    with MailBox(IMAP_SERVER).login(EMAIL_USER, EMAIL_PASS, "Inbox") as mb:
        msgs = mb.fetch(criteria=f'FROM "{email}"', limit=1, reverse=True)
        for msg in msgs:
            return msg.text or msg.html or ""
    return None

accepted_phrases = [
    "congradulations", 
    "we are pleased to offer you", 
    "we are excited to move forward", 
    "you have been selected", 
    "we would like to invite you", 
    "offer letter", 
    "next steps", 
    "we are happy to inform you", 
    "welcome aboard", 
    "we are delighted to",
    "you have been accepted",   
    "accepted to move forward"
]
rejected_phrases = [
    "we regret to inform you", 
    "unfortunately", 
    "we will not be moving forward", 
    "we have decided to pursue other candidates", 
    "after careful consideration", 
    "your application was not selected", 
    "we will not be offering", 
    "the position has been filled", 
    "thank you for your interest", 
    "we appreciate your application, however"
]

def determine_status (body:str):
    if not body:
        return "pending"

    body_lower = body.lower()
    for phrase in accepted_phrases:
        if phrase in body_lower:
            return "accepted"
    for phrase in rejected_phrases:
        if phrase in body_lower:
            return "rejected"
    return "pending"