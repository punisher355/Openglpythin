from object_resources import ObjectResources
from OpenGL.GL import glDrawElements, GL_TRIANGLES, GL_UNSIGNED_INT, glColor3f
from OpenGL.GL import glRotatef


class Scene:
    def __init__(self):
        self.object_resources = ObjectResources()

    def create_scene(self):
        # Define the vertices for a cube
        cube_vertices = [
            # Front face
            (-0.5, -0.5, 0.5),   # Bottom left
            (0.5, -0.5, 0.5),    # Bottom right
            (0.5, 0.5, 0.5),     # Top right
            (-0.5, 0.5, 0.5),    # Top left
            # Back face
            (-0.5, -0.5, -0.5),  # Bottom left
            (0.5, -0.5, -0.5),   # Bottom right
            (0.5, 0.5, -0.5),    # Top right
            (-0.5, 0.5, -0.5)    # Top left
        ]

        # Define the indices for the cube
        cube_indices = [
            # Front face
            0, 1, 2, 2, 3, 0,
            # Right face
            1, 5, 6, 6, 2, 1,
            # Back face
            5, 4, 7, 7, 6, 5,
            # Left face
            4, 0, 3, 3, 7, 4,
            # Bottom face
            4, 5, 1, 1, 0, 4,
            # Top face
            3, 2, 6, 6, 7, 3
        ]

        # Create resources for the cube
        self.object_resources.create_object_resources('cube', cube_vertices, cube_indices)

        # Render the cube object
        vao = self.object_resources.get_vao('cube')
        if vao:
            vao.bind()
            # Set color (red)
            glColor3f(1.0, 0.0, 0.0)
            # Draw the cube
            glDrawElements(GL_TRIANGLES, len(cube_indices), GL_UNSIGNED_INT, None)
            vao.unbind()

    def modify_scene(self):
        # Apply rotation transformation
        glRotatef(1, 1, 1, 1)  # Rotate 1 degree around the axis (1, 1, 1)
