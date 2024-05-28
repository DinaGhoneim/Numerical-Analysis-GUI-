from customtkinter import *
import tkinter as tk
from sympy import *
import numpy as np

it = 0
def Cramer_Rule():
    it = 0


    def Cramer():
        def back_substitution(matrix):
            n = len(matrix)
            x = [0] * n
            for i in range(n - 1, -1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - sum) / matrix[i][i]

            return x

        def display_matrix(matrix, title, factor="", it=0):
            Steps.insert(END, f"{title}:\n{matrix[0]} \n{factor}")
            it += 1
            for row in range(1, len(matrix)):
                Steps.insert(END, (f"{matrix[row]}\n"))
                it += 1
            Steps.insert(END, "\n", "\n", "\n", "\n")#
            it += 1
            return it

        def determinant(m):

            determinant_sum = (m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))) - (
                    m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))) + (
                                      m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0])))

            return determinant_sum

        def dA(matrix):
            A = []
            B = [matrix[0][3], matrix[1][3], matrix[2][3]]
            it = display_matrix(B, "B")
            matrix = np.delete(matrix, 3, 1)
            det_A = determinant(matrix)
            A.append(det_A)
            it = display_matrix(matrix, f"The First Matrix: A,And its det = {det_A}")
            A1 = np.copy(matrix)
            A1[:, 0] = B

            A2 = np.copy(matrix)
            A2[:, 1] = B

            A3 = np.copy(matrix)
            A3[:, 2] = B
            A.append(determinant(A1))
            A.append(determinant(A2))
            A.append(determinant(A3))
            it= display_matrix(A1, f"Matrix: A_1,And its det = {A[1]}")
            it = display_matrix(A2, f"Matrix: A_2,And its det = {A[2]}")
            it = display_matrix(A3, f"Matrix: A_3,And its det = {A[3]}")
            return A

        def solve():
            global it
            matrix = []
            for i in range(rows):
                matrix.append([float(entry_grid[i][j].get()) for j in range(columns)])

            A = dA(matrix)
            x = [A[1] / A[0], A[2] / A[0], A[3] / A[0]]
            Steps.insert(END, f"Solution: \nx{1} = {x[0]:.2f}\n")
            for i in range(1, rows):
                Steps.insert(END, f"x{i + 1} = {x[i]:.2f}\n")

        window = CTk(fg_color='#CADCFC')
        window.geometry("450x450")
        window.title("Cramer's Rule")
        frames = []
        for i in range(rows):
            frames.append(CTkFrame(master=window, fg_color="#CADCFC"))
            frames[i].pack(side="top", fill="both" )

        entry_grid = []
        for i in range(rows):
            entry_grid.append([])
            for j in range(columns):
                if j == columns - 1:
                    CTkLabel(window, text=" = ").pack(side="left", padx=5, pady=5, in_=frames[i])
                entry = CTkEntry(master=window, fg_color="white", width=100, corner_radius=500)
                entry.pack(side="left", padx=5, pady=5, in_=frames[i])
                entry_grid[i].append(entry)
        solve_button = CTkButton(window, text="Solve", fg_color="#00246B", hover_color="#0000cd",
                                 text_color="#CADCFC", command=solve)
        solve_button.pack(side="bottom")

        frameT = CTkScrollableFrame(window, fg_color='#CADCFC')
        frameT.pack(fill='both', side='top', expand=True)
        Steps = tk.Text(frameT, height=25, width=100, bg="white")
        Steps.pack(fill='both', side='top', expand=True)

        window.mainloop()

    def enter():
        global rows
        global columns
        rows = int(row_entry.get())
        columns = int(col_entry.get())
        Cramer()

    window = CTk(fg_color='#CADCFC')
    window.geometry("600x600")
    window.title("Cramer's Rule")
    label1 = CTkLabel(master=window, text="Cramer's Rule", font=("Times New Roman", 50),
                      text_color="#00246B", fg_color="#CADCFC")
    label1.place(relx=0.5, rely=0.1, anchor="n")
    row_label = CTkLabel(master=window, text=" Row : ", font=("Times New Roman", 25), text_color="black",
                         fg_color="#CADCFC")
    row_label.place(relx=0.2, rely=0.4, anchor="e")
    row_entry = CTkEntry(master=window, placeholder_text="3", text_color="black", width=120)
    row_entry.place(relx=0.4, rely=0.4, anchor="e")
    col_label = CTkLabel(master=window, text=" Col : ", font=("Times New Roman", 25), text_color="black",
                         fg_color="#CADCFC")
    col_label.place(relx=0.6, rely=0.4, anchor="w")
    col_entry = CTkEntry(master=window, placeholder_text="4", text_color="black", width=120)
    col_entry.place(relx=0.7, rely=0.4, anchor="w")

    btn1 = CTkButton(master=window, text="Submit", fg_color="#00246B", hover_color="#0000cd", text_color="#CADCFC",
                     command=enter)
    btn1.place(relx=0.5, rely=0.5, anchor="center")
    window.mainloop()



