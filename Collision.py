import pygame

def checkOverlap(object1, object2) -> bool:
    """Return True if one of the corners of object1 is inside object2, False otherwise.
    Both object1 and object2 must be rectangles.
    """
    x1 = object1.getX()
    y1 = object1.getY()
    w1 = object1.getWidth()
    h1 = object1.getHeight()

    x2 = object2.getX()
    y2 = object2.getY()
    w2 = object2.getWidth()
    h2 = object2.getHeight()

    #area_occupied_1 = [(x1,y1), (x1+w1,y1), (x1,y1+h1), (x1+w1,y1+h1)]

    """For each member of area_occupied_1, checks each column of pixels vertically from the top to see if any of them
    have the same coordinate. If so, returns true.
    
    THIS IS REALLY SLOW LOOKING FOR A FASTER WAY TO DO THIS
    """
    '''for j in area_occupied_1:
        for pixelset in range(x2,x2+w2):
            for pixel in range(y2,y2+h2):
                if j == (pixelset, pixel):
                    return True
    return False
    '''

    '''
    Here is my proposal - Eric
    I set up two rectangles using the coordinates for the objects
    I used pygame's rectangle collision method to test for collision
    '''
    rect1 = pygame.Rect(x1, y1, w1, h1)
    rect2 = pygame.Rect(x2, y2, w2, h2)
    if rect1.colliderect(rect2):
        return True
    return False

