from render_math import *

class CubeMesh:
    def __init__(self, size):
        self.size = size
        half_size = size / 2
        self.vertices = [Vector3(half_size, half_size, half_size),
                  Vector3(half_size, half_size, -half_size),
                  Vector3(half_size, -half_size, -half_size),
                  
                  Vector3(half_size, -half_size, -half_size),
                  Vector3(half_size, -half_size, half_size), 
                  Vector3(half_size, half_size, half_size),
                  
                  Vector3(-half_size, half_size, -half_size),
                  Vector3(-half_size, half_size, half_size),
                  Vector3(-half_size, -half_size, -half_size),
                  
                  Vector3(-half_size, half_size, half_size),
                  Vector3(-half_size, -half_size, -half_size),
                  Vector3(-half_size, -half_size, half_size), 
                  
                  Vector3(half_size, half_size, half_size),
                  Vector3(-half_size, half_size, half_size),
                  Vector3(-half_size, -half_size, half_size),
                  
                  Vector3(-half_size, -half_size, half_size),
                  Vector3(half_size, -half_size, half_size),
                  Vector3(half_size, half_size, half_size),
                  
                  Vector3(half_size, half_size, -half_size),
                  Vector3(-half_size, half_size, -half_size),
                  Vector3(-half_size, -half_size, -half_size),
                  
                  Vector3(-half_size, -half_size, -half_size),
                  Vector3(half_size, -half_size, -half_size),
                  Vector3(half_size, half_size, -half_size),
                  
                  Vector3(half_size, half_size, half_size),
                  Vector3(half_size, half_size, -half_size),
                  Vector3(-half_size, half_size, -half_size),
                  
                  Vector3(-half_size, half_size, -half_size),
                  Vector3(-half_size, half_size, half_size),
                  Vector3(half_size, half_size, half_size),
                  
                  Vector3(half_size, -half_size, half_size),
                  Vector3(half_size, -half_size, -half_size),
                  Vector3(-half_size, -half_size, -half_size),
                  
                  Vector3(-half_size, -half_size, -half_size),
                  Vector3(-half_size, -half_size, half_size),
                  Vector3(half_size, -half_size, half_size),
                  ]
        
        
class SphereMesh:
    def __init__(self, radius : float, accuracy : float):
        self.radius = radius
        self.accuracy = accuracy
        self.vertices = self._generate_mesh()
        
    def _generate_mesh(self):
        vertices = []
        radius = self.radius
        
        # x=r⋅sin(ϕ)⋅cos(θ)
        # y=r⋅sin⁡(ϕ)⋅sin⁡(θ)
        # z=r⋅cos⁡(ϕ)
        for i in range(0, 628, int(1 + 10 / self.accuracy)):
            f_i = i / 100
            cos_i = math.cos(f_i)
            sin_i = math.sin(f_i)
            for j in range(0, 628, int(1 + 10 / self.accuracy)):
                f_j = j / 100
                cos_j = math.cos(f_j)
                sin_j = math.sin(f_j)
                
                vert = Vector3(radius * sin_j * cos_i, radius * cos_j * cos_i, radius * sin_i)
                vertices.append(vert)
            
        # fill the array of vertices perpendicular to other triangles.
        for i in range(0, 628, int(1 + 10 / self.accuracy)):
            f_i = i / 100
            cos_i = math.cos(f_i)
            sin_i = math.sin(f_i)
            for j in range(0, 628, int(1 + 10 / self.accuracy)):
                f_j = j / 100
                cos_j = math.cos(f_j)
                sin_j = math.sin(f_j)
                
                vert = Vector3(radius * sin_i * cos_j, radius * cos_i * cos_j, radius * sin_j)
                vertices.append(vert)
        
        length_remainder = len(vertices) % 3        
        if length_remainder == 1:
            vertices.pop(len(vertices) - 1)
        elif length_remainder == 2:
            vertices.pop(len(vertices) - 1)
            vertices.pop(len(vertices) - 1)
    
        
        vertices.append(vertices[-1])
        vertices.append(vertices[0])
        vertices.append(vertices[-1])

        return vertices