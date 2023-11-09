import cv2
import numpy as np

# Load the image
img = cv2.imread("beach-and-boats.jpeg")

# Copy the image to keep the original image
result_image = img.copy()

# Create a window for the result image
cv2.namedWindow("result_image", cv2.WINDOW_NORMAL)

selected_color = None  # To store the color selected by hovering

def mouse_callback(event, x, y, flags, param):
    global selected_color
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the color at the clicked point
        selected_color = result_image[y, x]

# Set up a mouse callback to display the color on a click
cv2.setMouseCallback("result_image", mouse_callback)

while True:
    if selected_color is not None:
        # Create a mask for the selected color
        lower_bound = selected_color - np.array([20, 20, 20])
        upper_bound = selected_color + np.array([20, 20, 20])
        mask = cv2.inRange(result_image, lower_bound, upper_bound)

        # Highlight the selected color areas
        highlighted_image = result_image.copy()
        highlighted_image[np.where(mask == 255)] = [0, 255, 0]  # Highlight in green

        cv2.imshow("result_image", highlighted_image)
    else:
        cv2.imshow("result_image", result_image)

    cv2.imshow("img", img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        break

cv2.destroyAllWindows()