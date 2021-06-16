## 配置环境

打开你的命令行界面，找到一个目录位置，拉取仓库

```bash
git clone https://se.jisuanke.com/course/python39.git
```

拉取完成后进入目录

```bash
cd python39
```

进行构建（注意最后一个表示当前位置的 `.` 不能丢了）

```bash
docker build -t "python:39" .
```

## 进入环境

首次进入：

```bash
docker run -it -p 8000:8000 --name python39 python:39
```

之后进入

```bash
docker start python39
docker exec -it python39 /bin/bash
```
