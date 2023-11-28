# Image Filter Python Application documentation
## Intro
The following document provides the information about main functions and abilities of the "Image Filter Application", about installing and using it.This Python application applies the following filters to images: morphological filters (erosion, dilation, opening, closing), nonlinear filters based on ordinal statistics (median, maximum, mininum filters).
## Resourses and technologies
### Libraries and modules
•**tkinter** - standard library in Python for creating GUI application.

•**cv2**  - the module in the **OpenCV ** library for image and video processing.

•**numpy** - library for numerical computations, image processing.

•**PIL (Python Imaging Library)** - a library for handling and manipulating images.

### Methods for image processing (OpenCV)
•**cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)** - converts an image from one color space to another. In this case, it converts an image represented in the BGR (Blue-Green-Red) color space to the grayscale color space.

•**cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)** - applies a binary inverse threshold to an image, where pixels with values greater than or equal to the specified threshold are set to white and pixels with values below the threshold are set to black.

•**cv2.erode(image, area, iterations=1)** - performs erosion on an image using a specified structuring element. It operates on a binary image and reduces the boundary or the black regions in the foreground.

•**opening = cv2.dilate(erosion,  self.area, iterations=1)** - performs dilation on an image. Dilation is a morphological operation that expands the boundaries of objects in an image. It is applied on binary images, where white pixels represent objects and black pixels represent background.

•**median = cv2.medianBlur(image, kernel)** - applies a median blur to an image. A median blur replaces each pixel in the image with the median value of the pixels in its neighborhood, formed by kernel size.

_Methods for openind, closing, minimum and maximum filters are based on erode and dilate methods. In addition, there are median, minimum and maximum filters with unique realization._

## Installation

To start using "Image File Picker" you should just download the archive "executable" from this repozitory to your computer, unzip it and run the .exe file. You can check the program with dataset "Test".

## Interface 

After starting the app, you'll be presented with an interface consisting of the following elements:

• Field for image displaying

• Buttons for image opening and filters applying

• Combo-box for choosing the structuring element for morphological fitlers


