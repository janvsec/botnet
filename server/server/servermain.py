from function1 import example1
import tkinter as tk

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

data = [1, 2, 3, 4, 5]

def run_red():
    set_color("#1e1e1e")

def run_green():
    set_color("green")

def run_blue():
    set_color("blue")

def run_orange():
    set_color("orange")

def run_purple():
    set_color("purple")

def run_brown():
    set_color("brown")

def set_color(color):
    app.configure(bg=color)
    right_frame.configure(bg=color)
    output_label.configure(bg=color)
    output_label.config(text=example1(data))

app = tk.Tk()
app.title("Simple Python UI")
app.geometry("1200x800")
app.resizable(False, False)
app.configure(bg=theme["bg"])

main_frame = tk.Frame(app, bg=theme["bg"])
main_frame.pack(fill="both", expand=True)

left_panel = tk.Frame(main_frame, bg="#151515", width=250)
left_panel.pack(side="left", fill="y")
left_panel.pack_propagate(False)

right_frame = tk.Frame(main_frame, bg=theme["bg"])
right_frame.pack(side="right", fill="both", expand=True)

btn_red = tk.Button(left_panel, text="Run Default", command=run_red, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_red.pack(fill="x", pady=5, padx=10)

btn_green = tk.Button(left_panel, text="Run Green", command=run_green, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_green.pack(fill="x", pady=5, padx=10)

btn_blue = tk.Button(left_panel, text="Run Blue", command=run_blue, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_blue.pack(fill="x", pady=5, padx=10)

btn_orange = tk.Button(left_panel, text="Run Orange", command=run_orange, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_orange.pack(fill="x", pady=5, padx=10)

btn_purple = tk.Button(left_panel, text="Run Purple", command=run_purple, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_purple.pack(fill="x", pady=5, padx=10)
##########################
btn_brown = tk.Button(left_panel, text="Run Brown", command=run_brown, bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_active_bg"], activeforeground=theme["button_active_fg"], font=theme["button_font"], relief="flat", bd=0, padx=theme["padding"], pady=theme["padding"])
btn_brown.pack(fill="x", pady=5, padx=10)

output_label = tk.Label(right_frame, text="", font=theme["label_font"], bg=theme["bg"], fg=theme["fg"], wraplength=750, justify="center")
output_label.pack(expand=True)
app.mainloop()
