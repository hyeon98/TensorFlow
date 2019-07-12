from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import threading

class AsyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        print ('Process A')
        threading.Timer(1,self.TaskA).start()

    def TaskB(self):
        print ('Process B')
        threading.Timer(3, self.TaskB).start()

class Object():
    w,h= 500,500 

    def __init__(self):
        pass

    def square():  
        glBegin(GL_QUADS)
        glVertex2f(100, 100)
        glVertex2f(200, 100)
        glVertex2f(200, 200)
        glVertex2f(100, 200)
        glEnd()

    def iterate():  
        glViewport(0, 0, 500, 500)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()

    def showScreen():  
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        Object.iterate()
        glColor3f(1.0, 0.0, 3.0)
        Object.square()
        glutSwapBuffers()


def main():
    print ('Async Function')
    at = AsyncTask()
    at.TaskA()
    at.TaskB()

    temp = Object
    
    glutInit()  
    glutInitDisplayMode(GLUT_RGBA)  
    glutInitWindowSize(500, 500)  
    glutInitWindowPosition(0, 0)  
    glutCreateWindow(b'OpenGL Coding Practice')  
    glutDisplayFunc(Object.showScreen)  
    glutIdleFunc(Object.showScreen)  
    glutMainLoop()  

if __name__ == '__main__':
    main()
