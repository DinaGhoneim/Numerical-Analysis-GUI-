from simple_fixed_point import *
from Newton import *
from Secant import *
from false_position import *
import re


def click1():
    window = CTk(fg_color='#CADCFC')
    window.geometry("500x500")
    window.title("Chapter One")
    label = CTkLabel(master=window, text="Chapter One Methods", font=("Times New Roman", 50), text_color="#00246B",
                     fg_color="#CADCFC")
    label.place(relx=0.5, rely=0.1, anchor="n")
    btn1 = CTkButton(master=window, text="Bisection", fg_color="#00246B", hover_color="#0000cd", text_color="#CADCFC",
                     command=bisection)
    btn1.place(relx=0.4, rely=0.3, anchor="e")
    btn2 = CTkButton(master=window, text="False Position", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=false_position)
    btn2.place(relx=0.6, rely=0.3, anchor="w")
    btn3 = CTkButton(master=window, text="Simple Fixed Point", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=simple_fixed_point)
    btn3.place(relx=0.4, rely=0.7, anchor="e")
    btn4 = CTkButton(master=window, text="Newton", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=newton)
    btn4.place(relx=0.6, rely=0.7, anchor="w")
    btn5 = CTkButton(master=window, text="Secant", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Secant)
    btn5.place(relx=0.5, rely=0.5, anchor="center")
    window.mainloop()


def bisection():
    window = CTk(fg_color='#CADCFC')
    window.title("Bisection Method")
    label = CTkLabel(master=window, text="Bisection Method", font=("Times New Roman", 50), text_color="#00246B",
                     fg_color="#CADCFC")
    label.pack(side='top', pady=30)

    frameFx = CTkFrame(window, fg_color='#CADCFC')
    frameFx.pack(fill='x')

    f_label = CTkLabel(master=frameFx, text="F(x) : ", font=("Times New Roman", 30), text_color="black",
                       fg_color="#CADCFC")
    f_label.pack(side='left', padx=10)
    f_entry = CTkEntry(master=frameFx, placeholder_text="x^3+x-1....", text_color="black", width=960)
    f_entry.pack(side='right', ipadx=110, padx=30, fill='x')

    frameI = CTkFrame(window, fg_color='#CADCFC')
    frameI.pack(fill='both', padx=10)

    xl_label = CTkLabel(master=frameI, text=" x_l : ", font=("Times New Roman", 25), text_color="black",
                        fg_color="#CADCFC")
    xl_label.place(relx=0.1, rely=0.5, anchor="e")
    xl_entry = CTkEntry(master=frameI, placeholder_text="0", text_color="black", width=120)
    xl_entry.place(relx=0.2, rely=0.5, anchor="e")
    xu_label = CTkLabel(master=frameI, text=" x_u : ", font=("Times New Roman", 25), text_color="black",
                        fg_color="#CADCFC")
    xu_label.place(relx=0.3, rely=0.5, anchor="e")
    xu_entry = CTkEntry(master=frameI, placeholder_text="1", text_color="black", width=120)
    xu_entry.place(relx=0.4, rely=0.5, anchor="e")
    error_label = CTkLabel(master=frameI, text=" ε_a : ", font=("Times New Roman", 25), text_color="black",
                           fg_color="#CADCFC")
    error_label.place(relx=0.5, rely=0.5, anchor="e")
    error_entry = CTkEntry(master=frameI, placeholder_text="%", text_color="black", width=120)
    error_entry.place(relx=0.6, rely=0.5, anchor="e")
    switch = CTkSwitch(master=frameI, text="OR", font=("Times New Roman", 25), text_color="black")
    switch.place(relx=0.7, rely=0.5, anchor="e")
    et_label = CTkLabel(master=frameI, text=" Iteration Numbers : ", font=("Times New Roman", 25), text_color="black",
                        fg_color="#CADCFC")
    et_label.place(relx=0.9, rely=0.5, anchor="e")
    et_entry = CTkEntry(master=frameI, placeholder_text="4", text_color="black", width=120)
    et_entry.place(relx=0.9, rely=0.5, anchor="w")
    headers = ["i", "x_l", "F(x_l)", "x_u", "F(x_u)", "xr", "F(xr)", "ε_a"]

    frameL = CTkFrame(window, fg_color='#CADCFC')
    frameL.pack(side='bottom', fill='both')
    frameT = CTkScrollableFrame(frameL, fg_color='#CADCFC')
    frameT.pack(fill='both', side='top')
    table = CTkTable(master=frameT, column=8, fg_color="#00246B")
    table.pack(fill='both')

    table.add_row(headers, 0)

    def transform_expression(expression):
        terms = re.split(r'([-+*/])', expression)
        transformed_terms = []
        for term in terms:
            if 'x' in term:
                if term.startswith('x'):
                    term = '1' + term  # add coefficient 1 if none exists
                if not term.startswith('('):
                    term = term.replace('x', '*x')
                term = term.replace('^', '**')
            transformed_terms.append(term)

        return ''.join(transformed_terms)

    def insert_data():
        fx = f_entry.get()
        fx = transform_expression(fx)
        func = expand(fx)
        xl = float(xl_entry.get())
        xu = float(xu_entry.get())
        i = 1
        eerror = 10000.00
        if func.subs('x', xl)*func.subs('x', xu) >= 0:
            tk.messagebox.showerror("Error", "Please enter valid numbers for xl and xu.")
            return
        if switch.get() == 1:
            et = int(et_entry.get())
            while i <= et:
                xr = float((xl + xu) / 2)
                if i == 1:
                    eerror = '-----'
                input_data = [
                    i,
                    round(xl, 3),
                    round(func.subs('x', xl), 3),
                    round(xu, 3),
                    round(func.subs('x', xu), 3),
                    round(xr, 3),
                    round(func.subs('x', xr), 3),
                    eerror
                ]
                table.add_row(input_data, i)
                xxr = xr
                if func.subs('x', xl) * func.subs('x', xr) < 0:
                    xu = xr
                else:
                    xl = xr
                eerror = abs((xr - xxr) / xr) * 100
                i += 1
            tk.messagebox.showinfo("Solution", f"The Root= {round(xr, 3)}")
        else:
            error = float(error_entry.get())
            xr = float((xl + xu) / 2)
            input_data = [
                i,
                round(xl, 3),
                round(func.subs('x', xl), 3),
                round(xu, 3),
                round(func.subs('x', xu), 3),
                round(xr, 3),
                round(func.subs('x', xr), 3),
                '-----'
            ]
            table.add_row(input_data, i)
            i = 2
            while float(eerror) >= error:
                xr = float((xl + xu) / 2)
                xxr = xr
                if func.subs('x', xl) * func.subs('x', xr) < 0:
                    xu = xr
                else:
                    xl = xr
                xr = float((xl + xu) / 2)
                eerror = abs((xr - xxr) / xr) * 100
                input_data = [
                    i,
                    round(xl, 3),
                    round(func.subs('x', xl), 3),
                    round(xu, 3),
                    round(func.subs('x', xu), 3),
                    round(xr, 3),
                    round(func.subs('x', xr), 3),
                    round(eerror, 3)
                ]
                table.add_row(input_data, i)
                i += 1
            tk.messagebox.showinfo("Solution", f"The Root= {round(xr, 3)}")
    insert_button = CTkButton(master=frameL, text="Calculate", fg_color="#00246B", hover_color="#0000cd",
                              text_color="#CADCFC", command=insert_data)
    insert_button.pack(side='bottom')

    window.mainloop()
