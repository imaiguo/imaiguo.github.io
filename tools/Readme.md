
# txt文件GB2312转换 utf-8格式

## Debian环境部署

设置python虚拟环境
```bash
> sudo apt install python3-venv python3-pip -y
> mkdir /opt/Data/PythonVenv
> cd /opt/Data/PythonVenv
> python3 -m venv python
> source /opt/Data/PythonVenv/python/bin/activate
```

## 安装依赖
```bash
> cd tools
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
>
```


## 参考 https://www.codeleading.com/article/97283947939/