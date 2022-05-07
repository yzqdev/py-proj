
# pip配置
## 安装
### 导出python安装包环境
```shell

pip freeze > requirements.txt
```
### 导入requirements文件
```shell
pip install -r requirements.txt
```
一些命令
```shell
#升级pip
pip install -U pip
# 安装模块
pip install SomePackage              # 最新版本

pip install SomePackage==1.0.4       # 指定版本

pip install 'SomePackage>=1.0.4'     # 最小版本
#升级包
pip install --upgrade SomePackage
pip install -U SomePackage

#卸载包
pip uninstall <包名> 或 pip uninstall -r requirements.txt
#查看可以升级的包
pip list -o
```