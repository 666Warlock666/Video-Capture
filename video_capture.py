# Importing all necessary libraries
import cv2
import os
import shutil
# Read the video from specified path


import sys
import pathlib
filename = sys.argv[1]
filename = pathlib.Path(sys.argv[1])
print(filename)
cam = cv2.VideoCapture(os.path.join(filename))

try:
    if os.path.exists('data'):
        shutil.rmtree('data')
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
    
    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()








