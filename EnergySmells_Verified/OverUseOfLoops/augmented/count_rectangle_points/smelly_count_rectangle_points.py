def count_rectangle_points(width, height):
    # Counts integer grid points inside a rectangle
    points = 0
    for x in range(width + 1):
        for y in range(height + 1):
            points += 1
    return points
