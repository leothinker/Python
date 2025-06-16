import cv2
import numpy as np


def crop_black_border(img, thresh=10):
    """
    自动裁剪图片的黑色边框。
    :param img: 输入图像（BGR 或 灰度）。
    :param thresh: 阈值，小于等于此值的像素视为“黑”。
    :return: 裁剪后的图像。
    """
    # 确保处理灰度图
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()

    # 创建二值图：黑色背景为0，内容为255
    _, bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

    # 查找所有非零（内容）像素的位置
    coords = np.column_stack(np.where(bw > 0))
    if coords.size == 0:
        # 全图都很暗，直接返回原图
        return img
    # 获取内容区域的边界框
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1  # +1 为包含结束行/列

    # 裁剪并返回
    return img[y0:y1, x0:x1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print(f"用法：python {sys.argv[0]} input.jpg output.jpg")
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]
    img = cv2.imread(in_path)
    if img is None:
        print("无法读取图片，请检查路径。")
        sys.exit(1)

    cropped = crop_black_border(img, thresh=10)
    cv2.imwrite(out_path, cropped)
    print(f"已保存裁剪结果：{out_path}")
