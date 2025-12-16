from function1 import example1
import tkinter as tk

# ------------------- THEME CONFIG -------------------
theme = {
    "bg": "#1e1e1e",
    "fg": "white",
    "button_bg": "#2d2d2d",
    "button_fg": "white",
    "button_active_bg": "#444444",
    "button_active_fg": "white",
    "label_font": ("Arial", 14),
    "button_font": ("Arial", 12, "bold"),
    "padding": 10
}

# ------------------- DATA -------------------
data = [1, 2, 3, 4, 5]

# ------------------- FUNCTIONS -------------------
def getcommand():
    result = example1(data)
    convertext(result)

def convertext(text):
    output_label.config(text=text)

# ------------------- APP SETUP -------------------
app = tk.Tk()
app.title("Simple Python UI")
app.geometry("800x400")
app.resizable(False, False)
app.configure(bg=theme["bg"])

# ------------------- BUTTON -------------------
btn_hello = tk.Button(
    app,
    text="Run Function",
    command=getcommand,
    bg=theme["button_bg"],
    fg=theme["button_fg"],
    activebackground=theme["button_active_bg"],
    activeforeground=theme["button_active_fg"],
    font=theme["button_font"],
    relief="flat",
    bd=0,
    highlightthickness=0,
    padx=theme["padding"],
    pady=theme["padding"]
)
btn_hello.pack(pady=theme["padding"])

# ------------------- OUTPUT LABEL -------------------
output_label = tk.Label(
    app,
    text="",
    font=theme["label_font"],
    bg=theme["bg"],
    fg=theme["fg"],
    wraplength=750,
    justify="center"
)
output_label.pack(pady=theme["padding"])

# ------------------- RUN APP -------------------
app.mainloop()
