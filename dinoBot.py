from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
import sys

class Coordinates():
    # Coordinates of replay button to start the game
    replayButton = (755, 280)
    # Top left coordinates of the dino
    dino = (515, 283)

# Clicks the restart game button
def restartGame():

    pyautogui.click(Coordinates.replayButton)

    # Keeping the the dino down
    pyautogui.keyDown('down')

# Press space bar
def pressSpace():

    # Release the down key
    pyautogui.keyUp('down')

    # Press the space key
    pyautogui.keyDown('space')

    # Slight pause
    time.sleep(0.15)

    # Release the space button
    pyautogui.keyUp('space')

    # Press the down key again, to keep the dino always down
    pyautogui.keyDown('down') 
  
# Grabbing the image to check
def imageGrab():

    # Defining the coords of box infront of the dino
    box = (Coordinates.dino[0], Coordinates.dino[1],
            Coordinates.dino[0]+100, Coordinates.dino[1]+30)
    
    # Grabbing all pixel values in form of RGB tuples
    image = ImageGrab.grab(bbox=box)
 
     # Making the image grayscale to process faster
    grayImage = ImageOps.grayscale(image)
 
    # using numpy to get sum of al grayscale pixels
    a = np.array(grayImage.getcolors())
    
    print(a.sum())
    return a.sum()
 
def main():
    time.sleep(5)
    restartGame()
    while True:
        # Checks if it is a blank space or not
        if (imageGrab() != 3033):
            pressSpace()
        # imageGrab()
        # break

if __name__ == "__main__":
    main()
    