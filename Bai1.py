# Tuple product_info ban đầu có 4 phần tử
# Phần tử "SP001" đang nằm ở index 0
# Dòng product_code = product_info[1] lấy sai mã sản phẩm vì mã sản phẩm nằm ở index 0, không phải index 1
# Phần tử "Áo polo nam" đang nằm ở index 2
# Dòng product_name = product_info[2] lấy sai tên sản phẩm vì tên sản phẩm nằm ở index 1, không phải index 2
# Dòng product_length = product_info.length() gây lỗi vì tuple không có phương thức .length()
# Muốn đếm số phần tử trong tuple, cần dùng hàm len()
# Dòng product_info[3] = 279000 không hợp lệ vì tuple là kiểu dữ liệu bất biến, tuyệt đối không cho phép sửa trực tiếp giá trị sau khi đã tạo
# Muốn cập nhật giá bán từ 299000 thành 279000, cần tạo một tuple mới
# Code đúng:

product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_code = product_info[0]

product_name = product_info[1]

product_length = len(product_info)

product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)