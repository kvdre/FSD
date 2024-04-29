import re

email = "firstname.lastname@university.com"
password = "Admin123"


EMAIL_PATTERN = r'\b[A-Za-z]+[.][A-Za-z]+@[A-Za-z]{10,}\.com\b'
# email pattern has to match  firstname.lastname@university.com
PASSWORD_PATTERN = r'\b[A-Z][a-z]{4,}[0-9]{3,}\b'
# password pattern has to Starts with upper-case, with a min of 5 letters, followed by 3 or more digits


