from render_math import Transform
from meshes import CubeMesh

class Object:
    def __init__(self, transform : Transform, mesh : CubeMesh):
        self.transform = transform
        self.mesh = mesh