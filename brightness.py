import cv2
import numpy as np
import sys
import glob

#PASS CV2 Image
def brightness_image(img):
        return np.average(cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))[2]/25.5)

#PASS path of image
def brightness_path(img):
        return np.average(cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))[2]/25.5)

#PASS path of folder
def brightness_folder(path):
    scores=[]
    for f in glob.glob(path+'/*.jpg'):
        img = cv2.imread(f)
        scores.append([f,brightness_path(img)])
    return scores

def main():
    if sys.argv[1]=='path':
       print (brightness_path(cv2.imread(sys.argv[2])))
    elif sys.argv[1]=='folder':
       print (brightness_folder(sys.argv[2]))
      
 
if __name__ == '__main__':
    main()
