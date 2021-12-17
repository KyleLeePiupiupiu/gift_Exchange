import smtplib
from email.mime.multipart import MIMEMultipart #email內容載體
from email.mime.text import MIMEText #用於製作文字內文
from email.mime.base import MIMEBase #用於承載附檔
from email import encoders #用於附檔編碼
import datetime
import ssl

class guest:
    def __init__( self, name, email ):
        self.name = name
        self.email = email

def sendEmail( inputSubject , inputContent , inputToAddr ):
    
    # 寄件人訊息
    userName = 'noteboy123456789@gmail.com'
    userPassword = 'slspcyaqmpranzag'
    fromAddr = userName

    # 收件人訊息
    toAddrList = inputToAddr
    Subject = inputSubject
    contents = inputContent

    # 組合信件內容
    mail = MIMEMultipart()
    mail['From'] = fromAddr
    mail['To'] = ', '.join(toAddrList)
    mail['Subject'] = Subject
    mail.attach(MIMEText(contents)) # 內文加入進去 

    # 設定smtp伺服器並寄發信件   
    smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpserver.ehlo()
    smtpserver.login(userName, userPassword)
    smtpserver.sendmail(fromAddr, toAddrList, mail.as_string())
    smtpserver.quit()

def guestList( txtFile ):
    
    f = open(str(txtFile),'r')
    try:
        data = f.readlines()
        f.close()
    except:
        f.close()
    
    gList = list()
    for line in data:
        a = (line[3::].strip('\n')).split('-')
        g = guest( a[0], a[1] )
        gList.append( g )
    return gList
