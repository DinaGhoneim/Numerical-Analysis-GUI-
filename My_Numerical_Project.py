from Chapter_One import *
window = CTk(fg_color='#CADCFC')
window.geometry("500x500")
window.title("Welcome To Numerical Analysis Project")
label1 = CTkLabel(master=window, text="Numerical Analysis", font=("Times New Roman", 50), text_color="#00246B",
                  fg_color="#CADCFC")
label1.place(relx=0.5, rely=0.1, anchor="n")
btn1 = CTkButton(master=window, text="Chapter One", fg_color="#00246B", hover_color="#0000cd", text_color="#CADCFC",
                 command=click1)
btn1.place(relx=0.4, rely=0.5, anchor="e")
btn2 = CTkButton(master=window, text="Chapter Two", fg_color="#00246B", hover_color="#0000cd", text_color="#CADCFC",
                 command=click2)
btn2.place(relx=0.6, rely=0.5, anchor="w")
window.mainloop()
