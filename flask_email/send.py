import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user='saikrishnakerla@gmail.com'
email_send='saikrishnakerla@gmail.com'
subject='Python!'
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['subject']=subject
body='Hi there,sending this email from Python!'
msg.attach(MIMEText(body,'Plain'))
filename='Document.txt'
attachment=open(filename,'rb')

part=MIMEBase('application','octset-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Context_Disposition',"attachment:filename="+filename)
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'XXXXXXXXXXXXXX')
server.sendmail(email_user,email_send,text)
server.quit()
