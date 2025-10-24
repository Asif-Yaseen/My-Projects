import tkinter as tk
from tkinter import messagebox
import math



# -------------------- Main Window Setup --------------------

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("500x700")
root.resizable(False, False)



# -------------------- Gradient Background --------------------

canvas = tk.Canvas(root, width=500, height=700)
canvas.pack(fill="both", expand=True)



# Draw vertical gradient

for i in range(0, 700):
    color = "#%02x%02x%02x" % (255 - i//3, 180 - i//4, 255 - i//5)
    canvas.create_line(0, i, 500, i, fill=color)



# -------------------- Frame for Calculator --------------------

frame = tk.Frame(root, bg="#f8f8f8", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center")



# -------------------- Display Entry --------------------

display = tk.Entry(frame, font=("Consolas", 24), bd=5, relief="ridge", justify="right", width=22)
display.grid(row=0, column=0, columnspan=5, pady=10, padx=10)



# -------------------- History Panel --------------------

history_label = tk.Label(frame, text="History", font=("Arial", 12), bg="#f8f8f8", anchor="w")
history_label.grid(row=1, column=0, columnspan=5, sticky="w", padx=10)


history_text = tk.Text(frame, height=5, width=40, font=("Arial", 10), bg="#f0f0f0", relief="sunken")
history_text.grid(row=2, column=0, columnspan=5, padx=10, pady=5)



# -------------------- Button Styling --------------------

btn_font = ("Arial", 18)
btn_bg = "#e0e0e0"
btn_active = "#d0d0d0"

def on_enter(e):
    e.widget['background'] = btn_active

def on_leave(e):
    e.widget['background'] = btn_bg



# -------------------- Button Click Logic --------------------

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(display.get())
            history_text.insert(tk.END, display.get() + " = " + str(result) + "\n")
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
    elif text == "C":
        display.delete(0, tk.END)
    elif text == "⌫":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current[:-1])
    elif text == "√":
        try:
            value = float(display.get())
            result = math.sqrt(value)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input for √")
    elif text == "%":
        try:
            value = float(display.get())
            result = value / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input for %")
    else:
        display.insert(tk.END, text)



# -------------------- Button Layout --------------------

buttons = [
    ["C", "⌫", "%", "√", "/"],
    ["7", "8", "9", "*", "("],
    ["4", "5", "6", "-", ")"],
    ["1", "2", "3", "+", "."],
    ["0", "=", "", "", ""]
]


for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char != "":
            btn = tk.Button(frame, text=char, font=btn_font, width=5, height=2, bg=btn_bg, relief="raised")
            btn.grid(row=r+3, column=c, padx=5, pady=5)
            btn.bind("<Button-1>", click)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)


# -------------------- Keyboard Support --------------------

def keypress(event):
    key = event.char
    if key in "0123456789+-*/.=()":
        if key == "=":
            try:
                result = eval(display.get())
                history_text.insert(tk.END, display.get() + " = " + str(result) + "\n")
                display.delete(0, tk.END)
                display.insert(tk.END, str(result))
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
        else:

            display.insert(tk.END, key)
    elif event.keysym == "BackSpace":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current[:-1])
    elif event.keysym == "Return":
        try:
            result = eval(display.get())
            history_text.insert(tk.END, display.get() + " = " + str(result) + "\n")
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")


root.bind("<Key>", keypress)


# -------------------- Run the App --------------------

root.mainloop()