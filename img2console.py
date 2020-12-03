import cv2
import numpy as np
import matplotlib.pyplot as plt


def transform(raw, threshold=128, double=False):
    """
    :param raw: 原始图片
    :param threshold: 设为1的阈值
    :param double: 是否两倍图片
    :return: ascii图片
    """
    collector = []
    pxh, pxw = raw.shape
    base_w = 64 if double else 128
    base_h = 32 if double else 64
    step_w = int(pxh / base_w)
    step_h = int(pxh / base_h)
    for i in range(0, pxh, step_h):
        row = []
        for j in range(0, pxw, step_w):
            v = raw[i][j]
            if v > threshold:
                row.append(0)
            else:
                row.append(1)
        if double:
            collector.append(row + [" "] * 2 + row)
        else:
            collector.append(row)
    all_matrix = "\n".join(["".join(map(str, line)) for line in collector])
    if double:
        all_matrix += "\n\n" + all_matrix
    return "\033[2J" + all_matrix


def print_img(file_in):
    img = cv2.imread(file_in)  # 读取图像
    r, g, b = [img[:, :, i] for i in range(3)]
    img_gray = r * 0.299 + g * 0.587 + b * 0.114
    asciied = transform(img_gray)
    print(asciied)
    # plt.imshow(img_gray, cmap="gray")
    # plt.axis('off')
    # plt.show()


if __name__ == '__main__':
    file_in = "gj.jpg"
    print_img(file_in)

