from tkinter import Toplevel, Label, Scale, Button, messagebox

def set_gravity_slider():
    window = Toplevel()
    window.title("Gravity Settings")
    window.geometry("300x150")

    Label(window, text="Set Gravity:").pack(pady=5)
    slider = Scale(window, from_=0, to=200, orient="horizontal")
    slider.set(50)
    slider.pack(pady=5)

    def apply():
        messagebox.showinfo("Gravity Applied", f"Gravity set to {slider.get()}")
        window.destroy()

    Button(window, text="Apply", command=apply).pack(pady=10)
