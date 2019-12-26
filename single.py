import smtplib 
import config
# list of email_id to send the mail 
try:
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(config.EMAIL_ADDRESS, config.PASSWORD)
    message = "this is the message"
    s.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message) 
    s.quit()
    print("Email Sent")
except :
    print("Email failed to send.")


