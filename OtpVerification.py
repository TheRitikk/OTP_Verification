import random
import smtplib
import tkinter as tk
from tkinter import messagebox

# Global variable to track whether OTP has been sent
otp_sent = False

# Generate a random 6-digit OTP
def generate_otp():
    digits = "0123456789"
    return "".join(random.choice(digits) for _ in range(6))

# Send OTP
def send_otp():
    global otp_sent  # Declare otp_sent as a global variable
    email_address = "ritiksingh322001@gmail.com"
    email_password = "eedx odxk kswq anjq"
    recipient_email = email_entry.get()
    subject = "OTP"

    if not recipient_email or not subject:
        messagebox.showerror("Error", "Please enter email address")
        return

    try:
        global OTP
        OTP = generate_otp()
        otp_msg = f"Subject: {subject}\n\n{OTP} is your OTP"

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email_address, email_password)
        s.sendmail(email_address, recipient_email, otp_msg)
        s.quit()
        messagebox.showinfo("Success", "OTP sent successfully to your email.")

        # Disable the "Send OTP" button
        send_button.config(state="disabled")
        otp_sent = True

        # Show the OTP entry and verify button
        otp_frame.pack()
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "SMTP Authentication Error. Please check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Verify OTP
def verify_otp():
    user_input = otp_entry.get()

    if user_input == OTP:
        messagebox.showinfo("Success", "OTP Verified")
        window.destroy()  
    else:
        messagebox.showerror("Error", "Please check your OTP again.")

# Resend OTP
def resend_otp():
    send_otp()
    
    # Re-enable the "Send OTP" button after resending
    send_button.config(state="normal")

# Create a GUI window
window = tk.Tk()
window.title("OTP Verification")
window.geometry("400x200")  

# Email Entry
email_label = tk.Label(window, text="Enter your email:")
email_label.pack(pady=5)
email_entry = tk.Entry(window)
email_entry.pack(pady=5)

# Send OTP Button
send_button = tk.Button(window, text="Send OTP", command=send_otp)
send_button.pack()

# Frame to contain OTP entry and verify button (initially hidden)
otp_frame = tk.Frame(window)
otp_frame.pack_forget()

# OTP Entry
otp_label = tk.Label(otp_frame, text="Enter Your OTP:")
otp_label.pack()
otp_entry = tk.Entry(otp_frame)
otp_entry.pack()

# Verify OTP Button
verify_button = tk.Button(otp_frame, text="Verify OTP", command=verify_otp)
verify_button.pack()

# Resend OTP Button
resend_button = tk.Button(otp_frame, text="Resend OTP", command=resend_otp)
resend_button.pack()

# Label to display generated OTP
generated_otp_label = tk.Label(otp_frame, text="", font=("Helvetica", 16))
generated_otp_label.pack()

window.mainloop()
