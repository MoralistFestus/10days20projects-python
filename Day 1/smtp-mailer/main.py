import smtplib
from email import encoders
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 465)

server = ehlo()

# server.login('moralistfestus@gmail.com', 'xxxxxx')

# Create a text file to store password

with open('tmp/password.txt', 'r') as f:
	password = f.read()
server.login('moralistfestus@gmail.com', password)

# message body

msg = MIMEMultipart()
msg['From'] = 'Moralist Festus'
msg['To'] = 'festusoluwatobi294@gmail.com'
msg['Subject'] = 'Just a SMTP mail'

with open('tmp/message.txt', 'r') as f:
	message = f.read()

msg.attach(MIMEText(message, 'plain'))

# attach image

filename = 'tmp/coding.jpg'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('moralistfestus@gmail.com', 'festusoluwatobi294@gmail.com', text)

