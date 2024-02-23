from OpenGL.GL import *


class ShaderProgram:
    def __init__(self, vertex_shader_path, fragment_shader_path):
        self.vertex_shader_path = vertex_shader_path
        self.fragment_shader_path = fragment_shader_path
        self.shader_program = self.create_shader_program()

    def read_shader_source(self, path):
        with open(path, 'r') as f:
            return f.read()

    def compile_shader(self, shader_type, source):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader))
        return shader

    def create_shader_program(self):
        # Read shader source files
        vertex_shader_source = self.read_shader_source(self.vertex_shader_path)
        fragment_shader_source = self.read_shader_source(self.fragment_shader_path)

        # Compile vertex and fragment shaders
        vertex_shader = self.compile_shader(GL_VERTEX_SHADER, vertex_shader_source)
        fragment_shader = self.compile_shader(GL_FRAGMENT_SHADER, fragment_shader_source)

        # Create shader program
        shader_program = glCreateProgram()
        glAttachShader(shader_program, vertex_shader)
        glAttachShader(shader_program, fragment_shader)
        glLinkProgram(shader_program)
        if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(shader_program))

        # Clean up shaders
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        return shader_program

    def use(self):
        glUseProgram(self.shader_program)

    def __del__(self):
        glDeleteProgram(self.shader_program)
