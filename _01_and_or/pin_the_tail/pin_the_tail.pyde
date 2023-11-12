"""
The player of the game has to click the mouse where the donkey's
tail will go. The problem is, the picture keeps disappearing!
"""

def setup():
    size(800, 600)
    
    global donkey
    donkey = loadImage('donkey.jpg')
    donkey.resize(width, height)
    
    global tail
    tail = loadImage('tail.png')
    
    global x
    global y
    x = 700
    y = 125
    
    noStroke()
    
def draw():
    global x
    global y
    
    # 1. Use the background() function to draw the donkey

    # 2. Use the rect() function to draw a box in the upper left
    # corner of the screen:
    rect(0, 0, 30, 30)

    # 3. Now find the x and y coordinates where the tail attaches
    # to the donkey and draw another box with a side of 50
    rect(700, 125, 50, 50)
    # 4. Change your code so the donkey is only shown when the
    # mouse is inside the corner bounding box. 
    if mouseX<30 and mouseY<30:
        background(donkey)
    else:
        background(100)
    # Hint: check if mouseX is greater than 0 and less than 30
    # and y is greater than 0 and less than 30
    
    # 5. Check that when the mouse is outside the corner box,
    # you should show a solid color background.
    
    # 6. Use the image() method to draw the tail at the mouseX
    # and mouseY location. For example,

    
    # 7. Now, adjust your code so the tail sticks when you click the
    # mouse (this means it will no longer move when the mouse moves)
    #
    # Hint: you will need to use the mousePressed variable and set the
    # x and y variables declared in setup()


        if mouseX>700 and mouseX<750 and mouseY>125 and mouseY<175:
            background(donkey)
            image(tail, 700, 125)

    # 8. When the tail has been pinned, write code to check if the
    # tail was pinned inside the target bounding box.
    
    # 9. Show the donkey so the user knows where they pinned the tail.
