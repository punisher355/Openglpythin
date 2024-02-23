from OpenGL.GL import *  # OpenGL functions for rendering


class Shape:
    def __init__(self, vertices):
        self.vertices = vertices

    def draw(self, color, x_coord, y_coord, z_coord):
        # Save current transformation matrix
        glPushMatrix()
        # Translate to the specified coordinates
        glTranslatef(x_coord, y_coord, z_coord)
        # Set color for the shape
        glColor3f(*color)
        # Begin drawing a polygon
        glBegin(GL_POLYGON)
        for vertex in self.vertices:
            # Add each vertex of the shape
            glVertex3f(*vertex)
        # End drawing
        glEnd()
        # Restore previous transformation matrix
        glPopMatrix()
