import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import email.mime.application as apmim

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart('mixed')
    msg['Subject'] = 'candlestick _tests'
    msg['From'] = 'anders@a-greve.dk'
    msg['To'] = 'mr.a.greve@gmail.com '
    pdfAttachment = apmim.MIMEApplication(ImgFileName, _subtype = "pdf")
    pdfAttachment.add_header('content-disposition', 'attachment', filename = ('utf-8', '', 'C20Stocks.pdf'))
	
    text = MIMEText("C20 Test. Mvh. Emil")
    msg.attach(text)
    #image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    #msg.attach(image)
    msg.attach(pdfAttachment)

    s = smtplib.SMTP('smtp.oister.dk', 25)
    s.ehlo()
    s.starttls()
    s.ehlo()
    #s.login('anders@a-greve.dk', 'ag1611')
    s.sendmail('anders@a-greve.dk', 'emilkeinicke@gmail.com', msg.as_string())
    s.sendmail('anders@a-greve.dk', 'halborg35@hotmail.com', msg.as_string())
    s.sendmail('anders@a-greve.dk', 'mr.a.greve@gmail.com', msg.as_string())
    s.quit()

