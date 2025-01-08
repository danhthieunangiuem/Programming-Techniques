import tkinter as tk
from tkinter import messagebox

def check_doi_xung(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check_palindrome():
    # Lấy chuỗi từ ô nhập liệu
    s = entry.get()
    # Kiểm tra chuỗi đối xứng
    if check_doi_xung(s):
        result_label.config(text="Chuỗi bạn nhập đối xứng")
    else:
        result_label.config(text="Chuỗi bạn nhập không đối xứng")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Kiểm tra chuỗi đối xứng")
root.geometry("400x200")

# Nhãn và ô nhập liệu
entry_label = tk.Label(root, text="Nhập một chuỗi:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Nút để kiểm tra chuỗi
check_button = tk.Button(root, text="Kiểm tra", command=check_palindrome)
check_button.pack(pady=10)

# Nhãn để hiển thị kết quả
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Vòng lặp sự kiện chính
root.mainloop()
