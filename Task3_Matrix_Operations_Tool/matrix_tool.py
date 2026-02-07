import tkinter as tk
from tkinter import messagebox
import numpy as np

def parse_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        return None

def display_result(result):
    if isinstance(result, (int, float, np.float64, np.int64)):
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, str(result))
        return

    if isinstance(result, np.ndarray):
        result_text.delete("1.0", tk.END)
        formatted = "\n".join(["  ".join(map(lambda x: f"{x:.2f}", row)) for row in result])
        result_text.insert(tk.END, formatted)
        return

def get_matrices():
    A = parse_matrix(matrix_a_text.get("1.0", tk.END))
    B = parse_matrix(matrix_b_text.get("1.0", tk.END))
    return A, B

def add_matrices():
    A, B = get_matrices()
    if A is None or B is None:
        messagebox.showerror("Error", "Invalid matrix input.")
        return
    if A.shape != B.shape:
        messagebox.showerror("Error", "Matrices must have the same shape for addition.")
        return
    display_result(A + B)

def subtract_matrices():
    A, B = get_matrices()
    if A is None or B is None:
        messagebox.showerror("Error", "Invalid matrix input.")
        return
    if A.shape != B.shape:
        messagebox.showerror("Error", "Matrices must have the same shape for subtraction.")
        return
    display_result(A - B)

def multiply_matrices():
    A, B = get_matrices()
    if A is None or B is None:
        messagebox.showerror("Error", "Invalid matrix input.")
        return
    if A.shape[1] != B.shape[0]:
        messagebox.showerror("Error", "Number of columns in A must match rows in B.")
        return
    display_result(np.dot(A, B))

def transpose_matrix_a():
    A = parse_matrix(matrix_a_text.get("1.0", tk.END))
    if A is None:
        messagebox.showerror("Error", "Invalid matrix A input.")
        return
    display_result(A.T)

def transpose_matrix_b():
    B = parse_matrix(matrix_b_text.get("1.0", tk.END))
    if B is None:
        messagebox.showerror("Error", "Invalid matrix B input.")
        return
    display_result(B.T)

def determinant_a():
    A = parse_matrix(matrix_a_text.get("1.0", tk.END))
    if A is None:
        messagebox.showerror("Error", "Invalid matrix A input.")
        return
    if A.shape[0] != A.shape[1]:
        messagebox.showerror("Error", "Matrix A must be square for determinant.")
        return
    display_result(np.linalg.det(A))

def determinant_b():
    B = parse_matrix(matrix_b_text.get("1.0", tk.END))
    if B is None:
        messagebox.showerror("Error", "Invalid matrix B input.")
        return
    if B.shape[0] != B.shape[1]:
        messagebox.showerror("Error", "Matrix B must be square for determinant.")
        return
    display_result(np.linalg.det(B))

def clear_all():
    matrix_a_text.delete("1.0", tk.END)
    matrix_b_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("950x600")

title_label = tk.Label(root, text="Matrix Operations Tool", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

matrix_a_label = tk.Label(frame, text="Matrix A (space-separated values, new line for rows):", font=("Arial", 10, "bold"))
matrix_a_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

matrix_b_label = tk.Label(frame, text="Matrix B (space-separated values, new line for rows):", font=("Arial", 10, "bold"))
matrix_b_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

matrix_a_text = tk.Text(frame, width=40, height=10, font=("Consolas", 11))
matrix_a_text.grid(row=1, column=0, padx=10, pady=5)

matrix_b_text = tk.Text(frame, width=40, height=10, font=("Consolas", 11))
matrix_b_text.grid(row=1, column=1, padx=10, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="A + B", width=12, command=add_matrices)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_sub = tk.Button(button_frame, text="A - B", width=12, command=subtract_matrices)
btn_sub.grid(row=0, column=1, padx=5, pady=5)

btn_mul = tk.Button(button_frame, text="A x B", width=12, command=multiply_matrices)
btn_mul.grid(row=0, column=2, padx=5, pady=5)

btn_trans_a = tk.Button(button_frame, text="Transpose A", width=12, command=transpose_matrix_a)
btn_trans_a.grid(row=0, column=3, padx=5, pady=5)

btn_trans_b = tk.Button(button_frame, text="Transpose B", width=12, command=transpose_matrix_b)
btn_trans_b.grid(row=0, column=4, padx=5, pady=5)

btn_det_a = tk.Button(button_frame, text="Det(A)", width=12, command=determinant_a)
btn_det_a.grid(row=1, column=0, padx=5, pady=5)

btn_det_b = tk.Button(button_frame, text="Det(B)", width=12, command=determinant_b)
btn_det_b.grid(row=1, column=1, padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="Clear", width=12, command=clear_all, bg="red", fg="white")
btn_clear.grid(row=1, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
result_label.pack()

result_text = tk.Text(root, width=90, height=12, font=("Consolas", 12))
result_text.pack(pady=10)

root.mainloop()
