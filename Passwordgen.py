from operator import index
import tkinter as tk
import random
import string 

def generate_password():
    try:
        pwd_length = int(entry.get())
        
        if pwd_length<5 or pwd_length>20:
            output_lbl.config(text= "Password length must be between 5 and 20")
            return
        
        safe_symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        characters = string.ascii_letters + string.digits + safe_symbols
        password = ''.join(random.choice(characters) for i in range(pwd_length))
        
        
        entry.delete(0, tk.END)
        entry.insert(0, password)
        output_lbl.config(text= "Password generated successfully")
        
    except ValueError:
        output_lbl.config(text= "Please enter a valid number")
        



root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.config(bg = "navy")

lbl= tk.Label(root, text= "Enter length", font= ("Arial", 16), fg= "white", bg= "navy")
lbl.pack(pady = 10)

entry= tk.Entry(root, font= ("Arial", 16), justify= "right")
entry.insert( 0,"8")
entry.pack(pady = 10)

output_lbl= tk.Label(root, text= "", font= ("Arial", 16), fg= "white", bg= "navy")
output_lbl.pack(pady = 20)

btn = tk.Button(root, text= "Generate Password", font= ("Arial", 16), fg= "black", bg= "yellow", command = generate_password)
btn.pack(pady = 10)

root.mainloop()

