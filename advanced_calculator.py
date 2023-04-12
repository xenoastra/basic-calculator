
import tkinter as tk

calc = ""

def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calc)

def evaluate():
    global calc
    try:
        calc = str(eval(calc))
        result.delete(1.0, "end")
        result.insert(1.0, calc)
    except:
        clear()
        result.insert(1.0, "Error")
    
def clear():
    global calc
    calc = ""
    result.delete(1.0, "end")

def backspace():
    global calc
    calc = calc[:-1]
    result.delete(1.0, "end")
    result.insert(1.0, calc)

root = tk.Tk()
root.geometry("320x375") # size of calculator
root.configure(bg="#7BC6C0")


result = tk.Text(root, height=2, width=16, font=("Helvetica", 24))
result.grid(columnspan=5)
result.configure(bg="#C9F4EE")

button_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Helvetica", "14"),bg="#46C2B8")# lambda is needed
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_0.grid(row=5, column=2)

button_bs = tk.Button(root, text="Back", command=lambda: backspace(), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_bs.grid(row=7, column=3)

button_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_plus.grid(row=7, column=2)
button_minus = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_minus.grid(row=6, column=1)
button_div = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_div.grid(row=6, column=2)
button_mul = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_mul.grid(row=6, column=3)

button_open = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_close.grid(row=5, column=3)
button_clear = tk.Button(root, text="clear", command=clear, width=5, font=("Helvetica", "14"),bg="#46C2B8")
button_clear.grid(row=7, column=1)


button_eq = tk.Button(root, text="=", command=evaluate, width=8, font=("Helvetica", "14"),bg="#46C2B8")
button_eq.grid(row=8, column=2)

root.mainloop() # GUI objects
