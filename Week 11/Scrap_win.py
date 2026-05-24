from Scrapper import get_car_data
import tkinter as tk
from tkinter import ttk

# =========================
# FUNCTION
# =========================
def display_data(car):
    data = get_car_data(car)

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)

    if not data:
        result_box.insert(tk.END, "No data found.")
    else:
        for item in data:
            result_box.insert(
                tk.END,
                f"🚗 {item['name']}\n💰 Price: {item['price']}\n\n"
            )

    result_box.config(state="disabled")


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("850x550")
root.configure(bg="#0f172a")  # Dark background

# =========================
# STYLE
# =========================
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground="#1e293b",
    background="#1e293b",
    foreground="white",
    padding=8
)

style.configure(
    "Custom.TButton",
    font=("Segoe UI", 11, "bold"),
    padding=10
)

# =========================
# HEADER
# =========================
title = tk.Label(
    root,
    text="🚘 Car Price Scraper",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Search latest car prices instantly",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle.pack()

# =========================
# TOP FRAME
# =========================
top_frame = tk.Frame(root, bg="#0f172a")
top_frame.pack(pady=25)

cars = ['Kia', 'Honda', 'Toyota', 'Suzuki', 'Hyundai']

dropdown = ttk.Combobox(
    top_frame,
    values=cars,
    font=("Segoe UI", 11),
    state="readonly",
    width=25
)

dropdown.current(0)
dropdown.grid(row=0, column=0, padx=10)

find_btn = tk.Button(
    top_frame,
    text="Find Prices",
    font=("Segoe UI", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2",
    command=lambda: display_data(dropdown.get())
)

find_btn.grid(row=0, column=1)

# =========================
# RESULT FRAME
# =========================
result_frame = tk.Frame(
    root,
    bg="#111827",
    bd=0
)

result_frame.pack(padx=30, pady=10, fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

# Text Area
result_box = tk.Text(
    result_frame,
    yscrollcommand=scrollbar.set,
    bg="#111827",
    fg="white",
    font=("Consolas", 11),
    relief="flat",
    padx=15,
    pady=15,
    insertbackground="white"
)

result_box.pack(fill="both", expand=True)

scrollbar.config(command=result_box.yview)

result_box.config(state="disabled")

# =========================
# FOOTER
# =========================
footer = tk.Label(
    root,
    text="Made with Python Tkinter",
    font=("Segoe UI", 9),
    bg="#0f172a",
    fg="#64748b"
)

footer.pack(pady=10)

# =========================
# RUN APP
# =========================
root.mainloop()