# QR Code Generator Project

This project generates UPI payment QR codes using a provided UPI ID, name, message and amount. It also includes a Tkinter GUI for displaying the generated QR code.

https://github.com/user-attachments/assets/e70ef600-c98b-4ff0-b61d-7d5f620147c0



## Overview

- Validates all inputs
- Creates a payment link
- Saves a terminal QR Code 
- Display the QR Code in the GUI Framework
- Works on Windows, Linux, and macOS

## Features

- Validates UPI ID and rejects the UPI ID if something is missing 
- Works with all payment apps
- Just scan the QR code from the app which you need to  do the payment 
- It is a simple project
- Beginner friendly and helpful to learn python 
- Encodes special characters used in the URL

## Technology Used

- Python 3.8+  
- Tkinter for  (GUI)  
- qrcode for  (QR  code generation)  
- pillow  for (image handling)  
- urllib  for (encoding url)

## Installation

```sh
git clone https://github.com/priya25bce/upi-qr-gen
cd upi-qr-gen
pip install -r requirements.txt
```

> [!NOTE]
> Create a virtual environment if you're on linux before running the pip command

## Running the Program

```sh
python main.py
````

> [!TIP]
> Leave optional fields blank if you want to. (press return/enter) 

## Input Rules

- **UPI ID** must be in the format `user@provider`

- **Name**: enter your full  name or just the name 

- **Amount**: integers or up to 2 decimals

- **Message**: everything allowed except `&` and `=`

## Project Structure

- [main.py](./main.py)            project code
- [README.md](./README.md)        documentation
- [requirements.txt](./requirements.txt)   dependencies
- [Statement.md](./Statement.md)  project statement
