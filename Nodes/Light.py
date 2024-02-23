from Shapes import Shape
from OpenGL.GL import *


class LightEmitterController:
    def __init__(self):
        # Define the vertices for the square
        self.square_vertices = [
            (-0.1, -0.1, 0.0),  # Bottom left
            (-0.1, 0.1, 0.0),   # Top left
            (0.1, 0.1, 0.0),    # Top right
            (0.1, -0.1, 0.0)    # Bottom right
        ]

    def emit_light(self, light_position):
        # Placeholder function for showing location of the light
        self.draw_shape_3d(light_position)

        light_pos = [light_position]  # Positional light at the origin
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        ambient_color = [0.5, 0.5, 0.5, 0.5]  # Ambient light
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_color)
        diffuse_color = [1.0, 1.0, 1.0, 1.0]  # Diffuse light
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_color)

    def draw_shape_3d(self, location):
        # Create a Shape object with square vertices and draw it
        shape = Shape(self.square_vertices)
        shape.draw((1.0, 0.0, 0.0), location[0], location[1], location[2])  # Passing location coordinates


if __name__ == "__main__":
    # Create an instance of the LightEmitterController class
    light_emitter_controller = LightEmitterController()
    # Now, you can run your OpenGL project alongside the keyboard input handling thread
