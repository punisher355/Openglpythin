from opengl_utils import VAO, VBO, EBO
import numpy as np
import logging


class ObjectResources:
    def __init__(self):
        self.vao_dict = {}
        self.vbo_dict = {}

        # Configure logging
        logging.basicConfig(level=logging.INFO)

    def create_object_resources(self, object_name, vertices, indices):
        logging.info(f"Creating resources for object: {object_name}")

        # Convert vertices and indices to NumPy arrays
        vertices_array = np.array(vertices, dtype=np.float32)
        indices_array = np.array(indices, dtype=np.uint32)

        try:
            # Create VBO and EBO using NumPy arrays
            vbo = VBO(vertices_array)
            ebo = EBO(indices_array)

            # Create VAO and bind it
            vao = VAO()
            vao.bind()

            # Bind VBO
            vbo.bind()

            # Bind EBO
            ebo.bind()

            # Unbind VAO (unbind EBO first to avoid issues on some systems)
            ebo.unbind()
            vbo.unbind()
            vao.unbind()

            # Store the VAO and VBO in the dictionaries with the object name
            self.vao_dict[object_name] = vao
            self.vbo_dict[object_name] = vbo

            logging.info(f"Resources created successfully for object: {object_name}")
        except Exception as e:
            logging.error(f"Error creating resources for object {object_name}: {e}")

    def get_vao(self, object_name):
        # Retrieve VAO associated with the object name
        return self.vao_dict.get(object_name)

    def get_vbo(self, object_name):
        # Retrieve VBO associated with the object name
        return self.vbo_dict.get(object_name)

    def delete_object_resources(self, object_name):
        # Delete resources associated with the object name
        if object_name in self.vao_dict:
            del self.vao_dict[object_name]
        if object_name in self.vbo_dict:
            del self.vbo_dict[object_name]
