from MODULE4.Exercise85.libs.JsonFileFactory import JsonFileFactory
from MODULE4.Exercise85.models.Employee_Asset import Employee_Asset

jff=JsonFileFactory()
filename="../dataset/employee_assets.json"
eas=jff.read_data(filename,Employee_Asset)
print("Danh sách phân công quản lý tài sản đọc từ file:")
for ea in eas:
    print(ea)
