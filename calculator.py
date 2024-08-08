import tkinter as tk
from tkinter import messagebox

def setup_window():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("400x600")
    window.resizable(0, 0)
    return window

def create_widgets(window):
    display = tk.Entry(window, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
    display.grid(row=0, column=0, columnspan=4, ipady=10)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        create_button(window, display, button, row_val, col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    clear_button = tk.Button(window, text="C", font=("Arial", 20), fg="red", command=lambda: display.delete(0, tk.END))
    clear_button.grid(row=row_val, column=0, columnspan=4, sticky="nsew")

def create_button(window, display, value, row, col):
    button = tk.Button(
        window,
        text=value,
        font=("Arial", 20),
        command=lambda: on_button_click(display, value)
    )
    button.grid(row=row, column=col, sticky="nsew")

def on_button_click(display, value):
    if value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)

def configure_grid(window):
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)

def main():
    window = setup_window()
    create_widgets(window)
    configure_grid(window)
    window.mainloop()

if __name__ == "__main__":
    main()
