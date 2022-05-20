from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry("170x200")
inp = Entry(root, width=13, borderwidth=3, relief=GROOVE)
inp.grid(pady=10, row=0, sticky="w", padx=15)


def delete():
    d = inp.get()
    inp.delete(first=len(d) - 1)


def result():
    if inp.get() == "":
        inp.delete(0, "end")
    elif inp.get()[0] == "0":
        inp.delete(0, "end")
    elif inp.get() == "+":
        inp.delete(0, "end")
    elif inp.get() == "*":
        inp.delete(0, "end")
    elif inp.get() == ".":
        inp.delete(0, "end")
    elif inp.get() == "**":
        inp.delete(0, "end")
    elif inp.get() == "-":
        inp.delete(0, "end")
    elif inp.get() == "/":
        inp.delete(0, "end")
    elif inp.get() == "%":
        inp.delete(0, "end")
    elif ValueError:
        inp.delete(0, "end")

    else:
        calcres = inp.get()
        calcres = eval(calcres)
        clear()
        inp.insert("end", calcres)


def clear():
    inp.delete(0, "end")


Char_nine = Button(root, text="9", width=2, command=lambda: inp.insert("end", "9"), borderwidth=3, relief=GROOVE)
Char_nine.grid(row=1, sticky="w", padx=15)
Char_eight = Button(root, text="8", width=2, command=lambda: inp.insert("end", "8"), borderwidth=3, relief=GROOVE)
Char_eight.grid(row=1, sticky="w", padx=45)
Char_seven = Button(root, text="7", width=2, command=lambda: inp.insert("end", "7"), borderwidth=3, relief=GROOVE)
Char_seven.grid(row=1, sticky="w", padx=75)
Char_plus = Button(root, text="+", width=2, command=lambda: inp.insert("end", "+"), borderwidth=3, relief=GROOVE)
Char_plus.grid(row=1, sticky="n", padx=125)
Char_six = Button(root, text="6", width=2, command=lambda: inp.insert("end", "6"), borderwidth=3, relief=GROOVE)
Char_six.grid(row=2, sticky="w", padx=15)
Char_five = Button(root, text="5", width=2, command=lambda: inp.insert("end", "5"), borderwidth=3, relief=GROOVE)
Char_five.grid(row=2, sticky="w", padx=45)
Char_four = Button(root, text="4", width=2, command=lambda: inp.insert("end", "4"), borderwidth=3, relief=GROOVE)
Char_four.grid(row=2, sticky="w", padx=75)
Char_minus = Button(root, text="-", width=2, command=lambda: inp.insert("end", "-"), borderwidth=3, relief=GROOVE)
Char_minus.grid(row=2, sticky="n", padx=125)
Char_three = Button(root, text="3", width=2, command=lambda: inp.insert("end", "3"), borderwidth=3, relief=GROOVE)
Char_three.grid(row=3, sticky="w", padx=15)
Char_two = Button(root, text="2", width=2, command=lambda: inp.insert("end", "2"), borderwidth=3, relief=GROOVE)
Char_two.grid(row=3, sticky="w", padx=45)
Char_one = Button(root, text="1", width=2, command=lambda: inp.insert("end", "1"), borderwidth=3, relief=GROOVE)
Char_one.grid(row=3, sticky="w", padx=75)
Char_zero = Button(root, text="0", width=2, command=lambda: inp.insert("end", "0"), borderwidth=3, relief=GROOVE)
Char_zero.grid(row=4, sticky="w", padx=15)
Char_dot = Button(root, text=".", width=2, command=lambda: inp.insert("end", "."), borderwidth=3, relief=GROOVE)
Char_dot.grid(row=4, sticky="w", padx=45)
Char_multiply = Button(root, text="*", width=2, command=lambda: inp.insert("end", "*"), borderwidth=3, relief=GROOVE)
Char_multiply.grid(row=3, sticky="n", padx=125)
Char_divide = Button(root, text="/", width=2, command=lambda: inp.insert("end", "/"), borderwidth=3, relief=GROOVE)
Char_divide.grid(row=4, sticky="n", padx=125)
result = Button(root, text="=", width=11, command=result, bg="purple", fg="white", borderwidth=3)
result.grid(row=5, sticky="w", padx=15)
Char_modulus = Button(root, text="%", width=2, command=lambda: inp.insert("end", "%"), borderwidth=3, relief=GROOVE)
Char_modulus.grid(row=5, sticky="n", padx=125)
delete = Button(root, text="del", width=2, command=delete, bg="purple", fg="white")
clean = Button(root, text="C", width=2, command=clear, bg="purple", fg="white")
clean.grid(row=0, sticky="w", padx=125)
delete.grid(row=0, sticky="w", padx=100)
Char_exponentiation = Button(root, text="**", width=2, command=lambda: inp.insert("end", "**"), borderwidth=3,
                             relief=GROOVE)
Char_exponentiation.grid(row=4, sticky="w", padx=75)

root.mainloop()
