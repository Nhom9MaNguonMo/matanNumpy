# import numpy as np

# A=np.array([[1,2],[3,4]])


# B=np.array([[5,6]])

# A1=np.linalg.inv(A)
# print(A1)
# print(B.T)

# X=np.dot(A1,B.T)
# print("Nghiem  cua he : ",X)
import tkinter as tk
import numpy as np
from tkinter import messagebox
def taomatran():
    global mang1  # Sử dụng biến toàn cục để giữ các ô nhập liệu
    global mang2
    if(entry_num_eqns.get()=="" or entry_num_vars.get() ==""):
        messagebox.showinfo("Lỗi", "Vui lòng nhập đầy đủ")
        return
    num_eqns = int(entry_num_eqns.get())  # Lấy số phương trình
    num_vars = int(entry_num_vars.get())  # Lấy số ẩn
    # Xóa các ô nhập liệu cũ
    for widget in mangdauvao1.winfo_children():
        widget.destroy()

    mang1 = []  # Danh sách để lưu các ô nhập hệ số
    for i in range(num_eqns):
        row1 = []
        for j in range(num_vars):  # +1 để có cột giá trị sau dấu "="
            entry = tk.Entry(mangdauvao1, width=5)
            entry.grid(row=i, column=j)
            row1.append(entry)
        mang1.append(row1)
    mang2 = []  # Danh sách để lưu các ô nhập hệ số
    for i in range(num_eqns):
        row2 = []
        for j in range(num_vars):  # +1 để có cột giá trị sau dấu "="
            entry = tk.Entry(mangdauvao2, width=5)
            entry.grid(row=i, column=j)
            row2.append(entry)
        mang2.append(row2)

def tinhtoan():
    A=[]
    B=[]
    num_eqns = int(entry_num_eqns.get())
    num_vars = int(entry_num_vars.get())
    for i in range (num_eqns):
        row1 = []
        for j in range (num_vars):
            row1.append(float(mang1[i][j].get()))
        A.append(row1)
    for i in range (num_eqns):
        row2 = []
        for j in range (num_vars):
            row2.append(float(mang2[i][j].get()))
        B.append(row2)
    choice = choice_var.get()
    a=np.array(A)
    b=np.array(B)
    if choice == 1:
       tong=a+b
       messagebox.showinfo("Ket qua", str(tong)) 

    
            
            



# Hàm xử lý để tạo các ô nhập hệ số
def create_input_fields():
    try:
        global entries  # Sử dụng biến toàn cục để giữ các ô nhập liệu
        if(entry_num_eqns.get()=="" or entry_num_vars.get() ==""):
            messagebox.showinfo("Lỗi", "Vui lòng nhập đầy đủ")
            return
        num_eqns = int(entry_num_eqns.get())  # Lấy số phương trình
        num_vars = int(entry_num_vars.get())  # Lấy số ẩn
        # Xóa các ô nhập liệu cũ
        for widget in frame_inputs.winfo_children():
            widget.destroy()

        entries = []  # Danh sách để lưu các ô nhập hệ số
        for i in range(num_eqns):
            row = []
            for j in range(num_vars + 1):  # +1 để có cột giá trị sau dấu "="
                entry = tk.Entry(frame_inputs, width=5)
                entry.grid(row=i, column=j)
                row.append(entry)
            entries.append(row)
    except:
        messagebox.showinfo("Lỗi", "Vui lòng nhập đúng kiểu dữ liệu")
        return

# Hàm giải hệ phương trình
def solve_system():
    try:
        num_eqns = int(entry_num_eqns.get())
        num_vars = int(entry_num_vars.get())

        # Tạo ma trận hệ số và vector hằng số
        A = []
        B = []
        tong =0
        cot=0
        hang=0
        for i in range(num_eqns):
            row = []
            for j in range(num_vars):
                row.append(float(entries[i][j].get()))
                cot=cot+float(entries[i][j].get())
            hang=float(entries[i][num_vars].get())
            if(hang!=0 and cot==0):
                messagebox.showinfo("Kết quả", "Phuong trinh vo nghiem")
                return

            A.append(row)
            B.append(float(entries[i][num_vars].get()))
        for i in range(num_eqns):
            for j in range(num_vars+1):
                tong=tong+float(entries[i][j].get())
        if(tong==0):
            messagebox.showinfo("Kết quả", "Phuong trinh vo so nghiem")
        
            return
        A = np.array(A)
        B = np.array(B)
       

        

        # # Giải hệ phương trình bằng ma trận nghịch đảo
        # X = np.linalg.solve(A, B)

        A1=np.linalg.inv(A)
        print(A1)
        print(B)
        print(B.T)
        X=np.dot(A1,B.T)


        # Hiển thị kết quả
        result = "\n".join([f"x{i+1} = {X[i]:.2f}" for i in range(len(X))])
        messagebox.showinfo("Kết quả", result)
    except ValueError:

        messagebox.showerror("Lỗi", "Vui lòng nhập đúng kiểu dữ liệu trong mảng hoặc nhập đúng số phương trình,số ẩn")
    except Exception as e:
        messagebox.showerror("Lỗi", "Vui lòng nhập hệ số trước và làm từng bước")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm đại số")


# Nhãn và ô nhập cho số phương trình và số ẩn
label_num_eqns = tk.Label(root, text="Số phương trình:")
label_num_eqns.grid(row=0, column=0)
entry_num_eqns = tk.Entry(root)
entry_num_eqns.grid(row=0, column=1)

label_num_vars = tk.Label(root, text="Số ẩn:")
label_num_vars.grid(row=1, column=0)
entry_num_vars = tk.Entry(root)
entry_num_vars.grid(row=1, column=1)


# Nút tạo ô nhập hệ số
btn_create_fields = tk.Button(root, text="Tạo ô nhập hệ số", command=create_input_fields)
btn_create_fields.grid(row=2, column=0, columnspan=2)

# Khung để chứa các ô nhập hệ số
frame_inputs = tk.Frame(root)
frame_inputs.grid(row=3, column=0, columnspan=2)

# Nút giải hệ phương trình
btn_solve = tk.Button(root, text="Giải hệ phương trình", command=solve_system)
btn_solve.grid(row=4, column=0, columnspan=2)

global choice_var
choice_var = tk.StringVar(value='1')
tk.Radiobutton(root, text="Cộng ma trận", variable=choice_var, value='1').grid(row=6, column=0)
tk.Radiobutton(root, text="Trừ ma trận", variable=choice_var, value='2').grid(row=7, column=0)
tk.Radiobutton(root, text="Nhân ma trận", variable=choice_var, value='3').grid(row=8, column=0)
tk.Radiobutton(root, text="Chia ma trận", variable=choice_var, value='4').grid(row=9, column=0)

# Nút tạo ô nhập hệ số
tao_ma_tran = tk.Button(root, text="Nhập ma trân", command=taomatran)
tao_ma_tran.grid(row=10, column=0, columnspan=2)


labelmang1 = tk.Label(root, text="Ma Trận 1:")
labelmang1.grid(row=11, column=0)
mangdauvao1 = tk.Frame(root)
mangdauvao1.grid(row=12, column=0, columnspan=2)
labelmang2 = tk.Label(root, text="Ma Trận 2:")
labelmang2.grid(row=13, column=0)
mangdauvao2 = tk.Frame(root)
mangdauvao2.grid(row=14, column=0, columnspan=2)

btn_calc = tk.Button(root, text="Tính toán", command=tinhtoan)
btn_calc.grid(row=15, column=0, columnspan=2)

# Chạy vòng lặp chính của giao diện
root.mainloop()