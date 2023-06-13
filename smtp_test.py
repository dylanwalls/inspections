import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = 'dylan.walls@bitprop.com'
smtp_password = 'Termsheet2022'

# Create an SMTP connection with TLS encryption
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Authenticate with SMTP AUTH
server.login(smtp_username, smtp_password)

# Send email using the authenticated connection
# Example: sending a simple text email
sender = smtp_username
recipient = 'dyl.w@hotmail.com'
subject = 'Test Email'
body = 'This is a test email.'
message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender
message['To'] = recipient
server.send_message(message)

# Close the SMTP connection
server.quit()
