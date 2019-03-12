import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='derrendsouza36@gmail.com'
receiver='gchaturyar@gmail.com'
msg="Hii"
s.login(sender,'Der2000')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()
