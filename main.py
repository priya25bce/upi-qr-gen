import time
import qrcode
import tkinter as tk
from urllib.parse import quote as encode
from PIL import Image, ImageTk

# Validating the functions 

# Checks if  upi is valid

def correct_upi(i):
    if i.count('@')!=1:
        return False
        

    user= i.split('@')[0]
    provider=i.split('@')[1]

    if user=="" or provider=="":
        return False
        

    allowed= set("abcdefghijklmnopqrstuvwxyz0123456789.-_")
    

    for c in user:
        if c not in allowed:
            
            return False
            

    for c in provider:
        if not c.isalnum():
            return False

    return True


# Checking name 

def correct_name(n):
    if n=="":
        return False

    
    for c in n:
        if not c.isalnum() and c!= " " and c!='.': 
            return False
            
    return True
def correct_amount(a):
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
        if len(decimal)>2: 
            
        # only two decimal places allowed

            
            return False
            

    return True

# INPUT

upi_id = input("Enter your UPI ID: ").strip().lower()

if not correct_upi(upi_id):
    print("ERROR: Invalid UPI ID.  \n Please enter it correctly.")
    raise SystemExit(1)

name = input("Enter your Name: ").strip()

if not correct_name(name):
    print("ERROR: Invalid name.\n   Letters, numbersand spaces allowed.")
    raise SystemExit(1)

amount = input("Enter Amount (optional): ").strip()


if not correct_amount(amount):
    print("ERROR: Invalid amount. \n Example: 300.56 or 300")
    raise SystemExit(1)

message=input("Enter Message (optional): ").strip()

# URL CONSTRUCTION

# some symbols are not allowed in url, so we have to encode it


nameEnc= encode(name)
msgEnc= encode(message)




# URL is of the format upi://pay?pa={upi_id}&pn={name_enc}&cu=INR&am={amount}&tn={message}

upi_url= f"upi://pay?pa={upi_id}&pn={nameEnc}&cu=INR"

if amount!="":
    upi_url= upi_url + '&am=' + amount
# add amount if provided

if message!="":
   upi_url=upi_url+ '&tn=' + msgEnc 
# add message if provided

# QR SAVE AND DISPLAY

current_time = time.time()
timestamp= int(current_time)
qr_file= f"generated_qr_code_{timestamp}.png"
qr= qrcode.make( upi_url)
qr.save(qr_file)

print('\nQR code saved as file:', qr_file)
print('UPI URL:', upi_url)

root= tk.Tk()
root.title("QR Code")
root.geometry("320x320")
qr_img= Image.open(qr_file)
qr_img= qr_img.resize((300, 300)) # resize the image
tk_img= ImageTk.PhotoImage(qr_img)
label= tk.Label(root, image=tk_img)
label.pack(pady=10)
label.image= tk_img
root.mainloop()


# scan with your mobile phone
# the payment is done 
#good to go 
#enjoy this program









