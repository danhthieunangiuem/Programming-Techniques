def unique_elements_from_tuples(data):
    unique_elements = set()
    for tuple_item in data:
        unique_elements.update(tuple_item)
    return list(unique_elements)

data = []
n = int(input("Nhập số lượng tuple: "))
for i in range(n):
    user_input = input(f"Nhập tuple thứ {i+1} (các số cách nhau bằng dấu cách, ví dụ: '1 2'): ")
    tuple_item = tuple(map(int, user_input.split()))
    data.append(tuple_item)

result = unique_elements_from_tuples(data)
print("Các phần tử duy nhất:", result)