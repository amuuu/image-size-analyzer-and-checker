import os
import sys
from rescale import *

# def process(img, target_scale_, process_type, target_x=None, target_y=None, scale_x=None, scale_y=None):

img_, process_type, target_x, target_y = read(sys.argv)

print("##########")
print(img_)
print("##########")

processed_img = process(img_, process_type=process_type, target_x=target_x, target_y=target_y)

save(processed_img, img_)
