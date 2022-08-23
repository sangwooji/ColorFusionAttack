import cv2
from PIL import Image
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import qrcode
import numpy as np

def gen_marker():
    marker = np.array(qrcode.make('marker')).astype(np.float32)
    marker = np.stack((marker,)*3, axis=-1)
    # qr = qrcode.QRCode()
    # qr.add_data('markerd')
    # marker = qr.make_image(fill_color='black', back_color='white')
    # plt.imshow(marker)
    # print (marker.shape)
    # plt.imshow(marker)
    # plt.show()
    return marker

image = Image.open('C:/Users/sangwooji/Desktop/새 폴더/colorfusion/frame1.png')
plt.imshow(image)
plt.show()

def check_qrcode(image_path='sampleqrcode2.jpg'):
    image = Image.open(image_path)
    results = decode(image)

    for i in range(len(results)):
        print (results[i].rect)
        print (results[i].polygon)

# plt.imshow(image)
# plt.show()

# cv2 detector
# qrCodeDetector = cv2.QRCodeDetector()
# decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
# qr_data = decodedText.split(',')
# qr_size = qr_data[0]
# top = qr_data[1]
# right = qr_data[2]
# bottom = qr_data[3]
# left = qr_data[4]
#
# print(f'Size: {qr_size}' + str(qr_data[5]))
# print(f'Top: {top}')
# print(f'Right: {right}')
# print(f'Bottom: {bottom}')
# print(f'Left: {left}')
# if points is not None:
#     pts = len(points)
#     print(pts)
#     for i in range(pts):
#         nextPointIndex = (i+1) % pts
#         cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
#         print(points[i][0])
#     print(decodedText)
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("QR code not detected")

