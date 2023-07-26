import tkinter as tk
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
from tkinter import messagebox, END

root = tk.Tk()
root.title("Secured Notes")
root.geometry("600x700")

image_icon = ImageTk.PhotoImage(file="sn-icon.ico")
root.iconphoto(True, image_icon)

FONT = ('Bahnschrift', 14)

sn_logo = ImageTk.PhotoImage(Image.open("sn-logo.png"))
logo_label = tk.Label(root, image=sn_logo)
logo_label.place(x=-90, y=-55)

label_title = tk.Label(root, text="Enter the title of your note:", font=FONT)
label_title.place(x=130, y=150)

note_title = tk.StringVar()
entry_title = tk.Entry(width=35, textvariable=note_title)
entry_title.place(x=133, y=180)

label_note = tk.Label(root, text="Enter your note:", font=FONT)
label_note.place(x=130, y=230)

text1 = tk.Text(width=35, height=10)
text1.place(x=133, y=260)

label_code = tk.Label(root, text="Security code:", font=FONT)
label_code.place(x=130, y=450)

security_code = tk.StringVar()
entry_code = tk.Entry(textvariable=security_code, width=35, show="*")
entry_code.place(x=133, y=480)


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


write_key()

key = load_key()

f = Fernet(key)


def encrypt():
    temp = text1.get("1.0", END).encode()
    encrypted_note = f.encrypt(temp)
    encrypted_note_str = encrypted_note.decode()
    if security_code.get() == "28lethe_fd+8B==W?":
        output_window = tk.Tk()
        output_window.geometry("800x300")
        output_window.title("Secured Notes")
        output_label = tk.Label(output_window, text="Encrypted Note:", font=('Bahnschrift', 16))
        output_label.place(x=100,y=60)
        output_text = tk.Text(output_window, height=5, )
        output_text.insert(1.0, encrypted_note_str)
        output_text.place(x=100, y=100)
        with open("secured_notes.txt", "a") as file:
            file.write(f"Note Title: {note_title.get()}\n")
            file.write(f"Encrypted Note: {encrypted_note_str}\n\n")
    else:
        messagebox.showwarning("Warning!", "Incorrect password.")


def decrypt():
    try:
        if security_code.get() == "28lethe_fd+8B==W?":
            temp = text1.get("1.0", END).encode()
            decrypted_message = f.decrypt(temp)
            decrypted_message_str = decrypted_message.decode()
            output_window = tk.Tk()
            output_window.geometry("800x300")
            output_window.title("Secured Notes")
            output_label = tk.Label(output_window, text="Decrypted Note:", font=('Bahnschrift', 16))
            output_label.place(x=100, y=60)
            output_text = tk.Text(output_window, height=5, )
            output_text.insert(1.0, decrypted_message_str)
            output_text.place(x=100, y=100)
        else:
            messagebox.showwarning("Warning!", "Incorrect password")
    except:
        messagebox.showwarning("Unencrypted Note!", "You have entered an unencrypted note.")


def clear():
    entry_title.delete(0, END)
    text1.delete("1.0", END)
    entry_code.delete(0, END)


encrypt_button = tk.Button(root, text="Encrypt", font=FONT, bg= "SkyBlue2", command=encrypt)
encrypt_button.place(x=130, y=520,height=40, width=80)

decrypt_button = tk.Button(root, text="Decrypt", font=FONT, bg="SkyBlue2", command=decrypt)
decrypt_button.place(x=230, y=520, height=40, width=80)

clear_button = tk.Button(root, text="Clear", font=FONT, bg="gainsboro", command=clear)
clear_button.place(x=350, y=520, height=40, width=60)

root.mainloop()