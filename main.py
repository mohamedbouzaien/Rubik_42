from turtle import color
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#from pixel import rgb_color

rgb_to_opengl = lambda rgb: [value / 255 for value in rgb]

white = rgb_to_opengl((255, 255, 255))

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

def Cube():
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

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()