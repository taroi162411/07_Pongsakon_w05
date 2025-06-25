import os
from pathlib import Path

os_name = os.name
os_path = os.getcwd()
os_user = os.getenv("USERNAME")

print(os_name)
print(os_path)
print(os_user)

# ทำงานใน path
current_path = Path.cwd()
# print(current_path)
# สร้าง folder
make_folder = current_path / "test123"
make_folder.mkdir(exist_ok = True)

# สร้าง file
make_file = current_path / "test.txt"
make_file.write_text("Hello mamy!!!")

print(f"ขนาดไฟล์คือ {make_file.stat().st_size} ไบต์")

content = make_file.read_text()
print(content)

content_test = make_file
content = content_test.read_text()
print(content)