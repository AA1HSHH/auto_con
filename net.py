import os
import socket
import psutil
import requests
import time
import tkinter as tk
from tkinter import messagebox
def connect(user, passwd):
    # 连接NJUPT-CMCC WLAN
    os.system("netsh wlan connect name=NJUPT-CMCC")
    # 处理 NameResolutionError ailed to resolve 'p.njupt.edu.cn'
    os.system("nslookup p.njupt.edu.cn")

    # 获取ip地址
    net_interfaces = psutil.net_if_addrs()
    wlan_ip = None
    for interface, addresses in net_interfaces.items():
        if interface == "WLAN":
            wlan_ip = [addr.address for addr in addresses if addr.family == socket.AF_INET][0]
            break
    if wlan_ip:
        print(f"WLAN IPv4 Address: {wlan_ip}")
    else:
        print("WLAN IPv4 Address not found.")
        os.exit(1)

    # 构造请求体
    url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C"+user+"%40cmcc&user_password="+passwd+"&wlan_user_ip="+wlan_ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=3140&lang=zh"
    
    try:
        response = requests.get(url)

        # 检查响应状态码
        if response.status_code == 200:
            # 打印响应内容
            print("连接成功")
        else:
            print(f"失败: {response.status_code} - {response.reason}")
    except requests.exceptions.ProxyError as e:
        # 创建主窗口
        root = tk.Tk()
        root.title("警告")
        root.geometry("300x100")
        text_label = tk.Label(root, text="关闭代理后重试！")
        text_label.pack(pady=20)
        # 启动主循环
        root.mainloop()
        
        print("重试。。。。")
        connect(user, passwd)
    except Exception as e:
        time.sleep(10)
        print("重试。。。。")
        connect(user, passwd)
        
if __name__ == "__main__":
    connect("user","passwd")
