# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
src = cv2.imread("img1.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)
scale_percentage = 50

new_width = int(src.shape[1] * scale_percentage * scale_percentage/100)
new_height = int(src.shape[0] * scale_percentage * scale_percentage/100)

output = cv2.resize(src, (new_width, new_height))


cv2.imwrite("NewImg.png", output)
cv2.waitKey(0)

