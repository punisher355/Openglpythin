#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec3 frag_normal;
out vec2 frag_texcoord;

void main() {
    gl_Position = vec4(position, 1.0);
    frag_normal = normal;
    frag_texcoord = texcoord;
}
