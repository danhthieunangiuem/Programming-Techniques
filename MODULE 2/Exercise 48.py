def input_sets_list():
    sets_list = []
    n = int(input("Number of list: "))
    for i in range(n):
        elements = input(f"Nhập các phần tử cho tập hợp {i + 1}, cách nhau bởi dấu phẩy: ")
        set_elements = set(map(int, elements.split(',')))  # Chuyển các phần tử thành kiểu số nguyên và tạo set
        sets_list.append(set_elements)
    return sets_list
def union_of_sets(sets_list):
    result_set = set()
    for s in sets_list:
        result_set.update(s)  # Add all elements from the current set to result_set
    return result_set
sets_list = input_sets_list()
result = union_of_sets(sets_list)
print("Hợp của tất cả các tập hợp là:", result)