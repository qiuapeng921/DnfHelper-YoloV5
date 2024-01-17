import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab
import time
import keyboard
import os

# 定义进程的窗口标题
target_window_title = "地下城与勇士：创新世纪"

# 获取目标窗口
target_window = gw.getWindowsWithTitle(target_window_title)[0]

# 设置截图间隔（秒）
capture_interval = 3

# 设置热键
toggle_hotkey = "end"
save_images = False

# 设置保存图片的根目录
base_save_path = "./data/images/"

# 注册热键切换保存图片状态
keyboard.add_hotkey(toggle_hotkey, lambda: toggle_save_images())


def toggle_save_images():
    global save_images
    save_images = not save_images
    print(f"Save Images: {save_images}")

    # 如果需要保存图片，创建一个新的文件夹
    if save_images:
        current_time_folder = time.strftime("%Y%m%d%H%M%S")
        current_save_path = os.path.join(base_save_path, current_time_folder)
        os.makedirs(current_save_path, exist_ok=True)

        print(f"New folder created: {current_save_path}")

        # 开始保存图片
        save_images_in_folder(current_save_path)


def save_images_in_folder(folder_path):
    # 主循环
    while save_images:
        # 获取窗口位置和大小
        left, top, right, bottom = target_window.left, target_window.top, target_window.right, target_window.bottom

        # 获取屏幕截图
        screenshot = np.array(ImageGrab.grab(bbox=(left, top, right, bottom)))

        # 将截图保存为图片
        current_time = time.strftime("%Y%m%d%H%M%S")
        image_filename = f"{folder_path}/{current_time}.png"
        cv2.imwrite(image_filename, cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR))

        # 等待指定时间
        time.sleep(capture_interval)


def main():
    # 主循环
    try:
        while True:
            # 等待指定时间
            time.sleep(capture_interval)
    except KeyboardInterrupt:
        print("Program terminated by user.")


if __name__ == "__main__":
    main()
