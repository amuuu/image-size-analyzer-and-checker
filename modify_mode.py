import os
import sys
from process import *


img_, process_type, target_x, target_y = read_image(sys.argv)

processed_img = process(img_, process_type=process_type, target_x=target_x, target_y=target_y)

save(processed_img, img_)
