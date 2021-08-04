# Fast Image Resizer
A simple program to resize images using scikit-image.
## How To Use
1) Install requirements
```
pip install -r requirements.txt
```

2) Open terminal and run this command:
```
python main.py path/to/image.jpg PROCESS_TYPE TARGET_X TARGET_Y
```
PROCESS_TYPE is either "rescale", "resize", or "downscale".

If you wanted to rescale, just enter your desired scale after the process type. Otherwise, enter both the x and y coordinates of your target after process type.

**Note:** Most of the time we use rescale.


## EXAMPLES - ANALYZE MODE:
```
$ python analyze_mode.py
1920x1080 :::: never.jpg
~~~ rescale x from 1920 into 2048

747x717 :::: gonna.png
~~~ rescale x from 747 into 1024

939x939 :::: give.jpg
~~~ rescale x from 939 into 1024

512x512 :::: you.png
~~ ok

####

Would you like the program to rescale images automatically? (y/n)
y
Rescaling never.jpg...
Saved new never.jpg.
Rescaling gonna.png...
Saved new gonna.png.
Rescaling give.jpg...
Saved new give.jpg.
```

## EXAMPLES - MODIFY MODE:

Rescale image by given x:
```
python modify_mode.py img.jpg rescale x=512
```

Rescale image by given scale:
```
python modify_mode.py img.jpg rescale 0.25
```

Resize image by given x and y:
```
python modify_mode.py img.jpg resize 120 145
```

Downscale image by given scales in x and y:
```
python modify_mode.py img.jpg downscale 0.25 0.5
```
