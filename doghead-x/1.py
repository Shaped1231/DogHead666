print("欢迎使用" \
"1.关于" \
"2.文件" \
"3.桌面" \
"4.关闭")
import os
import time
while True:
    re = input()
    if re =="1":
        os.system('start winver')
    if re =="2":
        os.system('start explorer')
    if re =="3":
        os.system('start 2.sb3')
    if re =="4":
        break