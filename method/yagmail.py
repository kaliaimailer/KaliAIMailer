import yagmail

yag = yagmail.SMTP('your_email@gmail.com', 'your_password')
yag.send('to@example.com', 'Subject', 'This is the body')
