import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['SUbject'] = "An Email Alter"
msg['From'] = "1105894953@qq.com"
msg['To'] = "Aller_Dong@163.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()