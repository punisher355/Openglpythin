#version 330 core

in vec3 frag_normal;
in vec2 frag_texcoord;

out vec4 frag_color;

void main() {
    frag_color = vec4(frag_normal, 1.0); // Output fragment color based on normal
}
