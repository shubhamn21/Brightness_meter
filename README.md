# Brightness_meter

Score images [0-10] to rank brightness of the image.
0- low light images
10- very bright image


## Getting Started

### Prerequisites

Install requirements file

```
pip3 install -r requirements.txt
```

Run script

Using image path

```
python3 ./brightness.py path ./normal.jpg
```

```
python3 ./brightness.py path ./bright.jpg
```

To get scores for all images in folder: 

```
python3 ./brightness.py folder ./
```

![ScreenShot](https://github.com/shubhamn21/Brightness_meter/blob/master/Screenshot.png)


** Note: You can import "brightness_image" in your python project and pass cv2 object to fetch brightness score.

## Authors

* **Shubham Nimbalkar** - (shubhamn21@gmail.com , github.com/shubhamn21)


