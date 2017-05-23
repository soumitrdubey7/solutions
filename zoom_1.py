import numpy as np
import cv2
from math import *
import sys
#interpolation has been done using bilinear interpolation
def interpolation(x,y,img_buff):

  height, width, depth = img_buff.shape[:3] 

  y = y - height/(2*S)
  x = x - width/(2*S)
  img = np.zeros((height+3,width+3,depth),np.uint8)
  img[:height,:width,:]=img_buff

  x_1 = np.zeros((depth),np.uint8)
  x_2 = np.zeros((depth),np.uint8)
  img2 = np.zeros((height,width,depth), np.uint8)
  for i in range (0,height):
    for j in range (0,width):
      for k in range (0,depth):
        x_1[k] = (img[y + i/S,x + j/S,k]*(S - (i % S)) + img[y + i/S +1,x + j/S,k]*(i%S))/S
        x_2[k] = (img[y + i/S,x + j/S + 1,k]*(S - (i % S)) + img[y + i/S +1,x + j/S + 1,k]*(i%S))/S

        img2[i,j,k] = (x_1[k]*(S - (j%S)) + x_2[k]*(j%S))/S
       

  return img2
# for zooming I am dividing the image into 9 parts and then changing the pivot points to get us the best results
def zoom(img,S,x,y,height,width):
  if x < (width/(2*S)) and y < (height/(2*S)):
    #print "1"
    return interpolation(width/(2*S),height/(2*S),img);
  if x < width/(2*S) and y > height/(2*S) and y < height- height/(2*S):
    #print "2"
    return interpolation(width/(2*S),y,img);
  if x < width/(2*S) and y > height- height/(2*S) :
    #print "3"
    return interpolation(width/(2*S), height - height/(2*S),img) 
  if x > width/(2*S) and x < width - (width/(2*S)) and y > height - height/(2*S):
    #print "4"
    return interpolation(x, height - height/(2*S),img)
  if x > width - width/(2*S) and  y > height - height/(2*S):
    #print "5"
    return interpolation(width - width/(2*S),height - height/(2*S),img)
  if x > width - width/(2*S) and y < height - height/(2*S) and y > height/(2*S):
    #print "6"
    return interpolation(width - width/(2*S),y,img)
  if x > width - width/(2*S) and y < height/(2*S):
    #print "7"
    return interpolation(width- width/(2*S),height/(2*S),img)
  if x > width/(2*S) and x < width - width/(2*S) and y < height/(2*S): 
    #print "8"
    return interpolation(x, height/(2*S),img)
  #print "9"
  return interpolation(x,y,img)

if len(sys.argv) < 6:
  print 'Error : Input Arguments should have Scaling_Factor pivot_x pivot_y INPUT_PATH OUTPUT_PATH'
  quit()

IN_PATH = str(sys.argv[4])
#img = cv2.imread('THE1.JPEG')
img = cv2.imread(IN_PATH)
height, width,depth = img.shape[:3] 

#S is scaling factor.

S=int(sys.argv[1])
#pivot_x and pivot_y are points around which you want to zoom
#print sys.argv[1]
pivot_x=int(sys.argv[2])
pivot_y=int(sys.argv[3])
x=pivot_x
y=pivot_y

OUT_PATH = str(sys.argv[5])

img2 = zoom(img,S,x,y,height,width)
#cv2.imwrite('THE2.JPEG',img2) 
cv2.imwrite(OUT_PATH,img2)