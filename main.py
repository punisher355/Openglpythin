import glfw
from OpenGL.GL import *
# from OpenGL.GLU import gluPerspective, gluLookAt
from Scene.Test_Scene import Scene
from shader import ShaderProgram


class OpenGLApplication:
    def __init__(self, window_width, window_height):
        # Initialize window dimensions
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

    def main(self):
        # Initialize GLFW
        if not glfw.init():
            print("Failed to initialize GLFW")
            return

        # Create a window
        window = glfw.create_window(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, "OpenGL Window", None, None)
        if not window:
            glfw.terminate()
            print("Failed to create GLFW window")
            return

        # Set the current context to the created window
        glfw.make_context_current(window)

        # Enable alpha blending for transparency
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Set clear color (black)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        # Enable depth testing
        # glEnable(GL_DEPTH_TEST)

        scene = Scene()
        scene.create_scene()

        # # Set projection matrix (perspective)
        # glMatrixMode(GL_PROJECTION)
        # glLoadIdentity()
        # gluPerspective(45, self.WINDOW_WIDTH / self.WINDOW_HEIGHT, 0.1, 100.0)
        #
        # # Set model view matrix (camera position and orientation)
        # glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        # gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        # Create shader program
        shader = ShaderProgram("shaders/basic_vertex_shader.vert", "shaders/basic_fragment_shader.frag")

        # Use shader program
        shader.use()

        # Main loop for rendering
        while not glfw.window_should_close(window):
            # Clear color and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Render the cube object
            scene.modify_scene()

            # Apply rotation transformation
            glRotatef(1, 1, 1, 1)  # Rotate 1 degree around the axis (1, 1, 1)
            # Disable lighting before rendering GUI
            glDisable(GL_LIGHTING)

            # Swap buffers and poll events
            glfw.swap_buffers(window)
            glfw.poll_events()

            # Error handling
            while glGetError() != GL_NO_ERROR:
                error = glGetError()
                print(f"OpenGL Error: {error}")

        # Cleanup shader program
        del shader

        # Terminate GLFW
        glfw.terminate()


if __name__ == "__main__":
    # Initialize OpenGL application
    app = OpenGLApplication(800, 600)
    # Run the main loop of the application
    app.main()
