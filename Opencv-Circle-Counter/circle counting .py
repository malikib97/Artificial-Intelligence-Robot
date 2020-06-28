import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("blobs.jpg", 0)

# Load image
image = cv2.imread("blobs.jpg", 0)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image'); plt.show()

# Intialize the detector using the default parameters
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs
keypoints = detector.detect(image)
 
# Draw blobs on our image as red circles
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Total Number of Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
cv2.imwrite('input.jpg', image)

axs[1].imshow(cv2.cvtColor(blobs, cv2.COLOR_BGR2RGB))
axs[1].set_title('Blobs using default parameters')
cv2.imwrite('blobs.jpg', blobs)

plt.show()
# Set our filtering parameters
# Initialize parameter settiing using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True; params.minArea = 100

# Set Circularity filtering parameters
params.filterByCircularity = True ; params.minCircularity = 0.9

# Set Convexity filtering parameters
params.filterByConvexity = False; params.minConvexity = 0.2
    
# Set inertia filtering parameters
params.filterByInertia = True; params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
    
# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
cv2.imwrite('input.jpg', image)

axs[1].imshow(cv2.cvtColor(blobs, cv2.COLOR_BGR2RGB))
axs[1].set_title('Filtering Circular Blobs Only')
cv2.imwrite('circle_blobs.jpg', blobs)

plt.show()