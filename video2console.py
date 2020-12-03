import cv2
import time


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


def flow(filename, slide=100):
    cap = cv2.VideoCapture(filename)
    print(cap.get(cv2.CAP_PROP_FPS))
    i = 0
    try:
        while cap.isOpened():
            i += 1
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if i // slide % 2 == 0:
                print(transform(gray, double=True))
            else:
                print(transform(gray, double=False))
            if frame is None:
                continue
            time.sleep(0.02)
    except:
        pass
    print("\033[2J 耗子尾汁！")


if __name__ == '__main__':
    file_in = "cxk.flv"
    flow(file_in)
