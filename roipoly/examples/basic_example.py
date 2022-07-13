import logging

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
from matplotlib import pyplot as plt

from roipoly import RoiPoly

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)

imgf = cv2.imread('1.jpg')
# Create image
#imgf = np.ones((100, 100)) * range(0, 100)

# Show the image
fig = plt.figure()
plt.imshow(imgf, interpolation='nearest', cmap="Greys")
plt.colorbar()
plt.title("left click: line segment         right click or double click: close region")
plt.show(block=False)

# Let user draw first ROI
roi1 = RoiPoly(color='r', fig=fig)

# Show the image with the first ROI
fig = plt.figure()
plt.imshow(imgf, interpolation='nearest', cmap="Greys")
plt.colorbar()
roi1.display_roi()
plt.title('draw second ROI')
plt.show(block=False)

# Let user draw second ROI
roi2 = RoiPoly(color='b', fig=fig)

# Show the image with both ROIs and their mean values
plt.imshow(imgf, interpolation='nearest', cmap="Greys")
plt.colorbar()
for roi in [roi1, roi2]:
    roi.display_roi()
    roi.display_mean(imgf)
plt.title('The two ROIs')
plt.show()

# Show ROI masks
plt.imshow(roi1.get_mask(imgf) + roi2.get_mask(imgf),
           interpolation='nearest', cmap="Greys")
plt.title('ROI masks of the two ROIs')
plt.show()
