import sys

from termcolor import colored, cprint

class Cube:
    faces = ['left', 'front', 'right', 'back', 'up', 'down']
    colors = ['orange', 'green', 'red', 'blue', 'white', 'yellow']
    def __init__(self, size):
        self.size = size
        self.left = self.fill_face(self.colors[0])
        self.front = self.fill_face(self.colors[1])
        self.right = self.fill_face(self.colors[2])
        self.back = self.fill_face(self.colors[3])
        self.up = self.fill_face(self.colors[4])
        self.down = self.fill_face(self.colors[5]) # face[row][colomn]

    def get_faces(self):
        faces = list()
        faces.append(self.left)
        faces.append(self.front)
        faces.append(self.right)
        faces.append(self.back)
        faces.append(self.up)
        faces.append(self.down)
        return faces
            
    def fill_face(self, color):
        face = list()
        for i in range(self.size):
            line = list()
            for y in range(self.size):
                line.append(color)
            face.append(line)
        return face

    def print_faces(self):
        faces = self.get_faces()
        names = iter(self.faces)
        for face in faces:
            print(next(names), ": ")
            for row in face:
                for elem in row:
                    if elem == 'orange':
                        print("\033[38;5;202m{}\033[00m" .format(elem), end=' ')
                    else:
                        cprint(elem, elem, end=' ')
                print("\n")

    def move_F(self):
        tmp = self.front[0][0]
        tmp2 = self.front[1][0]
        self.front[0][0] = self.front[2][0]
        self.front[1][0] = self.front[2][1]
        self.front[2][0] = self.front[2][2]
        self.front[2][1] = self.front[1][2]
        self.front[2][2] = self.front[0][2]
        self.front[1][2] = self.front[0][1]
        self.front[0][2] = tmp
        self.front[0][1] = tmp2

        tmp = self.up[2][2]
        self.up[2][2] = self.left[0][2]
        self.left[0][2] = self.down[0][0]
        self.down[0][0] = self.right[2][0]
        self.right[2][0] = tmp
        tmp = self.up[2][1]
        self.up[2][1] = self.left[1][2]
        self.left[1][2] = self.down[0][1]
        self.down[0][1] = self.right[1][0]
        self.right[1][0] = tmp
        tmp = self.up[2][0]
        self.up[2][0] = self.left[2][2]
        self.left[2][2] = self.down[0][2]
        self.down[0][2] = self.right[0][0]
        self.right[0][0] = tmp

    def move_L(self):
        tmp = self.left[0][0]
        tmp2 = self.left[1][0]
        self.left[0][0] = self.left[2][0]
        self.left[1][0] = self.left[2][1]
        self.left[2][0] = self.left[2][2]
        self.left[2][1] = self.left[1][2]
        self.left[2][2] = self.left[0][2]
        self.left[1][2] = self.left[0][1]
        self.left[0][2] = tmp
        self.left[0][1] = tmp2
  
        tmp = self.up[2][0]
        self.up[2][0] = self.back[0][2]
        self.back[0][2] = self.down[2][0]
        self.down[2][0] = self.front[2][0]
        self.front[2][0] = tmp
        tmp = self.up[1][0]
        self.up[1][0] = self.back[1][2]
        self.back[1][2] = self.down[1][0]
        self.down[1][0] = self.front[1][0]
        self.front[1][0] = tmp
        tmp = self.up[0][0]
        self.up[0][0] = self.back[2][2]
        self.back[2][2] = self.down[0][0]
        self.down[0][0] = self.front[0][0]
        self.front[0][0] = tmp

    def move_R(self):
        tmp = self.right[0][0]
        tmp2 = self.right[1][0]
        self.right[0][0] = self.right[2][0]
        self.right[1][0] = self.right[2][1]
        self.right[2][0] = self.right[2][2]
        self.right[2][1] = self.right[1][2]
        self.right[2][2] = self.right[0][2]
        self.right[1][2] = self.right[0][1]
        self.right[0][2] = tmp
        self.right[0][1] = tmp2
  
        tmp = self.up[0][2]
        self.up[0][2] = self.front[0][2]
        self.front[0][2] = self.down[0][2]
        self.down[0][2] = self.back[2][0]
        self.back[2][0] = tmp
        tmp = self.up[1][2]
        self.up[1][2] = self.front[1][2]
        self.front[1][2] = self.down[1][2]
        self.down[1][2] = self.back[1][0]
        self.back[1][0] = tmp
        tmp = self.up[2][2]
        self.up[2][2] = self.front[2][2]
        self.front[2][2] = self.down[2][2]
        self.down[2][2] = self.back[0][0]
        self.back[0][0] = tmp

    def move_B(self):
        tmp = self.back[0][0]
        tmp2 = self.back[1][0]
        self.back[0][0] = self.back[2][0]
        self.back[1][0] = self.back[2][1]
        self.back[2][0] = self.back[2][2]
        self.back[2][1] = self.back[1][2]
        self.back[2][2] = self.back[0][2]
        self.back[1][2] = self.back[0][1]
        self.back[0][2] = tmp
        self.back[0][1] = tmp2
  
        tmp = self.up[0][0]
        self.up[0][0] = self.right[0][2]
        self.right[0][2] = self.down[2][2]
        self.down[2][2] = self.left[2][0]
        self.left[2][0] = tmp
        tmp = self.up[0][1]
        self.up[0][1] = self.right[1][2]
        self.right[1][2] = self.down[2][1]
        self.down[2][1] = self.left[1][0]
        self.left[1][0] = tmp
        tmp = self.up[0][2]
        self.up[0][2] = self.right[2][2]
        self.right[2][2] = self.down[2][0]
        self.down[2][0] = self.left[0][0]
        self.left[0][0] = tmp

    def move_U(self):
        tmp = self.up[0][0]
        tmp2 = self.up[1][0]
        self.up[0][0] = self.up[2][0]
        self.up[1][0] = self.up[2][1]
        self.up[2][0] = self.up[2][2]
        self.up[2][1] = self.up[1][2]
        self.up[2][2] = self.up[0][2]
        self.up[1][2] = self.up[0][1]
        self.up[0][2] = tmp
        self.up[0][1] = tmp2
  
        tmp = self.back[0][0]
        self.back[0][0] = self.left[0][0]
        self.left[0][0] = self.front[0][0]
        self.front[0][0] = self.right[0][0]
        self.right[0][0] = tmp
        tmp = self.back[0][1]
        self.back[0][1] = self.left[0][1]
        self.left[0][1] = self.front[0][1]
        self.front[0][1] = self.right[0][1]
        self.right[0][1] = tmp
        tmp = self.back[0][2]
        self.back[0][2] = self.left[0][2]
        self.left[0][2] = self.front[0][2]
        self.front[0][2] = self.right[0][2]
        self.right[0][2] = tmp

    def move_D(self):
        tmp = self.down[0][0]
        tmp2 = self.down[1][0]
        self.down[0][0] = self.down[2][0]
        self.down[1][0] = self.down[2][1]
        self.down[2][0] = self.down[2][2]
        self.down[2][1] = self.down[1][2]
        self.down[2][2] = self.down[0][2]
        self.down[1][2] = self.down[0][1]
        self.down[0][2] = tmp
        self.down[0][1] = tmp2
  
        tmp = self.front[2][2]
        self.front[2][2] = self.left[2][2]
        self.left[2][2] = self.back[2][2]
        self.back[2][2] = self.right[2][2]
        self.right[2][2] = tmp
        tmp = self.front[2][1]
        self.front[2][1] = self.left[2][1]
        self.left[2][1] = self.back[2][1]
        self.back[2][1] = self.right[2][1]
        self.right[2][1] = tmp
        tmp = self.front[2][0]
        self.front[2][0] = self.left[2][0]
        self.left[2][0] = self.back[2][0]
        self.back[2][0] = self.right[2][0]
        self.right[2][0] = tmp
        
rubik = Cube(3)
rubik.move_F()
rubik.move_L()
rubik.move_R()
rubik.move_B()
rubik.move_U()
rubik.move_D()
rubik.print_faces()