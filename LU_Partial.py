from customtkinter import *
import tkinter as tk
from sympy import *
import numpy as np

it = 0
flag = False
swap = ""


def LU_Partial():
    flag = False
    swap = ""
    it = 0
    row_column_select = CTk()
    row_column_select.title("Enter Rows and Columns")
    rows = 3
    columns = 4

    def gauss_e():
        def display_matrix(matrix, title, factor="", it=0):
            Steps.insert(END, f"{title}:\n{matrix[0]} \n{factor}")
            it += 1
            for row in range(1, len(matrix)):
                Steps.insert(END, (f"{matrix[row]}\n"))
                it += 1
            Steps.insert(END, "\n", "\n", "\n", "\n")
            it += 1
            return it


        def partial_pivot_gauss_elimination(matrix):
            n = len(matrix)
            global it
            global tag
            global flag
            global swap
            global Choice
            display_matrix(matrix, "The First Matrix")
            B = []
            B.append(matrix[0][3])
            B.append(matrix[1][3])
            B.append(matrix[2][3])
            display_matrix(B, "B")
            # Create identity matrix (L) for LU decomposition
            L = np.identity(n)
            L = L.tolist()

            Factors = []
            for i in range(n):
                max_row = i
                for k in range(i + 1, n):
                    if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                        max_row = k

                # Swap rows in matrix and L
                if max_row != i:
                    if i == 1:
                        flag = True
                    matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                    display_matrix(matrix, f"After Swapping Row {i + 1} and {max_row + 1}")
                    swap += str(i)
                    swap += str(max_row)
                # Gaussian elimination
                for j in range(i + 1, n):
                    factor = matrix[j][i] / matrix[i][i]
                    Factors.append(factor)   # Fill L with elimination factors


                    # Update remaining elements in row j
                    for k in range(i, n+1):
                        matrix[j][k] -= factor * matrix[i][k]
                        matrix[j][k] = round(matrix[j][k], 3)
                    Steps.insert(END,f"The Multiplier : m{j + 1}{i + 1}={factor}\n")
                    display_matrix(matrix, f"After Using:{factor}R{i + 1} - R{j + 1}->R{j + 1}")

            L[1][0] = Factors[0]
            L[2][0] = Factors[1]
            L[2][1] = Factors[2]

            display_matrix(L, "Lower Triangular (L)")
            display_matrix(matrix, "Upper Triangular (U)")
            while len(swap):
                B[int(swap[0])], B[int(swap[1])] = B[int(swap[1])], B[int(swap[0])]
                display_matrix(B, f"After Pivoting Row {int(swap[0])+1} and {int(swap[1])+1} in B")
                swap = swap[2:]
            if flag:
                L[2][0], L[1][0] = L[1][0], L[2][0]
                display_matrix(L, f"After Swapping Multiplier M_21 with M_31 in L")
            # Now you have L (lower triangular) and U (upper triangular) matrices

            # Display L and U matrices (optional)


            return L, matrix, B

        def solve():
            global tag
            global it
            matrix = []
            for i in range(rows):
                matrix.append([float(entry_grid[i][j].get()) for j in range(columns)])

            # Perform LU decomposition
            L, U, B = partial_pivot_gauss_elimination(matrix.copy())  # Use a copy to avoid modifying the original matrix

            # Solve for intermediate vector C (L * C = B)
            n = len(matrix)
            C = np.zeros(n)  # Initialize C vector

            # Forward substitution to solve for C
            for i in range(n):
                sum = 0
                for j in range(i):
                    sum += L[i][j] * C[j]
                C[i] = B[i] - sum
            Steps.insert(END, "C values from L * C = B")
            Steps.insert(END, f"\nc{1} = {C[0]:.2f}\n")
            for i in range(1, rows):
                Steps.insert(END, f"c{i + 1} = {C[i]:.2f}\n")  # Add solution row to treeview
            # Solve for solution vector X (U * X = C)
            X = np.zeros(n)  # Initialize X vector

            # Backward substitution to solve for X
            for i in range(n - 1, -1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += U[i][j] * X[j]
                X[i] = (C[i] - sum) / U[i][i]
            # Display solution (X vector)
            Steps.insert(END, "\nX Values from U * X = C")
            # Display solution in treeview (optional)
            Steps.insert(END, f"\nSolution: \nx{1} = {X[0]:.2f}\n")
            for i in range(1, rows):
                Steps.insert(END, f"x{i + 1} = {X[i]:.2f}\n")  # Add solution row to treeview


        window = CTk(fg_color='#CADCFC')
        window.geometry("450x450")
        window.title("LU Decomposition with Partial Pivoting")
        frames = []
        for i in range(rows):
            frames.append(CTkFrame(master=window, fg_color="#CADCFC"))
            frames[i].pack(side="top", fill="both")

        entry_grid = []
        for i in range(rows):
            entry_grid.append([])
            for j in range(columns):
                if j==columns-1:
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
        gauss_e()

    window = CTk(fg_color='#CADCFC')
    window.geometry("600x600")
    window.title("LU Decomposition with Partial Pivoting")
    label1 = CTkLabel(master=window, text="LU with Partial Pivoting", font=("Times New Roman", 50),
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