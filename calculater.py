import tkinter as tk

def click_button(item):
    current_text = input_text.get()
    input_text.set(current_text + str(item))

def clear_input():
    input_text.set("")

def evaluate_expression():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.resizable(0, 0)

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=('Arial', 18), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, font=('Arial', 18), fg='red', width=5, height=2,
                        command=clear_input)
    elif button == '=':
        btn = tk.Button(root, text=button, font=('Arial', 18), fg='green', width=5, height=2,
                        command=evaluate_expression)
    else:
        btn = tk.Button(root, text=button, font=('Arial', 18), width=5, height=2,
                        command=lambda b=button: click_button(b))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
