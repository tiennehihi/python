# Định nghĩa hàm
# def nhan(a, b):
#     'Ham cho phep tinh nhan 2 so'
#     return a * b
#
#
# # goi ham
# x = 4
# y = 9
# ketqua = nhan(x, y)
# print('Ket qua = ', ketqua)




# Viết một chương trình Python mô tả một chiếc máy tính (Calculator), trong đó có các hàm tính
# toán đại số cơ bản như sau:
# Danh sách các hàm như sau:
# sum(int num1, int num2): Cộng giá trị của hai số, trả về tổng giá trị của hai số.
# minus(int num1, int num2): Trừ giá trị của hai số, trả về hiệu của hai số.
# divide(int num1, int num2): Chia giá trị của hai số, trả về kết quả phép chia giá trị của hai
# số.
# multiple(int num1, int num2): Nhân giá trị của hai số, trả về kết quả phép nhân giá trị của
# hai số.
# Giá trị của hai số sẽ được nhập vào từ bàn phím. Yêu cầu: Sau khi người dùng nhập 2 số vào từ
# bàn phím, hãy gọi các hàm nói trên, sau đó in ra kết quả

def sum(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def divede(num1, num2):
    return num1/num2
def multiple(num1, num2):
    return num1*num2

a = float(input())
b = float(input())
print(sum(a, b))
print(minus(a, b))
print(divede(a, b))
print(multiple(a, b))
