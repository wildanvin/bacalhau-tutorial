import cv2
import numpy as np

image = cv2.imread("../testImages/dron2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

#Select the range of colors in HSV
light_green = (50, 50, 50)
dark_green = (120, 255, 255)

# Segment image using inRange() function
mask = cv2.inRange(hsv_image, light_green, dark_green)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask=mask)

#Calculate a score based on how much "green" is in the image
greenPixels = np.count_nonzero(mask == 255)

# height and width in image
height = image.shape[0]
width = image.shape[1]

score = round((greenPixels*10/(height*width)),1)
print('Green score is:', score)

#Save the result image:
cv2.imwrite('result.jpg',result)
cv2.imwrite('mask.jpg',mask)

print('Saving the result image as result.jpg')

#Save the green score in a file
f = open("score.txt", "w")
f.write(str(score))
f.close()