import time
import qrcode
import tkinter as tk
from urllib.parse import quote as encode
from PIL import Image, ImageTk

# VALIDATION FUNCTIONS

# Checks if  upi is valid
def valid_upi(u):
    if u.count('@')!=1:
        return False

    user= u.split('@')[0]
    provider=u.split('@')[1]

    if user=="" or provider=="":
        return False

    allowed_set= set("abcdefghijklmnopqrstuvwxyz0123456789.-_")

    for c in user:
        if c not in allowed_set:
            return False

    for c in provider:
        if not c.isalnum():
            return False

    return True
# Check valid name
def valid_name(n):
    if n=="":
        return False
    for c in n:
        if not c.isalnum() and c!= " " and c!='.': 
            return False
    return True
def valid_amount(a):
    if a =="":
        return True
    number_parts= a.split('.')
    if len(number_parts)>2:
        return False
    integer= number_parts[0]
    if not integer.isdigit():
        return False
    if len(number_parts) ==2:
        decimal= number_parts[1]
        if not decimal.isdigit():
            return False
        if len(decimal)>2:  # only two decimal places allowed
            return False

    return True

# INPUT

user_upi_id = input("Enter your UPI ID: ").strip().lower()

if not valid_upi(user_upi_id):
    print("ERROR: Invalid UPI ID. Expected format: user@provider")
    raise SystemExit(1)

user_name = input("Enter your Name: ").strip()

if not valid_name(user_name):
    print("ERROR: Invalid name. only letters, numbers, and spaces allowed.")
    raise SystemExit(1)

amount = input("Enter Amount (optional): ").strip()


if not valid_amount(amount):
    print("ERROR: Invalid amount. Example: 530.56 or 300")
    raise SystemExit(1)

message=input("Enter Message (optional): ").strip()

# URL CONSTRUCTION

# some symbols are not allowed in url, so we have to encode it
nameEnc= encode(user_name)
msgEnc= encode(message)




# URL is of the format upi://pay?pa={upi_id}&pn={name_enc}&cu=INR&am={amount}&tn={message}
url= f"upi://pay?pa={user_upi_id}&pn={nameEnc}&cu=INR"
if amount!="":
    url= url + '&am=' + amount # add amount if provided
if message!="":
    url= url + '&tn=' + msgEnc # add message if provided

# QR SAVE AND DISPLAY

current_time = time.time()
timestamp= int(current_time)
qrfile= f"generated_qr_code_{timestamp}.png"
qr= qrcode.make(url)
qr.save(qrfile)

print('\nQR code saved as file:', qrfile)
print('UPI URL:', url)

root= tk.Tk()
root.title("QR Code")
root.geometry("320x320")
qr_img= Image.open(qrfile)
qr_img= qr_img.resize((300, 300)) # resize the image
tk_img= ImageTk.PhotoImage(qr_img)
label= tk.Label(root, image=tk_img)
label.pack(pady=10)
label.image= tk_img
root.mainloop()

# scan with your mobile phone
