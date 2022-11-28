from turtle import color
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

rgb_to_opengl = lambda rgb: [value / 255 for value in rgb]

white = (1, 1, 1) #rgb_to_opengl((255, 255, 255))

yellow = rgb_to_opengl((255, 255, 0))

red = rgb_to_opengl((255, 0, 0))

orange = rgb_to_opengl((250, 164, 0))

green = rgb_to_opengl((0, 128, 0))

blue = rgb_to_opengl((0, 0, 255))

mask = rgb_to_opengl((15, 15, 15))

colors = [white, yellow, red, orange, green, blue]

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,0),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = ((1,5,7,2), # top
			(4,0,3,6), # bottom
			(3,2,7,6), # right
			(4,5,1,0), # left
			(6,7,5,4), # front
			(0,1,2,3)  # back
	)

def set_vertices(x_dist, y_dist, z_dist):
    new_vertices = []
    for vertex in vertices:
        x = vertex[0] + x_dist
        y = vertex[1] + y_dist
        z = vertex[2] + z_dist
        new_vertices.append([x, y, z])
    return new_vertices

def Block(vertices):
    glBegin(GL_QUADS)
    for x, surface in enumerate(surfaces):
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Cube(cube_size, gap, block_size):
    norm = lambda n : (n - 1) * (gap + block_size)
    for x in range(cube_size):
        for y in range(cube_size):
            for z in range(cube_size):
                Block(set_vertices(norm(x), norm(y), norm(z)))
                glRotatef(0.01, 3, 1, 1)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -20)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(3, 0.05, 2)
        pygame.display.flip()
        pygame.time.wait(10)


main()