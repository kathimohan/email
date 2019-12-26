import smtplib 
import config
# list of email_id to send the mail 
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] 
for i in range(len(li)): 
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login(config.EMAIL_ADDRESS, config.PASSWORD)
		message = "Message_you_need_to_send"
		s.sendmail("config.EMAIL_ADDRESS", li[i], message) 
		s.quit() 
	except :
		print("Email failed to send.")
message = 'Subject: {}\n\n{}'.format(subject, msg)
subject = "Test subject"
msg = "Hello there, how are you today?"
