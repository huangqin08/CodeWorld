import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(file_new):
    # 邮件服务器
    smtpserver = 'smtp.qq.com'
    # 发件人
    sender = '549418724@qq.com'
    # 发件人授权码
    sender_AuthCode = 'lkgvptfualbkbccc'
    # 收件人
    receiver = ['570219494@qq.com', 'huangqin@guojingold.com']

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    #   邮件主题
    subject = 'Python test send email--来自老婆的信'
    # content='这是BPM系统自动化测试报告'

    # 邮件正文
    body = MIMEText(mail_body, 'html', 'utf-8')

    # 邮件对象
    email = MIMEMultipart()
    email['Subject'] = Header(subject, 'utf-8').encode()
    email['From'] = sender
    email['To'] = ','.join(receiver)
    email['date'] = time.strftime('%Y-%m-%d %H_%M_%S')
    email.attach(body)

    # 附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="test_report.html"'
    # print(att)
    email.attach(att)

    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(sender, sender_AuthCode)
        smtp.sendmail(sender, receiver, email.as_string())
        print("send success")
    except Exception as e:
        print('send failed', e)
    smtp.quit()

if __name__ == '__main__':
    file_new = './report/report.html'
    send_email(file_new)
