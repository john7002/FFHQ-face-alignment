# FFHQ-alignement-generic
Using FFHQ alignement initial method using mediapipe or dlib as landmarks detection method.

### 1. Usage
Launch the following script:
```
python generate_image.py
```

<img src="imgs/align1.png" width=400px>

### 2. Script options

* --InFolder: directory to input images to align
* --OutFolder: directory where to place generates align images
* --method: landmark library. So far, supported are 'mediapipe' and 'dlib'
* --no_padding: Do not us padding.

<img src="imgs/align3.png" width=400px>

* --rotate_level. Do not rotate face.

<img src="imgs/align2.png" width=500px>

* * --size_output. Image output size. Default is 1024


Script is able to manage multi faces in a single image.

<img src="imgs/align4.png" width=500px>

### 3. Photo credits




