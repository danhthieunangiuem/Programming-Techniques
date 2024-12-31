def decimal_to_binary(n):
    # Trường hợp cơ sở: nếu n là 0 hoặc 1, trả về chính nó
    if n == 0:
        return "0"
    elif n == 1:
        return "1"

    # Gọi đệ quy với n chia 2 và thêm phần dư (n % 2) vào kết quả
    return decimal_to_binary(n // 2) + str(n % 2)


# Kiểm tra hàm với một số ví dụ
print(decimal_to_binary(14))
print(decimal_to_binary(17))
