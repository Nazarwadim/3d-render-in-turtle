from turtle import *
from render_math import *
from meshes import *
from object import Object

import turtle
import time

basis = Basis([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
transform = Transform(Vector3(100, 100, -200), basis)
cube = Object(transform, SphereMesh(100, 0.25))

turtle.hideturtle()

screen = turtle.Screen()
screen.tracer(0)

def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def main():
    fps = float(144)
    frameDelay = 1000 / fps
    turtle.speed(0)
    turtle.hideturtle()  
    
    screen.title('3D render')
    screen.bgpic('background.png')
    screen.setup(width=0.75, height=0.75)
    screen.bgcolor('#729EFF')
    turtle.color("#FFFFFF")
    frametime = float(frameDelay)
    frameStart = float()
    while True:
        frameStart = time.time()
        turtle.clear()
        update(frametime)
        render(frametime)
        frametime = time.time() - frameStart
        if frameDelay > frametime: 
            time.sleep((frameDelay - frametime) / 1000)
        screen.update() 

x2 = float(10)      
y2 = float(10)
rotation_speed = Vector3(1, 1, 1) # In radians.
start_rotation = Vector3()

def render(delta):
    global cube
    position = cube.transform.position
    vertices = cube.mesh.vertices
    d = 1000
    xform_vertices_2d = []
    for vert in vertices: # IDK How to use turtle and vertex shader.
        xvert = transform.basis.xform(vert)
        
        fx = 55.08 + d * (position.x - 600 + xvert.x) / (xvert.z + position.z + d)
        fy = 18.08 + d * (position.y - 150 + xvert.y) / (xvert.z + position.z + d)
        
        xform_vertices_2d.append(Vector2i(fx, fy))

    for i in range(int(len(xform_vertices_2d) / 3)):
        loc = i * 3 
        draw_line(xform_vertices_2d[loc].x, xform_vertices_2d[loc].y, xform_vertices_2d[loc + 1].x, xform_vertices_2d[loc + 1].y)
        draw_line(xform_vertices_2d[loc + 1].x, xform_vertices_2d[loc + 1].y, xform_vertices_2d[loc + 2].x, xform_vertices_2d[loc + 2].y)
        draw_line(xform_vertices_2d[loc + 2].x, xform_vertices_2d[loc + 2].y, xform_vertices_2d[loc].x, xform_vertices_2d[loc].y)    
    
    
def update(delta):
    global cube
    global rotation_speed
    global start_rotation
    cube.transform.rotate(start_rotation)
    start_rotation += rotation_speed * delta
    
    x, y = screen.getcanvas().winfo_pointerxy()
    y = screen.getcanvas().winfo_height() - y
    cube.transform.position = Vector3(x, y, cube.transform.position.z)

def input(key):
    global cube
    global rotation_speed
    
    if key == "q":
        rotation_speed.x += 0.5
    elif key == "a":
        rotation_speed.x -= 0.5
        
    elif key == "w":
        rotation_speed.y += 0.5
    elif key == "s":
        rotation_speed.y -= 0.5
        
    elif key == "e":
        rotation_speed.z += 0.5
    elif key == "d":
        rotation_speed.z -= 0.5
    
    elif key == "k":
        cube.transform.position.z -= 10
    elif key == "l":
        cube.transform.position.z += 10
    elif key == "c":
        if isinstance(cube.mesh, SphereMesh):
            cube.mesh = CubeMesh(100)
        else:
            cube.mesh = SphereMesh(100, 0.25)


screen.listen()

screen.onkeypress(lambda: input("k"), "k")
screen.onkeypress(lambda: input("l"), "l")
screen.onkeypress(lambda: input("c"), "c")

screen.onkeypress(lambda: input("q"), "q")
screen.onkeypress(lambda: input("a"), "a")

screen.onkeypress(lambda: input("w"), "w")
screen.onkeypress(lambda: input("s"), "s")

screen.onkeypress(lambda: input("e"), "e")
screen.onkeypress(lambda: input("d"), "d")

if __name__ == "__main__":
    main()
