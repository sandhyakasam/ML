# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:29:51 2018

@author: user
"""

import cvlib as cv
import cv2
image = cv2.imread('D:\objdet\dog.jpg')
bbox, label, conf = cv.detect_common_objects(image)
print(label, conf)











#from cvlib.object_detection import draw_bbox
#draw bounding box over detected objects
#out = draw_bbox(image, bbox, label, conf)
#
## display output
## press any key to close window           
#cv2.imshow("object_detection", out)
#cv2.waitKey()
#
## save output
#cv2.imwrite("object_detection.jpg", out)
#
## release resources
#cv2.destroyAllWindows()