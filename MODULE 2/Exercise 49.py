def sum_values_by_key(data):
    result_dict = {}

    for key, value in data:
        if key in result_dict:
            result_dict[key] += value  # Cộng dồn giá trị nếu key đã tồn tại
        else:
            result_dict[key] = value  # Thêm key mới với giá trị tương ứng

    return result_dict

# Dữ liệu ví dụ
data = [('a', 10), ('b', 20), ('a', 30), ('c', 40)]
# Chạy hàm và in kết quả
result = sum_values_by_key(data)
print(result)
