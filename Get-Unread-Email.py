mailUser = "email@website.com"
mailPass = "password"
imapHost = "website.com"

mailConn = imaplib.IMAP4_SSL(imapHost, 993)
mailConn.login(mailUser, mailPass)
mailConn.select()
result, data = mailConn.search(None, '(UNSEEN)')
if result == 'OK':
	for num in data[0].split():
		result, data = mailConn.fetch(num,'(RFC822)')
		if result == 'OK':
			email_message = email.message_from_bytes(data[0][1])
			print('From:' + email_message['From'])
			print('To:' + email_message['To'])
			print('Date:' + email_message['Date'])
			print('Subject:' + str(email_message['Subject']))
			print('Content:' + str(email_message.get_payload()[0]))
mailConn.close()
mailConn.logout()
