import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import re
import sys
import time


toaddr = str(sys.argv[1])
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', toaddr)

if match == None:
	print("Email non valida!!!")
	exit(0)


fromaddr = "syrusiot@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "#SYRUS-LEGO-IOT"

body = "#SYRUS-LEGO-IOT"

msg.attach(MIMEText(body, 'plain'))

filename = "SyrusLegoIOT.jpg"
attachment = open("SyrusLegoIOT.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "provaprova")
text = msg.as_string()


server.sendmail(fromaddr, toaddr, text)
server.quit()

