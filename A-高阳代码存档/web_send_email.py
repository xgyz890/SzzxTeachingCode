
import smtplib
from email.mime.text import MIMEText
import numpy as np
import time
import CONFIGS_EMAIL

# 第三方 SMTP 服务
mail_host = CONFIGS_EMAIL.MAIL_HOST      
mail_user = CONFIGS_EMAIL.MAIL_USER

# 授权密码，非登录密码
mail_pass = CONFIGS_EMAIL.MAIL_PASS_GY   
           
sender = CONFIGS_EMAIL.SENDER    # 发件人邮箱
receivers = CONFIGS_EMAIL.RECEIVERS  # 接收邮件


def title_gen():
    now = int(round(time.time()*1000))
    now01 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
    res = "测试" + " " + now01  # 邮件主题，加入时间
    return res

def content_gen():
    res = "Python发送邮件测试"
    res += "\n以下内容为随机生成：\n"
    start = np.random.randint(19968,40895)
    for i in range(50):
        n = start + i
        res += "{}\t\t\t{}\t\t\t{}\n".format(n, hex(n), chr(n))
    # print(res)
    return res

def send_email(title, content):

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("邮件发送成功。")
        print("主题：", title)
        # print("内容：", content)
        
    except smtplib.SMTPException as e:
        print(e)

def main():
    email_num = CONFIGS_EMAIL.NUM_EMAILS
    print("{} emails.".format(email_num))
    for i in range(email_num):
        print("-"*10 + "Email {}".format(i+1) + "-"*10)
        # 发送邮件
        send_email(title_gen(), content_gen())
        time.sleep(np.random.uniform(2,6))
        
if __name__ == '__main__':
    main()
        
    
