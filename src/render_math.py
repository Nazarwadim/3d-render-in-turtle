import math

class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)


    def __rmul__(self, other):
        return self * other
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def dot(self, p_with):
        return self.x * p_with.x + self.y * p_with.y + self.z * p_with.z

class Vector2i:
    def __init__(self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2i(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2i(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2i(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

class Basis:
    def __init__(self, *args):
        if len(args) == 0:
            self.matrix = [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ]
        elif len(args) == 1:
            self.matrix = args[0]
        elif len(args) == 9:
            self.set(*args)
        else:
            raise ValueError("Invalid number of arguments")

    def __str__(self):
        return f"[{self.matrix}]"

    def set(self, ax, bx, cx, ay, by, cy, az, bz, cz):
        self.matrix = [[ax, bx, cx], [ay, by, cy], [az, bz, cz]]
  
    def xform(self, vector : Vector3):
        rows = self.matrix
        return Vector3(
            vector.dot(Vector3(rows[0][0], rows[0][1], rows[0][2])),
            vector.dot(Vector3(rows[1][0], rows[1][1], rows[1][2])),
            vector.dot(Vector3(rows[2][0], rows[2][1], rows[2][2]))
        )

    def tdotx(self, v : list) -> float:
        matrix = self.matrix
        return matrix[0][0] * v[0] + matrix[1][0] * v[1] + matrix[2][0] * v[2]

    def tdoty(self, v : list) -> float:
        matrix = self.matrix
        return matrix[0][1] * v[0] + matrix[1][1] * v[1] + matrix[2][1] * v[2]
    
    def tdotz(self, v : list) -> float:
        matrix = self.matrix
        return matrix[0][2] * v[0] + matrix[1][2] * v[1] + matrix[2][2] * v[2]

    def __mul__(self, other):
        rows = self.matrix
        return Basis(
            other.tdotx(rows[0]), other.tdoty(rows[0]), other.tdotz(rows[0]),
 			other.tdotx(rows[1]), other.tdoty(rows[1]), other.tdotz(rows[1]),
 			other.tdotx(rows[2]), other.tdoty(rows[2]), other.tdotz(rows[2]))
        
    def __rmul__(self, other):
        rows = self.matrix
        self.set(
            other.tdotx(rows[0]), other.tdoty(rows[0]), other.tdotz(rows[0]),
 			other.tdotx(rows[1]), other.tdoty(rows[1]), other.tdotz(rows[1]),
 			other.tdotx(rows[2]), other.tdoty(rows[2]), other.tdotz(rows[2]))

    def rotate_euler(self, euler : Vector3):
        c = math.cos(euler.x)
        s = math.sin(euler.x)
        xmat = Basis(1, 0, 0, 0, c, -s, 0, s, c)

        c = math.cos(euler.y)
        s = math.sin(euler.y)
        ymat = Basis(c, 0, s, 0, 1, 0, -s, 0, c)
        
        c = math.cos(euler.z)
        s = math.sin(euler.z)
        zmat = Basis(c, -s, 0, s, c, 0, 0, 0, 1)
        matrix = xmat * ymat * zmat
        self.matrix = matrix.matrix
        

class Transform:
    def __init__(self, position : Vector3, basis : Basis):
        self.position = position
        self.basis = basis

    def __str__(self):
        return f"Position: {self.position}, Matrix: {self.basis}"
    
    def rotate(self, to : Vector3):
        self.basis.rotate_euler(to)
