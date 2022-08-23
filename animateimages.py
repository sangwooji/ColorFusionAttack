# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation
import videofig

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

image1 = mpimg.imread('C:/Users/sangwooji/Desktop/새 폴더/colorfusion/frame1.png')
image2 = mpimg.imread('C:/Users/sangwooji/Desktop/새 폴더/colorfusion/frame2.png')

# def redraw_fn(f, axes):
#     if f % 2 == 0:
#         img = image1
#     else:
#         img = image2
#
#     if not redraw_fn.initialized:
#         redraw_fn.im = axes.imshow(img, animated=True)
#         redraw_fn.initialized = True
#     else:
#         redraw_fn.im.set_data(img)
# redraw_fn.initialized = False

fig = plt.figure()
im = plt.imshow(image1)
plt.draw()

def init():
    im.set_data(image2)

def animate(i):
    if i % 2 == 0:
        im.set_data(image1)
    if i % 2 == 1:
        im.set_data(image2)
    return im
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fps=60
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=60, interval=1)
    plt.show()
    #videofig.videofig(fps, redraw_fn, play_fps=fps*100)
    # for i in range(fps*1):
    #     if i % 2 == 0:
    #         plt.imshow(image1)
    #         #plt.title('Number 1')
    #     else:
    #         plt.imshow(image2)
    #         #plt.title('Number 2')
    #     plt.pause(1/fps)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
