def area(vertices):
    '''calculates the area of a triangle
    vertices is a dictionary of three ordered pairs
    vertices = {1: (x1,y1), 2: (x2,y2), 3: (x3,y3)}
    each element of vertices is a point specifying the location of the 
    corner of the triangle in the cartesian plane.
    The corners must be listed in the counterclockwise direction.
    '''

    x1,y1 = vertices[1]
    x2,y2 = vertices[2]
    x3,y3 = vertices[3]
    return 1.0/2 * abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)

v = {1: [0,0], 2: [0,2], 3: [-2,0]} # area is 2
x = area(v)
print 'The area of', v, 'is 2. \nOur function gives us %.1f' % (x)

'''
python area_triangle_dict.py
The area of {1: [0, 0], 2: [0, 2], 3: [-2, 0]} is 2. 
Our function gives us 2.0
'''
