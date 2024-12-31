def analyze_string(s):
    vowels = "aeiouAEIOU"
    num_upper = 0
    num_lower = 0
    num_digits = 0
    num_special = 0
    num_spaces = 0
    num_vowels = 0
    num_consonants = 0

    for char in s:
        if char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1

        if char.isdigit():
            num_digits += 1
        elif char.isspace():
            num_spaces += 1
        elif char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif not char.isalnum():
            num_special += 1

    print(f"Số chữ IN HOA: {num_upper}")
    print(f"Số chữ in thường: {num_lower}")
    print(f"Số chữ là chữ số: {num_digits}")
    print(f"Số chữ là ký tự đặc biệt: {num_special}")
    print(f"Số chữ là khoảng trắng: {num_spaces}")
    print(f"Số chữ là nguyên âm: {num_vowels}")
    print(f"Số chữ là phụ âm: {num_consonants}")


# Nhập chuỗi từ người dùng
input_string = input("Nhập vào một chuỗi: ")
analyze_string(input_string)