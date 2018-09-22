# Fast Image Resizer
A simple program to resize images using scikit-image.
## How To Use
Open terminal and run this command:
```
python main.py path/to/image.jpg PROCESS_TYPE TARGET_X TARGET_Y
```
PROCESS_TYPE is either "rescale", "resize", or "downscale".

If you wanted to rescale, just enter your desired scale after the process type. Otherwise, enter both the x and y coordinates of your target after process type.

**Note:** Most of the time we use rescale.

## EXAMPLES:

Rescale image by given x:
```
python main.py img.jpg rescale x=512
```

Rescale image by given scale:
```
python main.py img.jpg rescale 0.25
```

Resize image by given x and y:
```
python main.py img.jpg 120 145
```

Downscale image by given scales in x and y:
```
python main.py img.jpg 0.25 0.5
```
