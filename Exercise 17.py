def decimal_to_hexadecimal(n):
    # Trường hợp cơ sở: nếu n là 0-16, trả về chính nó
    hex_digits = "0123456789ABCDEF"

    # Trường hợp cơ sở: nếu n nhỏ hơn 16, trả về chữ số thập lục phân tương ứng
    if n < 16:
        return hex_digits[n]
    # Gọi đệ quy với n chia 16 và thêm phần dư (n % 16) vào kết quả
    return decimal_to_hexadecimal(n // 16) + hex_digits[n % 16]
n=int(input('n:'))
print(decimal_to_hexadecimal(n))
