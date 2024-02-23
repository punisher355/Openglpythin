from object_resources import ObjectResources

class Scene:
    def __init__(self):
        self.object_resources = ObjectResources()

    def create_scene(self):
        # Define the vertices for the pyramid
        pyramid_vertices = [
            (0.0, 0.25, -2.0),     # Apex
            (-0.25, -0.25, -1.75),  # Base vertex 1
            (0.25, -0.25, -1.75),   # Base vertex 2
            (0.25, -0.25, -2.25),   # Base vertex 3
            (-0.25, -0.25, -2.25)   # Base vertex 4
        ]
        # Define the indices for the pyramid (assuming you want to render it as a single triangle fan)
        pyramid_indices = [0, 1, 2, 3, 4, 1]

        # Create resources for the pyramid
        self.object_resources.create_object_resources('pyramid', pyramid_vertices, pyramid_indices)

    def modify_scene(self):
        # Render the pyramid
        vao = self.object_resources.get_vao('pyramid')
        if vao:
            vao.bind()
            # Render the pyramid (e.g., using glDrawElements)
            vao.unbind()

        # Print the location of the pyramid
        position = (0.0, 1.0, 0.0)
        print(f"Pyramid Location: X={position[0]}, Y={position[1]}, Z={position[2]}")
