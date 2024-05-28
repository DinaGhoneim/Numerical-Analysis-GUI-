from Gauss_Elimination import *
from Gauss_Jordan import *
from Cramer import *
from LU import *
from Gauss_Partial import *
from Jordan_Partial import *
from LU_Partial import *


def click2():
    window = CTk(fg_color='#CADCFC')
    window.geometry("500x500")
    window.title("Chapter Two")
    label = CTkLabel(master=window, text="Chapter Two Methods", font=("Times New Roman", 50), text_color="#00246B",
                     fg_color="#CADCFC")
    label.place(relx=0.5, rely=0.1, anchor="n")
    btn1 = CTkButton(master=window, text="Gauss Elimination", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Gauss_Elimination)
    btn1.place(relx=0.4, rely=0.3, anchor="e")
    btn5 = CTkButton(master=window, text="Partial Gauss", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Gauss_Partial)
    btn5.place(relx=0.4, rely=0.4, anchor="e")
    btn2 = CTkButton(master=window, text="LU Decomposition", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=LU_Decomp)
    btn2.place(relx=0.6, rely=0.3, anchor="w")
    btn8 = CTkButton(master=window, text="LU Partial", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=LU_Partial)
    btn8.place(relx=0.6, rely=0.4, anchor="w")
    btn3 = CTkButton(master=window, text="Cramer's Rule", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Cramer_Rule)
    btn3.place(relx=0.4, rely=0.6, anchor="e")
    btn4 = CTkButton(master=window, text="Gauss-Jordan", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Gauss_Jordan)
    btn4.place(relx=0.6, rely=0.6, anchor="w")
    btn6 = CTkButton(master=window, text="Jordan_Partial", fg_color="#00246B", hover_color="#0000cd",
                     text_color="#CADCFC", command=Jordan_Partial)
    btn6.place(relx=0.6, rely=0.7, anchor="w")
    window.mainloop()
