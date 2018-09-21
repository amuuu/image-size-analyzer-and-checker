import os

import matplotlib.pyplot as plt

from skimage import data, color, io
from skimage.transform import rescale, resize, downscale_local_mean


def read(args):
    img = args[1]
    process_type = args[2]
    if process_type == "rescale":
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
    image = data.load(img)
    processed_image = None

    if process_type == "rescale":
        image_rescaled = rescale(image, target_x, anti_aliasing=False)
        processed_image = image_rescaled
    elif process_type == "resize":
        # image_resized = resize(image, (image.shape[0] / 4, image.shape[1] / 4),
        #                        anti_aliasing=True)
        image_resized = resize(image, (target_x, target_y),
                               anti_aliasing=True)
        processed_image = image_resized
    elif process_type == "downscale":
        image_downscaled = downscale_local_mean(image, (target_x, target_y))
        processed_image = image_downscaled

    return processed_image


def save(img, directory):
    name = os.path.basename(directory).replace(os.path.basename(directory), "r" + os.path.basename(directory))
    io.imsave(name, img)


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
