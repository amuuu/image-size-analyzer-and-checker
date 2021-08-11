import os

import matplotlib.pyplot as plt
import math
from skimage import data, color, io 
from skimage.transform import rescale, resize, downscale_local_mean
from PIL import Image

def read_image(args):
    img = args[1]
    process_type = args[2]
    
    if process_type == "rescale":
        if "x=" or "x =" in args[3]:
            target_scale_x = args[3]
            target_scale_y = ""
        elif "y=" or "y =" in args[3]:
            target_scale_x = ""
            target_scale_y = args[3]
        else:
            target_scale_x = float(args[3])
            target_scale_y = float(args[3])
        return img, process_type, target_scale_x, target_scale_y
    elif process_type == "resize":
        target_x = float(args[3])
        target_y = float(args[4])
        return img, process_type, target_x, target_y
    elif process_type == "downscale":
        scale_x = float(args[3])
        scale_y = float(args[4])
        return img, process_type, scale_x, scale_y

    return img, process_type, "error", "error"


def process(img, process_type, target_x=None, target_y=None):
    image = io.imread(img, False)
    processed_image = None

    if process_type == "rescale":
        if "x=" in target_x:
            target_scale = float(target_x.replace("x=", "").replace(" ","")) / image.shape[0]
        elif "y=" in target_y:
            target_scale = float(target_y.replace("y=", "").replace(" ","")) / image.shape[1]
        else:
            target_scale = target_x
        processed_image = rescale_img(image, target_scale)

    elif process_type == "resize":
        processed_image = resize_img(image,target_x, target_y)
    
    elif process_type == "downscale":
        processed_image = downscale_img(image, target_x, target_y)
    
    show_plot(processed_image)
    return processed_image

def get_size(img):
    img_ = io.imread(img)   
    return img_.shape

def save(img, directory):
    # name = os.path.basename(directory).replace(os.path.basename(directory), "r" + os.path.basename(directory))
    name = directory
    # io.imsave(name, img)
    Image.fromarray(img, mode='RGB').save(name)

def resize_img(img, target_x, target_y):
    return resize(img, (target_x, target_y), anti_aliasing=True)
            
def rescale_img(img, new_scale):
    return rescale(img, new_scale, anti_aliasing=False)

def downscale_img(img, scale_x, scale_y):
    return downscale_local_mean(img, (scale_x, scale_y))

def check_size(size):
    y = size[0]
    x = size[1]
    x_log = math.log(x, 2)
    y_log = math.log(y, 2)

    x_ok, y_ok = False, False
    if x_log.is_integer():
        x_ok = True
    if y_log.is_integer():
        y_ok = True
    
    if x_ok and y_ok:
        return "~~ ok", None
    elif x_ok and not y_ok:
        return " ~~ x power of 2", None
    elif y_ok and not x_ok:
        return "~~ y power of 2", None
    
    else:
        if x_log - int(x_log) > 0.5:
            closest_ok_x = int(math.pow(2, math.ceil(x_log)))
        else:
            closest_ok_x = int(math.pow(2, math.floor(x_log)))

        if y_log - int(y_log) > 0.5:
            closest_ok_y = int(math.pow(2, math.ceil(y_log)))
        else:
            closest_ok_y = int(math.pow(2, math.floor(y_log)))

        if closest_ok_y > closest_ok_x:
            return "~~~ rescale y from " + str(y) + " into " + str(closest_ok_y), (0, closest_ok_y)
        else:
            return "~~~ rescale x from " + str(x) + " into " + str(closest_ok_x), (1, closest_ok_x)
            
def show_plot(img_dictionary):
    fig, axes = plt.subplots(nrows=1, ncols=2)

    ax = axes.ravel()

    ax[0].imshow(img_dictionary[0], cmap='gray')
    ax[0].set_title("Original image")

    ax[1].imshow(img_dictionary[1], cmap='gray')
    ax[1].set_title("Rescaled image (aliasing)")

    ax[2].imshow(img_dictionary[2], cmap='gray')
    ax[2].set_title("Resized image (no aliasing)")
    #
    ax[3].imshow(img_dictionary[3], cmap='gray')
    ax[3].set_title("Downscaled image (no aliasing)")
    #
    ax[0].set_xlim(0, 512)
    ax[0].set_ylim(512, 0)
    plt.tight_layout()
    plt.show()
