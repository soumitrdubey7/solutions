import numpy as np
import cv2
from math import *
import sys

def distorted_image(orig_a_x,orig_a_y, orig_b_x,orig_b_y,orig_c_x,orig_c_y,orig_d_x,orig_d_y,dist_a_x,dist_a_y,dist_b_x,dist_b_y,dist_c_x,dist_c_y,dist_d_x,dist_d_y,height,width,img):
  pointWarp_1 = [(orig_a_x,orig_a_y) ,(orig_b_x,orig_b_y),(orig_c_x,orig_c_y),(orig_d_x,orig_d_y)]
  ptwarp_1 = np.array(pointWarp_1,dtype="float32")
  
  pointWarp_2 = [(dist_a_x,dist_a_y),(dist_b_x,dist_b_y),(dist_c_x,dist_c_y),(dist_d_x,dist_d_y)]
  ptwarp_2 = np.array(pointWarp_2,dtype="float32")
      
  M = cv2.getPerspectiveTransform(ptwarp_1, ptwarp_2)
  warped = cv2.warpPerspective(img, M, (width,height))

  cv2.imwrite('distorted_test2.jpg',warped)

img = cv2.imread('test.jpg')
height, width = img.shape[:2]
#the first 8 points are the coordintes of first image and 
#last 8 points are the points of distoreted image to which you wanna map

if len(sys.argv) < 9:
  print 'Error : Input Arguments should have dist_a_x,dist_a_y,dist_b_x,dist_b_y,dist_c_x,dist_c_y,dist_d_x,dist_d_y'
  quit()

distorted_image(0,0,640,0,0,512,640,512,int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]),height,width,img)
 