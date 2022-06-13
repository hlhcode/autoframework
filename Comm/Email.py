# -*- coding = uft-8 -*-
# @Time : 2022/6/13 22:35
# @Author : 黄立慧
# @File : Email.py
# @Software : PyCharm
import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Conf.config import smtp_cfg, email_cfg

FILESIZE = 20  # 单位M，单个附件大小
FILECOUNT = 10  # 附件个数
smtp_cfg = smtp_cfg
email_cfg = email_cfg
logger = logging.getLogger("main.email")


class Email:
    def __init__(self, subject, context=None, attachment=None):
        self.subject = subject
        self.context = context
        self.attachment = attachment
        self.message = MIMEMultipart()
        self._message_init()

    def _message_init(self):
        if self.subject:
            self.message['subject'] = Header(self.subject,'utf-8')  #邮件标题
        else:
            raise ValueError("Invalid subject")

        self.message['from'] = email_cfg['sender']  # from
        self.message['to'] = email_cfg['receivers'] # to

        if self.context:
            self.message.attach(MIMEText(self.context,'html','utf-8'))  #邮件正文内容
        # 邮件附件
        if self.attachment:
            if isinstance(self.attachment,str):
                self._attach(self.attachment)
            if isinstance(self.attachment,list):
                count = 0
                for each in self.attachment:
                    if count <= FILECOUNT:
                        self._attach(each)
                        count +=1
                    else:
                        logger.warning('Attachments is more than ',FILECOUNT)
                        break

    def _attach(self, file):
        if os.path.isfile(file) and os.path.getsize(file)<=FILESIZE*1024*1024:
            attach = MIMEApplication(open(file,'rb').read())
            attach.add_header('Content-Disposition','attachment',filename=os.path.basenae(file))
            attach['Content-Type']= 'application/octet-stream'
            self.message.attach(attach)
        else:
            logger.error('The attachment is not exist or more than %sM: %s'%(FILESIZE,file))

    def send_email(self):
        s = smtplib.SMTP_SSL(smtp_cfg['host'],int(smtp_cfg['port']))
        result = True
        try:
            s.login(self.smtp_cfg['user'],self.smtp_cfg['passwd'])
            s.sendmail(self.smtp_cfg['sender'],self.smtp_cfg['receivers'],self.message.as_string())
        except smtplib.SMTPException as e:
            result = False
            logger.error('Send mail faild',exc_info=True)
        finally:
            s.close()
        return result


mail = Email('title' ,'context','WBS_1219063746359296_1654765657044.xlsx')
send = mail.send_email()
print(send)