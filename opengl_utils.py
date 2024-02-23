from OpenGL.GL import *


class VAO:
    def __init__(self):
        self.vao_id = glGenVertexArrays(1)
        self.buffers = []

    def add_buffer(self, buffer):
        self.buffers.append(buffer)

    def bind(self):
        glBindVertexArray(self.vao_id)

    def unbind(self):
        glBindVertexArray(0)

    def enable_attributes(self):
        for buffer in self.buffers:
            buffer.enable_attribute()

    def disable_attributes(self):
        for buffer in self.buffers:
            buffer.disable_attribute()


class VBO:
    def __init__(self, data):
        self.vbo_id = glGenBuffers(1)
        self.data = data

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_id)
        glBufferData(GL_ARRAY_BUFFER, self.data, GL_STATIC_DRAW)

    def unbind(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def enable_attribute(self, index=0, size=3, type=GL_FLOAT, normalized=GL_FALSE, stride=0, offset=None):
        glEnableVertexAttribArray(index)
        glVertexAttribPointer(index, size, type, normalized, stride, offset)

    def disable_attribute(self, index=0):
        glDisableVertexAttribArray(index)

class EBO:
    def __init__(self, indices):
        self.ebo_id = glGenBuffers(1)
        self.indices = indices

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices, GL_STATIC_DRAW)

    def unbind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
