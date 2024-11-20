# email_validator_module.py

import re
from email_validator import validate_email, EmailNotValidError
from email.utils import parseaddr

def validate_email_regex(email):
    """
    Validates the email address using regular expressions.
    
    :param email: Email address to be validated.
    :return: True if valid, False otherwise.
    """
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False

def validate_email_validator(email):
    """
    Validates the email address using the email-validator library.
    
    :param email: Email address to be validated.
    :return: True if valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def validate_email_basic(email):
    """
    Validates the email address using basic parsing with the email.utils module.
    
    :param email: Email address to be validated.
    :return: True if valid, False otherwise.
    """
    name, addr = parseaddr(email)
    if '@' in addr and '.' in addr.split('@')[1]:
        return True
    return False
