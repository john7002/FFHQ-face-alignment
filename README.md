# FFHQ-alignement-generic
Using FFHQ alignement initial method using mediapipe or dlib as landmarks detection method.

### 1. Usage
Launch the following script:
```
python generate_image.py
```

<img src="imgs/align_1.png">

### 2. Script options

* --InFolder: directory to input images to align
* --OutFolder: directory where to place generates align images
* --method: landmark library. So far, supported are 'mediapipe' and 'dlib'
* --no_padding: Do not us padding.
* --rotate_level. Do not rotate face.

<img src="imgs/align_2.png" size= 200px>

* * --size_output. Image output size. Default is 1024







