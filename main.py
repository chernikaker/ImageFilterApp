import copy
import tkinter as tk
from tkinter import *

from tkinter import filedialog
from tkinter import ttk

import cv2
import numpy as np

from PIL import Image, ImageTk


class ImageProcessor:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.title("Image processor")

        self.default_image = np.zeros((300, 300, 3), dtype=np.uint8)
        self.default_image[:] = (255, 255, 255)

        self.image = None
        self.processed_image = None
        self.panel = tk.Label(self.root)
        self.panel.pack(side="right", padx=10, pady=7)
        self.area_mode = "5x5 Rectangle"
        self.area = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        self._setup_buttons()

    def _setup_buttons(self) -> None:

        self.open_btn = tk.Button(
            self.root, text="Open Image", command=self.open_image
        )
        self.open_btn.pack(pady=3)

        self.original_btn = tk.Button(
            self.root, text="Show Original", command=self.show_original_image
        )
        self.original_btn.pack(pady=3)

        self.grey_btn = tk.Button(
            self.root, text="Show Gray", command=self.show_grey,
        )
        self.grey_btn.pack(pady=3)

        self.blackwhite_btn = tk.Button(
            self.root, text="Show Binary", command=self.show_blackwhite,
        )
        self.blackwhite_btn.pack(pady=3)


        self.mode = tk.Label(self.root, width=20, height=3,
                             text="Your structuring\n element shape is\n " + self.area_mode, background='#fff')
        self.mode.pack(pady=0)

        self.mode_picker = ttk.Combobox(self.root, values=["5x5 Rectangle", "3x3 Rectangle", "1x2 Rectangle",
                                                           "2x1 Rectangle", "3x3 Cross", "5x5 Cross", "5x5 Ellipse"])
        self.mode_picker.current(0)
        self.mode_picker.bind("<<ComboboxSelected>>", self.mode_select)
        self.mode_picker.pack(pady=0)


        self.line = tk.Label(self.root,width=20, height=3, text="MORPHOLOGICAL\n PROCESSING")
        self.line.pack(pady=0)


        self.erosion_btn = tk.Button(
            self.root, text="Show Erosion", command=self.show_erosion
        )
        self.erosion_btn.pack(pady=3)

        self.dilation_btn = tk.Button(
            self.root, text="Show Dilation", command=self.show_dilation
        )
        self.dilation_btn.pack(pady=3)

        self.opening_btn = tk.Button(
            self.root, text="Show Opening", command=self.show_opening
        )
        self.opening_btn.pack(pady=3)

        self.closing_btn = tk.Button(
            self.root, text="Show Closing", command=self.show_closing
        )
        self.closing_btn.pack(pady=3)

        self.line1 = tk.Label(self.root, width=20, height=3, text="NONLINEAR\n FILTERS")
        self.line1.pack(pady=0)

        self.median_btn = tk.Button(
            self.root, text="Show Median Filter", command=self.show_median
        )
        self.median_btn.pack(pady=3)

        self.minimum_btn = tk.Button(
            self.root, text="Show Minimum Filter", command=self.show_minimum
        )
        self.minimum_btn.pack(pady=3)

        self.maximum_btn = tk.Button(
            self.root, text="Show Maximum Filter", command=self.show_maximum
        )
        self.maximum_btn.pack(pady=3)

        self.my_median_btn = tk.Button(
            self.root, text="Show Median Filter (own realization)", command=self.show_my_median
        )
        self.my_median_btn.pack(pady=3)

        self.my_minimum_btn = tk.Button(
            self.root, text="Show Minimum Filter (own realization)", command=self.show_my_minimum
        )
        self.my_minimum_btn.pack(pady=3)

        self.my_maximum_btn = tk.Button(
            self.root, text="Show Maximum Filter (own realization)", command=self.show_my_maximum
        )
        self.my_maximum_btn.pack(pady=3)

    def mode_select(self, event):
        selected_item = self.mode_picker.get()
        self.area_mode = selected_item
        self.mode['text'] = "Your structuring\n element shape is\n " + self.area_mode
        if self.area_mode == "5x5 Rectangle":
            self.area = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        elif self.area_mode == "3x3 Rectangle":
            self.area = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        elif self.area_mode == "1x2 Rectangle":
            self.area = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
        elif self.area_mode == "2x1 Rectangle":
            self.area = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
        elif self.area_mode == "3x3 Cross":
            self.area = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        elif self.area_mode == "5x5 Cross":
            self.area = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        elif self.area_mode == "5x5 Ellipse":
            self.area = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))


    def resize_image(self, image, width=None, height=None):
        h, w = image.shape[:2]

        if width is None and height is None:
            return image

        if width is None:
            aspect_ratio = height / h
            new_width = int(w * aspect_ratio)
            new_size = (new_width, height)
        else:
            aspect_ratio = width / w
            new_height = int(h * aspect_ratio)
            new_size = (width, new_height)

        resized_img = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
        return resized_img

    def open_image(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.image = cv2.imread(file_path)
            self.processed_image = np.copy(self.image)
            self.display_image(self.processed_image)
        else:
            self.image = None
            self.processed_image = None
            self.display_image(self.default_image)

    def show_original_image(self):
        if self.image is None:
            return
        self.processed_image = np.copy(self.image)
        self.display_image(self.processed_image)

    def get_grey(self):
        if self.image is None:
            return
        gray_im = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        enhanced_im = np.array(gray_im, np.uint8)

        return enhanced_im

    def show_grey(self):
        self.display_image(self.get_grey())
    def get_binary(self):
        if self.image is None:
            return
        thresh, bw_im = cv2.threshold(self.get_grey(), 128, 255, cv2.THRESH_BINARY_INV)

        return bw_im

    def show_blackwhite(self):
        self.display_image(self.get_binary())

    def show_erosion(self):
        if self.image is None:
            return
        erosion = cv2.erode(self.get_binary(), self.area, iterations=1)
        print("with "+self.area_mode)
        self.display_image(erosion)

    def show_dilation(self):
        if self.image is None:
            return

        dilation = cv2.dilate(self.get_binary(),  self.area, iterations=1)
        self.display_image(dilation)

    def show_opening(self):
        if self.image is None:
            return
        erosion = cv2.erode(self.get_binary(),  self.area, iterations=1)
        opening = cv2.dilate(erosion,  self.area, iterations=1)
        self.display_image(opening)

    def show_closing(self):
        if self.image is None:
            return

        dilation = cv2.dilate(self.get_binary(),  self.area, iterations=1)
        erosion = cv2.erode(dilation,  self.area, iterations=1)
        self.display_image(dilation)

    def median_filter(self, arrimg, inpk):

        k = inpk//2
        img = Image.fromarray(arrimg)
        newimg = copy.copy(img)
        members = [0]*inpk*inpk
        for i in range(k, img.width - k):
            for j in range(k, img.height - k):
                count = 0
                for i1 in range (-k, k):
                    for j1 in range (-k,k):
                        members[count] = img.getpixel((i +i1, j + j1))
                        count+=1
                members.sort()
                newimg.putpixel((i, j), (members[count//2]))
        return np.array(newimg)

    def max_filter(self, arrimg, inpk):
        k = inpk // 2
        img = Image.fromarray(arrimg)
        newimg = Image.new("RGB", (img.width, img.height), "white")
        for i in range(k, img.width - k):
            for j in range(k, img.height - k):
                count = 0
                maxpix = 0
                for i1 in range(-k, k):
                    for j1 in range(-k, k):
                        if maxpix < img.getpixel((i + i1, j + j1)): maxpix = img.getpixel((i + i1, j + j1))
                        count += 1
                newimg.putpixel((i, j), (maxpix, maxpix, maxpix))
        return np.array(newimg)

    def min_filter(self, arrimg, inpk):
        k = inpk // 2
        img = Image.fromarray(arrimg)
        newimg = Image.new("RGB", (img.width, img.height), "white")
        for i in range(k, img.width - k):
            for j in range(k, img.height - k):
                count = 0
                minpix = 255
                for i1 in range(-k, k):
                    for j1 in range(-k, k):
                        if minpix > img.getpixel((i + i1, j + j1)): minpix = img.getpixel((i + i1, j + j1))
                        count += 1
                newimg.putpixel((i, j), (minpix, minpix, minpix))
        return np.array(newimg)
    def display_image(self, img):
        img = self.resize_image(img, width=650, height=650)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        self.panel.config(image=img)
        self.panel.image = img

    def run(self) -> None:
        self.display_image(self.default_image)
        self.root.mainloop()

    def show_median(self):
        if self.image is None:
            return
        median = cv2.medianBlur(self.get_grey(),7)

        self.display_image(median)

    def show_my_median(self):
        if self.image is None:
            return
        median=self.median_filter(self.get_grey(),5)
        self.display_image(median)

    def show_minimum(self):
        if self.image is None:
            return
        min = cv2.erode(self.get_grey(), cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
        self.display_image(min)

    def show_my_minimum(self):
        if self.image is None:
            return
        min = self.min_filter(self.get_grey(), 5)
        self.display_image(min)

    def show_maximum(self):
        if self.image is None:
            return
        max = cv2.dilate(self.get_grey(), cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)
        self.display_image(max)

    def show_my_maximum(self):
        if self.image is None:
            return
        max = self.max_filter(self.get_grey(), 5)
        self.display_image(max)

def main() -> None:
    processor = ImageProcessor()
    processor.run()


if __name__ == "__main__":
    main()