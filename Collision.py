def check_overlap(object1, object2) -> bool:
    """Return True if one of the corners of object1 is inside object2, False otherwise.
    Both object1 and obje\ct2 must be rectangles.
    """
    x1, y1, w1, h1 = object1.hitbox()
    x2, y2, w2, h2 = object2.hitbox()
    return x1 - w2 <= x2 <= x1 + w1 + w2 and y1 - h2 <= y2 <= y1 + h1 + h2
