# Image Utility
A simple program to work wit images using scikit-image.

## How to Use?

### 0) Install requirements:
```
$ pip install -r requirements.txt
```


### 1) ANALYZE MODE:
Analyze mode informs you about the size of images and compares them with nearest powers of two. It can be useful for memory optimizations.

#### USE:
You can use the absolute directory address:
```
$ python main.py "C:\Users\RickAstley\Desktop\photos"
```

Optional: You can also put the assets folder inside the same directory as the `main.py` and just use this command:

```
$ python main.py
```
Make sure to specify the name of the assets folder inside the `.env`. file. The default name for images folder is `imgs/`.


### 2) EDIT MODE:

Rescale image by given x:
```
python modify_mode.py img.jpg rescale x=512
```

Rescale image by given ratio:
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
