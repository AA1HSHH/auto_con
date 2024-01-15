# NJUPT自动连接脚本
## 环境安装
```
conda create -n net python=3.8
conda activate net
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple psutil requests 
```
## 执行
第一个参数是conda环境的python位置，第二个参数是文件位置
```
D:/Program/miniconda3/envs/net/python.exe e:/code/py/auto_con/net.py
```
## 定时执行
可参考 https://www.cnblogs.com/sui776265233/p/13602893.html

本机配置了

![图片](https://raw.githubusercontent.com/AA1HSHH/auto_con/master/img.png)

第一项是定时任务
第二项是解锁屏幕的时候联网，远程主机不要配置

## 报错
### ProxyError
可向系统代理设置添加`p.njupt.edu.cn;`
## 致谢
GPT3.5

https://github.com/Yolumia/NJUPT-NETWORK


