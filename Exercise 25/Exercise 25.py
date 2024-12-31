def CheckDoiXung(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def main():
     print("Nhập 1 chuỗi:")
     s=input()
     if(CheckDoiXung(s)):
        print("Chuỗi bạn nhập đối xứng")
     else:
        print("Chuỗi bạn nhập không đối xứng")
while True:
     main()
     print("Tiếp không Thím?(c/k):",end='')
     s=input()
     if s=="k":
        break
print("CÁM ƠN THÍM")