from mysite.settings import MEDIA_ROOT
import os
import cv2


def find_calibration(sizeX, sizeY, image, size, step=5):
    """
    SizeX, SizeY - размер области
    size - размер стороны квадрата в которых ищется калибровка
    """
    cord = []
    for i in range(0, sizeY, step):
        for j in range(0, sizeX, step):
            roi = image[i:i + size, j:j + size]
            if (step * step - cv2.countNonZero(roi)) / (step * step) * 100 > 85:
                cord.append((i, j))
    for i in cord:
        image[i[0]:i[0] + size, i[1]:i[1] + size] = size * [255]
    return image


def count_black_pix(img):
    path = os.path.abspath(os.path.join(MEDIA_ROOT, img.image.name))
    print(path)
    image = cv2.imread(path, 0)
    image = image[:image.shape[0] - 20, 80:]
    sizeX = image.shape[1]
    sizeY = image.shape[0]
    image = find_calibration(sizeX, sizeY, image, 10)
    res = {}
    tho_hour_size = 330
    for i in range(0, 6):
        res[(i, i + 1)] = round(((tho_hour_size * sizeX) - cv2.countNonZero(
            image[i * tho_hour_size:i * tho_hour_size + tho_hour_size, :])) / (tho_hour_size * sizeX) * 100, 2)
    res[(6, 8)] = round(((sizeX * sizeY) - cv2.countNonZero(image)) / (sizeX * sizeY) * 100, 2)
    return res
