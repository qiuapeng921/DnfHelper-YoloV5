# 配置视频

视频地址: [https://www.bilibili.com/video/BV1Mp4y1n7HR/](https://www.bilibili.com/video/BV1Mp4y1n7HR/)

## 需求环境
1. **操作系统:** Win10 或 Win11 64位系统（必须）
2. **显卡要求:** 最好有 NVIDIA 显卡，显卡驱动更新到最新版本，最好是30系列以上（可选，建议）
3. **网络要求:** 全局科学上网，因为安装包需要从外网下载（必须）

## 安装步骤
1. **安装 Python3.10.8:**
    - 下载地址: [Python官网](https://www.python.org/downloads/)
    - 安装时勾选添加路径到系统环境变量，推荐手动添加环境变量 `PYTHONDONTWRITEBYTECODE=1`

2. **安装 CUDA (可选):**
    - 下载地址: [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)
    - 自定义安装，仅选择安装 CUDA，其他不选

3. **安装 PyTorch:**
    - 下载地址: [PyTorch](https://pytorch.org/get-started/locally)
    - 选择稳定版本，Windows系统，Pip安装，选择最新的 CUDA 版本（或选择 CPU）

4. **安装 YOLO依赖:**
    - 进入yolov5-7.0目录执行命令：`pip install -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt`

5. **安装 Git:**
    - 下载地址: [Git](https://git-scm.com/download/win)

6. **测试识别:**
    - 进入 yolo 目录，执行命令：`python detect.py --weights yolov5s.pt --source data/images/bus.jpg`

7. **测试训练:**
    - 进入 yolo 目录，执行命令：`python train.py --weights yolov5s.pt --epochs 300 --batch-size 16 --workers 8 --data ../datasets/coco8/coco8.yaml`

8. **测试模型格式转换:**
    - 进入 yolo 目录，执行命令：`python export.py --weights yolov5s.pt --simplify --include onnx`

9. **环境配置完成!**
    - 观看视频教程学习如何搭配插件使用

> 注意: YOLO路径中不要包含非英文字符。

## 免责声明

程序是免费开源的产品，仅用于学习交流使用！       
不可用于任何违反`中华人民共和国(含台湾省)`或`使用者所在地区`法律法规的用途。      
因为作者即本人仅完成代码的开发和开源活动`(开源即任何人都可以下载使用)`，从未参与用户的任何运营和盈利活动。    
且不知晓用户后续将`程序源代码`用于何种用途，故用户使用过程中所带来的任何法律责任即由用户自己承担。

## JetBrains 支持的项目

非常感谢 Jetbrains 友好地为我提供了一个许可，让我可以从事这个项目和其他开源项目。

[![](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg)](https://www.jetbrains.com/?from=https://github.com/qiuapeng921)

## License

MIT
