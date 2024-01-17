import cv2
import numpy as np
import pyautogui

def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame


def predict_function(processed_image):
    return 1


def main():
    try:
        # 请替换为您的模型加载代码
        # model = load_your_model()
        while True:
            # 获取屏幕截图
            screen_image = capture_screen()

            # 在这里添加您的图像处理代码，例如缩放、裁剪、预处理等
            processed_image = screen_image  # 临时示例，通常需要图像处理步骤

            # 请替换为您的模型推理代码
            prediction = predict_function(processed_image)

            # 处理模型输出，例如打印或执行其他操作
            print("Model Prediction:", prediction)

            # 调整窗口大小
            screen_image = cv2.resize(screen_image, (640, 480))  # 请根据需要调整大小
            processed_image = cv2.resize(processed_image, (640, 480))  # 请根据需要调整大小
            # 显示原始截图和处理后的图像（可选）
            cv2.imshow("Original", screen_image)
            cv2.imshow("Processed", processed_image)

            # 检测键盘按键，按下'q'键退出循环
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    except KeyboardInterrupt:
        print("Ctrl+C detected. Exiting...")

    finally:
        # 关闭窗口
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
