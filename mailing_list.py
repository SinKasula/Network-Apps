# Import smtplib for the actual sending function
import smtplib
# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
sender_emailaddress = "xyx@gmail.com" # sender email
sender_password = '###'  # sender password - to be read from a text file
to_list = [] # mailing list - in a list of strings
# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Happy Diwali'
family = to_list
msg['From'] = sender_emailaddress
msg['To'] = ', '.join(family)
msg.preamble = 'Diwali'

# Assume we know that the image files are all in PNG format
"""for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    with open(file, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)"""

# Send the email via our own SMTP server.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(sender_emailaddress, sender_password)
s.sendmail(sender_emailaddress, family, msg.as_string())
s.quit()