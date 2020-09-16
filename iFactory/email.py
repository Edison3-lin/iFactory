from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send(email_list):
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "%s gotna wrong"%dev_id  #郵件標題
    content["from"] = "edison3.lin@gmail.com"  #寄件者
    content["to"] = ".".join(email_list)  #"b82506001@gmail.com" #收件者
    content.attach(MIMEText("%s seems unworkable"%dev_id))  #郵件內容

    import smtplib
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("edison3.lin@gmail.com", "nhgw qgvw aszm fdmd")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
