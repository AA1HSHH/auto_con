import os
import sys
import socket
import psutil
import requests
import time
from tkinter import messagebox
import subprocess
import re
def get_current_wlan_name():
    try:
        # 使用 netsh 命令获取 WLAN 名称
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # 寻找 WLAN 名称所在行
        for line in output_lines:
            if "SSID" in line:
                wlan_name = line.split(":")[1].strip()
                return wlan_name

        return None  # 未找到 WLAN 名称

    except Exception as e:
        print(f"发生错误: {e}")
        return None

err = None
def retry(user, passwd, num, e):
    time.sleep(10)
    err = e
    print("重试第%d次。。。。"% (5 - num))
    connect(user, passwd, num)

def connect(user, passwd, num):
    global err
    if num == 0:
        print("重试失败")
        print(err)
        os.exit(1)
    num -= 1
    
    # 连接NJUPT-CMCC WLAN
    wlan_name = get_current_wlan_name()
    if wlan_name != "NJUPT-CMCC" or wlan_name == None:
        os.system("netsh wlan connect name=NJUPT-CMCC")

    # 获取ip地址
    net_interfaces = psutil.net_if_addrs()
    wlan_ip = None
    for interface, addresses in net_interfaces.items():
        if "WLAN" in interface:
            wlan_ip = [addr.address for addr in addresses if addr.family == socket.AF_INET][0]
            break
    if wlan_ip == None:        
        retry(user, passwd, num, Exception("未分配IP"))

    # 构造请求体
    url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C"+user+"%40cmcc&user_password="+passwd+"&wlan_user_ip="+wlan_ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=3140&lang=zh"
    try:
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200 and ("错误" not in response.text):
            # 打印响应内容
            print("连接成功")
        else:
            print(f"失败: {response.status_code} - {response.text}")
            msg = re.search(r'"msg":"(.*?)"', response.text)
            messagebox.showwarning("警告", "网页报错：" + msg.group(1))
    except requests.exceptions.ProxyError as e:
        err = e
        messagebox.showwarning("警告","取消代理后关闭对话框重试\n 或将`p.njupt.edu.cn;`添加系统代理设置")
        connect(user, passwd, num)
    except Exception as e:
        retry(user, passwd, num, e)
        
if __name__ == "__main__":
    assert (len(sys.argv) == 3 or len(sys.argv) == 1), "参数错误:参数格式为 python net.py 或者 python net.py 用户名 密码"
    
    if len(sys.argv) == 3:
        user = sys.argv[1]
        passwd =  sys.argv[2]
    elif len(sys.argv) == 1:
        user = input("请输入用户名:")
        passwd =input("请输入密码:")
        
    connect(user,passwd,5)
