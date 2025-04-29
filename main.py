import tkinter as tk
from tkinter import messagebox
from injector import core
from mods import gravity, aimbot, esp, fly, noclip, wallbang
import threading

def show_mod_menu():
    tk.Button(root, text="Gravity Hack", command=gravity.set_gravity_slider).pack(pady=5)
    tk.Button(root, text="Aimbot", command=lambda: threading.Thread(target=aimbot.activate).start()).pack(pady=5)
    tk.Button(root, text="ESP", command=lambda: threading.Thread(target=esp.activate).start()).pack(pady=5)
    tk.Button(root, text="Fly", command=lambda: threading.Thread(target=fly.activate).start()).pack(pady=5)
    tk.Button(root, text="Noclip", command=lambda: threading.Thread(target=noclip.activate).start()).pack(pady=5)
    tk.Button(root, text="Wallbang", command=lambda: threading.Thread(target=wallbang.activate).start()).pack(pady=5)

root = tk.Tk()
root.title("Arsenal Cheat Injector")
root.geometry("400x500")

label = tk.Label(root, text="Arsenal Cheat Loader", font=("Arial", 16))
label.pack(pady=20)

def inject():
    if core.attach_to_process():
        label.config(text="Injection Successful")
        show_mod_menu()
    else:
        messagebox.showerror("Injection Failed", "Arsenal not running")

tk.Button(root, text="Inject", font=("Arial", 14), command=inject).pack(pady=10)

root.mainloop()
