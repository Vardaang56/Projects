import random
import string
import smtplib

def OTP(Lenth=6):
    Character = string.digits
    otp = "".join(random.choice(Character) for _ in range(Lenth))
    return otp


# Sender details
sender_email = "vardaan.r12@gmail.com"
app_password = "bbzofagnhjrzcfoq"

# Receiver
receiver_email = "kaamchor.yt56@gmail.com"

# Message
subject = OTP()
body = "Here is your OTP!"

message = f"Subject: {subject}\n\n{body}"

# Send email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    server.sendmail(sender_email, receiver_email, message)
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)

EnterOTP = input("Enter OTP => ")

if(EnterOTP == subject):
    print("OTP Matched!")
else:
    print("OTP Isn't Matched")

