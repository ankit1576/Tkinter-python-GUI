from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


def validate_phone_number(action, value):
    """Allow only numbers and ensure the length does not exceed 10 digits."""
    if action != '1':  # Not inserting new text
        return True
    return value.isdigit() and len(value) <= 10


def validate_otp(action, value):
    """Allow only numbers and ensure the length is exactly 6 digits."""
    if action != '1':  # Not inserting new text
        return True
    return value.isdigit() and len(value) <= 6


def send_otp():
    """Simulate OTP sending with a delay and show a success message."""
    root.config(cursor="wait")
    login_button.config(text="Sending...", font=("Helvetica", 13, "bold"), bg='white', fg='black', state=DISABLED)
    root.after(3000, reset_after)  # Show success message after 3 seconds


def reset_after():
    """Reset the cursor and update button text to indicate OTP sent."""
    root.config(cursor="")
    login_button.config(text="OTP Sent!", font=("Helvetica", 13, "bold"), bg='white', fg='black', state=DISABLED)

    # Hide mobile entry fields
    mobile_entry.place_forget()
    country_code_dropdown.place_forget()

    # Clear the mobile number display
    canvas.itemconfig(mobile_number_display, text="", state='normal')

    # Clear the country and mobile number labels
    canvas.itemconfig(country_label, text="", state='normal')  # Clear country label
    canvas.itemconfig(mobile_label, text="", state='normal')  # Clear mobile label

    # Show OTP entry field
    otp_entry.place(x=100, y=320, height=30,width=80)  # Center the OTP entry box
    canvas.itemconfig(otp_label, state='normal')  # Show the OTP label

    # Display the entered mobile number
    canvas.itemconfig(mobile_number_display, text=f"Otp send to {country_code_var.get()}{mobile_entry.get()}",
                      state='normal')

    # Show the login button for OTP verification
    login_button_otp.place(x=87, y=370)


def login_handle():
    login_input=mobile_entry.get()
    if login_input=='9889669245':
        messagebox.showinfo(login_input,'Login Succesfully',)
    else:
        messagebox.showinfo(login_input, 'Phone no does not exist', )

# Initialize Tkinter window
root = Tk()
root.geometry("300x500")
root.minsize(300, 500)
root.maxsize(300, 500)
root.iconbitmap('images/icon.ico')
root.title("WhatsApp Login")

# Load and set the background image
bg_image = Image.open("images/bg.jpg").resize((400, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(root, width=300, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# Add the logo on the canvas
logo_image = Image.open("images/logo3.png").resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
canvas.create_image(51, 20, anchor="nw", image=logo_photo)

canvas.create_text(150, 233, text="Welcome to", fill="black", font=("Helvetica", 12, "bold"))

# Add the text to the canvas
canvas.create_text(150, 259, text="WhatsApp", fill="#319763", font=("Helvetica", 24, "bold"))

# Country code label and dropdown
country_label = canvas.create_text(65, 310, text="Country", fill="black", font=("Helvetica", 10))
mobile_label = canvas.create_text(167, 310, text="Mobile Number", fill="black", font=("Helvetica", 10))

country_code_var = StringVar()
country_code_dropdown = ttk.Combobox(root, textvariable=country_code_var, font=("Helvetica", 14), width=5)
country_code_dropdown['values'] = ["+1", "+91", "+44", "+61", "+81"]
country_code_dropdown.current(1)
country_code_dropdown.place(x=41, y=320)

# Validation command for phone number entry
vcmd_phone = (root.register(validate_phone_number), '%d', '%P')

# Mobile number entry
mobile_entry = Entry(root, width=11, font=("Helvetica", 14), validate="key", validatecommand=vcmd_phone)
mobile_entry.place(x=120, y=320, height=30)

# OTP label (initially hidden)
otp_label = canvas.create_text(150, 360, text="Enter 6 digit One time password", fill="black", font=("Helvetica", 10), state='hidden')

# OTP entry (initially hidden)
otp_entry = Entry(root, width=11, font=("Helvetica", 14), validate="key",
                  validatecommand=(root.register(validate_otp), '%d', '%P'))
otp_entry.place(x=120, y=380, height=30)
otp_entry.place_forget()  # Hide the OTP entry initially

# Mobile number display (initially hidden)
mobile_number_display = canvas.create_text(150, 310, text="", fill="black", font=("Helvetica", 10), state='hidden')

# Login button for sending OTP
login_button = Button(root, text="Send OTP", bg="#319763", fg="white", font=("Helvetica", 12, "bold"), width=10,
                      command=send_otp)
login_button.place(x=87, y=410)

# Login button for OTP verification (initially hidden)
login_button_otp = Button(root, text="Login", bg="#319763", fg="white", font=("Helvetica", 12, "bold"), width=10,command=login_handle)
login_button_otp.place(x=87, y=2800)  # Position of the login button for OTP verification
login_button_otp.place_forget()  # Hide the login button initially

root.mainloop()
