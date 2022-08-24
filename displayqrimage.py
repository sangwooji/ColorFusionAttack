import cv2
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import matplotlib.pyplot as plt
import qrcode
import numpy as np

def get_marker(data='marker'):
    # marker = np.array(qrcode.make('marker')).astype(np.float32)
    qr = qrcode.QRCode(
        box_size=6,
        border=2
    )
    qr.add_data(data)
    marker = qr.make_image(fill_color='black', back_color='white')
    marker = np.stack((marker,)*3, axis=-1).astype(np.uint8)*255
    # plt.imshow(marker)
    # print (marker.shape)
    # plt.imshow(marker)
    # plt.show()
    return marker

def gen_image(image_path='C:/Users/sangwooji/Desktop/새 폴더/colorfusion/frame1.png'):
    height = width = 600
    canvas = np.ones([height,width,3]).astype(np.uint8)*255

    image = np.array(Image.open(image_path).convert('RGB')).astype(np.uint8)
    print (image.max())

    marker_size = get_marker().shape[0]

    canvas[0:marker_size, 0:marker_size] = get_marker('lefttop')
    canvas[-marker_size:, -marker_size:] = get_marker('rightbottom')
    canvas[0:marker_size, -marker_size:] = get_marker('righttop')
    canvas[-marker_size:, 0:marker_size] = get_marker('leftbottom')

    canvas[int(height/2-image.shape[0]/2):int(height/2+image.shape[0]/2), \
            int(width/2-image.shape[1]/2):int(width/2+image.shape[1]/2)] = image

    # Show
    # plt.imshow(canvas)
    # plt.show()

    # Save
    im = Image.fromarray(canvas)
    im.save('code.png')

def check_qrcode(image_path='sampleqrcode2.jpg'):
    # height = width = 600
    # canvas = np.ones([height,width,3]).astype(np.uint8)*255
    # marker_size = get_marker().shape[0]
    #
    # canvas[0:marker_size, 0:marker_size] = get_marker('lefttop')
    #
    # image = Image.fromarray(canvas)
    image = Image.open(image_path)
    results = decode(image, symbols=[ZBarSymbol.QRCODE])

    # plt.imshow(image)
    # plt.show()

    print (results)

    for i in range(len(results)):
        print (results[i].rect)
        print (results[i].polygon)
        print (results[i].data)

    return results

def crop_image(image_path, data, i_lefttop, i_righttop, i_leftbottom, i_rightbottom):
    image = np.array(Image.open(image_path).convert('RGB')).astype(np.uint8)

    for point in data:
        if point.data == b'lefttop':
            lefttop = point.polygon[i_lefttop]
        elif point.data == b'righttop':
            righttop = point.polygon[i_righttop]
        elif point.data == b'leftbottom':
            leftbottom = point.polygon[i_leftbottom]
        elif point.data == b'rightbottom':
            rightbottom = point.polygon[i_rightbottom]

    pts1 = np.float32([[lefttop.x, lefttop.y], [righttop.x, righttop.y], [leftbottom.x, leftbottom.y], [rightbottom.x, rightbottom.y]])
    # plt.imshow(image)
    # plt.scatter(pts1[:,0], pts1[:,1])
    # plt.show()
    pts2 = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    results = cv2.warpPerspective(image,M,(600,600))

    return results[300-112:300+112, 300-112:300+112]

    # pts1 = np.float32([[lefttop.x, lefttop.y], [612, 8], [380, 493], [785, 271]])
    # # Size of the Transformed Image
    # pts2 = np.float32([[0, 0], [500, 0], [0, 400], [500, 400]])
    # for val in pt1:
    #     cv2.circle(paper, (val[0], val[1]), 5, (0, 255, 0), -1)
    # M = cv2.getPerspectiveTransform(pt1, pts2)
    # print (lefttop.x)

def compare_images(image_path, cropped):


# gen_image('C:/Users/sangwooji/Desktop/새 폴더/colorfusion/frame1.png')
image_path = 'C:/Users/sangwooji/Desktop/새 폴더/colorfusion/220724_capturedquality/IMG_20210323_160413.jpg'
data = check_qrcode(image_path)
cropped = crop_image(image_path, data, 0, 3, 1, 2)
compare_images(image_path, cropped)