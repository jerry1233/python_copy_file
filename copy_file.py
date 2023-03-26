import os
import shutil
import sys

# 获取当前脚本所在目录的路径
current_dir = os.path.dirname(sys.executable)

# 定义启动目录路径
startup_dir = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

# 定义目标文件路径
dst_path = os.path.join(startup_dir, "example.exe")

# 拷贝文件
try:
    shutil.copy(sys.executable, dst_path)
    print("文件拷贝成功！")
except Exception as e:
    print("文件拷贝失败：", e)

input("按回车键退出")