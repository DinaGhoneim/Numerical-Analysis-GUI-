from Chapter_Two import *
from CTkTable import *
from sympy import *
import re


def newton():
    window = CTk(fg_color='#CADCFC')
    window.title("Newton Method")
    label = CTkLabel(master=window, text="Newton Method", font=("Times New Roman", 50),
                     text_color="#00246B",
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

    x0_label = CTkLabel(master=frameI, text=" X_0 : ", font=("Times New Roman", 25), text_color="black",
                        fg_color="#CADCFC")
    x0_label.place(relx=0.1, rely=0.5, anchor="e")
    x0_entry = CTkEntry(master=frameI, placeholder_text="0", text_color="black", width=120)
    x0_entry.place(relx=0.2, rely=0.5, anchor="e")
    error_label = CTkLabel(master=frameI, text=" ε_a : ", font=("Times New Roman", 25), text_color="black",
                           fg_color="#CADCFC")
    error_label.place(relx=0.4, rely=0.5, anchor="e")
    error_entry = CTkEntry(master=frameI, placeholder_text="%", text_color="black", width=120)
    error_entry.place(relx=0.5, rely=0.5, anchor="e")
    switch = CTkSwitch(master=frameI, text="OR", font=("Times New Roman", 25), text_color="black")
    switch.place(relx=0.6, rely=0.5, anchor="center")
    et_label = CTkLabel(master=frameI, text=" Iteration Numbers : ", font=("Times New Roman", 25), text_color="black",
                        fg_color="#CADCFC")
    et_label.place(relx=0.9, rely=0.5, anchor="e")
    et_entry = CTkEntry(master=frameI, placeholder_text="4", text_color="black", width=120)
    et_entry.place(relx=0.9, rely=0.5, anchor="w")
    headers = ["i", "x_i", "F(x_i)", "F'(x_i)", "ε_a"]
    frameL = CTkFrame(window, fg_color='#CADCFC')
    frameL.pack(side='bottom', fill='both')
    frameT = CTkScrollableFrame(frameL, fg_color='#CADCFC')
    frameT.pack(fill='both', side='top')
    table = CTkTable(master=frameT, column=5, fg_color="#00246B")
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
        der_func = diff(func, Symbol('x'))
        xi = float(x0_entry.get())
        i = 1
        eerror = 10000.00
        if switch.get() == 1:
            et = int(et_entry.get())
            while i <= et:
                fxi = float(func.subs('x', xi))
                dfxi = float(der_func.subs('x', xi))
                if i == 1:
                    eerror = '-----'
                input_data = [
                    i,
                    round(xi, 3),
                    round(func.subs('x', xi), 3),
                    round(der_func.subs('x', xi), 3),
                    eerror
                ]
                table.add_row(input_data, i)
                xxi = xi
                xi = xxi-(fxi/dfxi)
                eerror = abs((xi - xxi) / xi) * 100
                i += 1
            tk.messagebox.showinfo("Solution", f"The Root= {round(xi, 3)}")
        else:
            error = float(error_entry.get())
            fxi = float(func.subs('x', xi))
            dfxi = float(der_func.subs('x', xi))
            input_data = [
                i,
                round(xi, 3),
                round(func.subs('x', xi), 3),
                round(der_func.subs('x', xi), 3),
                '-----'
            ]
            table.add_row(input_data, i)
            i = 2
            while float(eerror) >= error:
                xxi = xi
                xi = xxi - (fxi / dfxi)
                fxi = float(func.subs('x', xi))
                dfxi = float(der_func.subs('x', xi))
                eerror = abs((xi - xxi) / xi) * 100
                input_data = [
                    i,
                    round(xi, 3),
                    round(func.subs('x', xi), 3),
                    round(der_func.subs('x', xi), 3),
                    round(eerror, 3)
                ]
                table.add_row(input_data, i)
                i += 1
            tk.messagebox.showinfo("Solution", f"The Root= {round(xi, 3)}")
    insert_button = CTkButton(master=frameL, text="Calculate", fg_color="#00246B", hover_color="#0000cd",
                              text_color="#CADCFC", command=insert_data)
    insert_button.pack(side='bottom')
    window.mainloop()
