import pandas as pd
df=pd.read_csv('../Exercise 124/employee.csv')
#print(df)
#0
new_employees = pd.DataFrame([
    {'Id': 5, 'Name': 'Minh Quân', 'Dob': '15/05/1999', 'Role': 'Data Scientist'},
    {'Id': 6, 'Name': 'Hải Yến', 'Dob': '30/09/2000', 'Role': 'UI/UX Designer'},
    {'Id': 7, 'Name': 'Bảo Long', 'Dob': '20/07/2001', 'Role': 'Project Manager'},
    {'Id': 8, 'Name': 'Lan Anh', 'Dob': '10/12/2002', 'Role': 'Software Engineer'},
    {'Id': 9, 'Name': 'Phương Nam', 'Dob': '05/11/1998', 'Role': 'Database Administrator'}
])
# Nối dữ liệu mới vào DataFrame hiện tại
df = pd.concat([df, new_employees], ignore_index=True)
#1 Xuất DataFrame sau khi cập nhật
print(df)
#2 Chuyển cột 'Dob' thành kiểu datetime
df['Dob'] = pd.to_datetime(df['Dob'], format='%d/%m/%Y')
# Nhập năm từ bàn phím
year = int(input("Nhập năm sinh cần lọc: "))
# Lọc nhân viên theo năm sinh nhập vào
filtered_df = df[df['Dob'].dt.year == year]
# Xuất dữ liệu ra màn hình
print(filtered_df)
#3 Chuyển cột 'Dob' thành kiểu datetime
df['Dob'] = pd.to_datetime(df['Dob'], format='%d/%m/%Y')
# Sắp xếp theo ngày sinh tăng dần (người già nhất sẽ ở đầu)
df_sorted = df.sort_values(by='Dob', ascending=True)
# Lấy 3 nhân viên lớn tuổi nhất
top_3_oldest = df_sorted.head(3)
# Xuất dữ liệu ra màn hình
print(top_3_oldest)
#4
# Lọc nhân viên có vai trò "Tester"
tester_employees = df[df['Role'] == 'Tester']
# Xuất dữ liệu ra màn hình
print(tester_employees)
#5
# Đếm số lượng nhân viên theo từng vai trò
role_counts = df['Role'].value_counts()
# Xuất dữ liệu ra màn hình
print(role_counts)