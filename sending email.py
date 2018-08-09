
import smtplib

email_user = 'bricksamitnikhade@gmail.com'

email_send = 'amitnikhade@outlook.com'


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'9922284567')

message = "hi there"
server.sendmail(email_user,email_send,message)
server.quit()