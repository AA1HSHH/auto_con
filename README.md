# NJUPT自动连接脚本
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
- 使用定时任务定时执行程序，并且参数列表中添加用户名和密码


## 定时执行
可参考 https://www.cnblogs.com/sui776265233/p/13602893.html

本机配置了

![图片](https://raw.githubusercontent.com/AA1HSHH/auto_con/master/img.png)

第一项定时任务执行，可用于长期在线主机

第二项电脑启动时执行

## 报错
### ProxyError
可向系统代理设置添加`p.njupt.edu.cn;`
## 致谢
GPT3.5

https://github.com/Yolumia/NJUPT-NETWORK


