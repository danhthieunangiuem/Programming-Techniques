def calculate_statistics(students_data):
    # Kiểm tra danh sách rỗng
    if not students_data:
        return {'average_score': 0, 'average_age': 0}

    # Tính tổng điểm và tổng tuổi
    total_score = sum(student['score'] for student in students_data)
    total_age = sum(student['age'] for student in students_data)

    # Tính trung bình
    average_score = total_score / len(students_data)
    average_age = total_age / len(students_data)

    # Lưu vào dictionary kết quả
    statistics = {
        'average_score': round(average_score, 2),
        'average_age': round(average_age, 2)
    }
    return statistics
# Dữ liệu ví dụ
students_data = [
    {'name': 'Phúc', 'age': 20, 'score': 85},
    {'name': 'Thanh', 'age': 22, 'score': 75},
    {'name': 'Thản', 'age': 21, 'score': 90}
]
# Chạy hàm và in kết quả
result = calculate_statistics(students_data)
print(result)
