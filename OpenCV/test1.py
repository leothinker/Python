import os

import cv2
import numpy as np


def remove_black_border(src_path, dst_path, thresh=5, min_cover=0.5):
    """
    去除单张图像外围黑边并保存结果

    参数:
        src_path (str): 输入图像路径
        dst_path (str): 输出图像路径
        thresh (int): 灰度阈值，低于该值视为“黑边”
        min_cover (float): 区域中至少有多少比例像素为黑才认为是边
    """
    img = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"❌ 无法读取图像：{src_path}")
        return
    h, w = img.shape
    _, bin_img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
    # 找连通区域
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 找最大的连通区域
    cnt = max(contours, key=cv2.contourArea)
    x, y, cw, ch = cv2.boundingRect(cnt)
    # 判断该区域是否真的覆盖边缘
    area_ratio = cv2.contourArea(cnt) / (w * h)
    if area_ratio < min_cover:
        print(f"⚠️ 边缘区域不显著，跳过：{src_path}")
        save_img = cv2.imread(src_path)
    else:
        save_img = cv2.imread(src_path)
        save_img = save_img[y : y + ch, x : x + cw]
    cv2.imwrite(dst_path, save_img)


def batch_process(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for fname in os.listdir(input_folder):
        src = os.path.join(input_folder, fname)
        if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            continue
        dst = os.path.join(output_folder, fname)
        remove_black_border(src, dst)


if __name__ == "__main__":
    batch_process("input_images", "cropped_images")
    print("✅ 处理完成")
