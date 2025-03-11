from MODULE4.Exercise85.libs.DataConnector import DataConnector

dc=DataConnector()
#Lấy toàn bộ nhân viên:
employees=dc.get_all_employees()
print("Danh sách nhân viên:")
for e in employees:
    print(e)
#Lấy toàn bộ tài sản:
assets=dc.get_all_assets()
print("Danh sách tài sản:")
for a in assets:
    print(a)
#Lấy toàn bộ danh sách phân công quản lý tài sản:
aes=dc.get_all_employee_assets()
print("Danh sách phân công quản lý tài sản:")
for ae in aes:
    print(ae)

#Test chức năng đăng nhập hệ thống:
uid="danh"
pwd="123456789"
emp=dc.login(uid,pwd)
if emp!=None:
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")
