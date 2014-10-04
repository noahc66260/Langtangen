def area(vertices):
    '''calculates the area of a triangle
    vertices is a list of three ordered pairs
    vertices = [[x1,y1],[x2,y2],[x3,y3]]
    each element of vertices is a point specifying the location of the 
    corner of the triangle in the cartesian plane.
    The corners must be listed in the counterclockwise direction.
    '''

    x1,y1 = vertices[0]
    x2,y2 = vertices[1]
    x3,y3 = vertices[2]
    return 1.0/2 * abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)

v = [[0,0],[0,2],[-2,0]] # area is 2
x = area(v)
print 'The area of', v, 'is 2. Our function gives us %.1f' % (x)

'''
python area_triangle.py
The area of [[0, 0], [0, 2], [-2, 0]] is 2. Our function gives us 2.0
'''
