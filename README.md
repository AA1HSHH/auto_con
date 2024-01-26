<p align="center">
  <picture>
    <source width="500px" media="(prefers-color-scheme: dark)">
    <img src="icon.svg" width="500px">
  </picture>
</p>

# NJUPT CMCC自动连接脚本
## 环境安装
```
conda create -n net python=3.8
conda activate net
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple psutil requests 
```
## 执行(两种方法)
1. 直接执行python脚本
```
cd AUTO_CON
conda activate net
python net.py 用户名 密码
```
2. 执行打包好的程序
- 双击 net.exe 并且输入用户名和密码
## 任务计划程序-启动程序配置
可参考进行配置 https://www.cnblogs.com/sui776265233/p/13602893.html

1. 直接执行python脚本
程序或脚本输入`D:\Program\miniconda3\envs\net\python.exe`
添加参数输入`/path/to/auto_con/net.py "用户名" "密码"`

2. 执行打包好的程序
程序或脚本输入`e:/path/to/net.exe`
添加参数输入`"用户名" "密码"`
### 触发器配置

本机配置了

![图片](https://raw.githubusercontent.com/AA1HSHH/auto_con/master/img.png)

第一项定时任务执行，可用于长期在线主机

第二项电脑启动时执行

## 报错
### 取消代理
可向`参数设置`-`系统代理`设置中添加`*njupt;`
## 参考
GPT3.5

https://github.com/Yolumia/NJUPT-NETWORK

## 参与者


