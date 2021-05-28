import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'NasarKamish@gmail.com'
receiver_email_id = 'Thapelo@lifechoices.co.za,NasarKamish@gmail.com,d.e.fledermaus86@gmail.com'
password = input("Enter your password: ")
subject = input("Enter Subject: ")
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = input("Enter Body: ")
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email_id, password)
s.sendmail(sender_email_id, receiver_email_id, text)
s.quit()
