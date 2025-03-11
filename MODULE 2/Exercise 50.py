def sort_scores(scores):
    # Sắp xếp theo giá trị giảm dần, giữ nguyên thứ tự ban đầu nếu giá trị bằng nhau
    sorted_scores = dict(sorted(scores.items(), key=lambda item: (-item[1], list(scores.keys()).index(item[0]))))
    return sorted_scores

scores = {'Hạnh': 85, 'Phúc': 75, 'Thanh': 85, 'Thản': 80}
result = sort_scores(scores)
print(result)
