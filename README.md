# QR Code Generator Project

This project generates UPI payment QR codes using a provided UPI ID, name, message and amount. It also includes a Tkinter GUI for displaying the generated QR code.


https://github.com/user-attachments/assets/cf2750f6-1772-4408-a24c-07e4facca3a1





## Overview

- Validates all inputs.
- Creates a payment link.
- Saves a terminal QR with timestamp.  
- Works on Windows, Linux, and macOS.

## Features

- Validates UPI IDs and rejects invalid ones  
- Works with all payment apps
- Appends timestamp to the image file to avoid conflict
- Simple and beginner-friendly
- Encodes special characters used in the URL

## Technology Used

- Python 3.8+  
- Tkinter (GUI)  
- qrcode (QR generation)  
- pillow (image handling)  
- urllib (encoding url)

## Installation

```sh
git clone https://github.com/priya25bce/upi-qr-gen
cd upi-qr-gen
pip install -r requirements.txt
```

> [!NOTE]
> Create a virtual environment if you're on linux before running the pip command. 

## Running the Program

```sh
python main.py
````

> [!TIP]
> Leave optional fields blank if you want to. (press return/enter) 

## Input Rules

- **UPI ID** must be in the format `user@provider`

- **Name**: letters, digits, spaces

- **Amount**: integers or up to 2 decimals

- **Message**: everything allowed except `&` and `=`

## Project Structure

- [main.py](./main.py)            project code
- [README.md](./README.md)        documentation
- [requirements.txt](./requirements.txt)   dependencies
- [Statement.md](./Statement.md)  project statement
