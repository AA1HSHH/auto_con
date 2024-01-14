import os
import socket
import psutil
import requests
import time
import tkinter as tk
import subprocess
from requests.adapters import HTTPAdapter
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


def connect(user, passwd, num):

    if num == 0:
        print("重试失败")
        return
    num -= 1
    
    # 连接NJUPT-CMCC WLAN
    wlan_name = get_current_wlan_name()
    if wlan_name != "NJUPT-CMCC" or wlan_name == None:
        os.system("netsh wlan connect name=NJUPT-CMCC")

    # 获取ip地址
    net_interfaces = psutil.net_if_addrs()
    wlan_ip = None
    for interface, addresses in net_interfaces.items():
        if interface == "WLAN":
            wlan_ip = [addr.address for addr in addresses if addr.family == socket.AF_INET][0]
            break
    if wlan_ip == None:        
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
    except Exception as e:
        time.sleep(10)
        print("重试。。。。")
        connect(user, passwd, 5)
        
if __name__ == "__main__":
    connect("name","passwd",1)
