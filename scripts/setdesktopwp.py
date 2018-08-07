import ctypes
import os
import random
import ctypes

ctypes.windll.user32.MessageBoxW(0, u"It works!", u"It works!", 0)

SPI_SETDESKWALLPAPER = 20 #0x14


# if __name__ == '__main__':
    # # find folder of current script
    # cwd = os.path.dirname(os.path.realpath('jm.jpg')) #__change.jpg__
    # image_folder = os.path.join(cwd, "images")

    # # pick image
    # images = os.listdir(image_folder)
    # image = random.choice(images)
    # image_full = os.path.join(image_folder, image)

    # # set wallpaper
    # ctypes.windll.user32.SystemParametersInfoW(
            # SPI_SETDESKWALLPAPER, 0, image_full, 0)
if __name__ == '__main__':

    # find folder of current script
    cwd = os.path.dirname(os.path.realpath('jm.jpg')) #__change.jpg__
    image_folder = os.path.join(cwd, "wp")

    # pick image
    images = os.listdir(image_folder)
    image = random.choice(images)
    image_full = os.path.join(image_folder, image)

    # set wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, image_full, 0)