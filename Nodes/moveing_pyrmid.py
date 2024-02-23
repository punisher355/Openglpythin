import keyboard
import threading
from Shapes import Shape
# from your_shape_module import Shape  # Assuming you have a module for Shape class


class PyramidController:
    def __init__(self):
        # Define the vertices for the pyramid
        self.pyramid_vertices = [
            (0.0, 0.25, -2.0),     # Apex
            (-0.25, -0.25, -1.75),  # Base vertex 1
            (0.25, -0.25, -1.75),   # Base vertex 2
            (0.25, -0.25, -2.25),   # Base vertex 3
            (-0.25, -0.25, -2.25)   # Base vertex 4
        ]
        # Initialize pyramid position
        self.pyramid_X_location = 1.0
        self.pyramid_Y_location = 0.0

        # Create a lock to prevent race conditions
        self.lock = threading.Lock()

        # Start the keyboard input handling in a separate thread
        self.keyboard_thread = threading.Thread(target=self.update_position)
        self.keyboard_thread.daemon = True  # Daemonize the thread so it terminates with the main program
        self.keyboard_thread.start()

    def get_action_strength(self, key):
        # Check if the key is pressed and return action strength
        is_pressed = keyboard.is_pressed(key)
        # print(f"Key '{key}' pressed: {is_pressed}")
        if is_pressed:
            return 0.0001
        else:
            return 0

    def update_position(self):
        # Continuously update pyramid position based on key presses
        print("Keyboard thread started.")
        while True:
            # Update X and Y positions based on key presses
            with self.lock:
                self.pyramid_X_location += self.get_action_strength('d') - self.get_action_strength('a')
                self.pyramid_Y_location += self.get_action_strength('w') - self.get_action_strength('s')

    def draw_shape_3d(self, color):
        # Create a Shape object with pyramid vertices and draw it
        shape = Shape(self.pyramid_vertices)
        with self.lock:
            shape.draw(color, self.pyramid_X_location, self.pyramid_Y_location, 0.0)


if __name__ == "__main__":
    # Create an instance of the PyramidController class
    pyramid_controller = PyramidController()
    # Now, you can run your OpenGL project alongside the keyboard input handling thread
