import random
import math

class Vec3:
    def __init__(self, new_x=0, new_y=0, new_z=0):
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def __add__(self, vector):
        return Vec3(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vec3(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, d):
        return Vec3(self.x * d, self.y * d, self.z * d)

    def __truediv__(self, d):
        return Vec3(self.x / d, self.y / d, self.z / d)

    def normalize(self):
        length = self.length()
        return Vec3(self.x / length, self.y / length, self.z / length)

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

def random_double():
    return random.uniform(0.0, 1.0)

name = input("Name: ")
color_model = input("ColorModel: ")
normal_flux = input("NormalFlux: ")
scale = int(input("Scale: "))
ray_number = int(input("RayNumber: "))

ray_flux = input("RayFlux: ")

points = []
radius = 5
pi = math.pi

for i in range(ray_number):
    random_number_1 = random.random()
    h = -radius + 2 * radius * random_number_1

    random_number_2 = random.random()
    fi = 2 * pi * random_number_2

    theta = math.acos(h / radius)
    z = radius * math.sin(theta) * math.sin(fi)
    x = radius * math.sin(theta) * math.cos(fi)
    y = radius * math.cos(theta) 

    new_vector = (Vec3(x, y, z) + Vec3(0, radius, 0)).normalize()
    points.append(new_vector)

file = name + ".ray"
with open(file, 'w') as fout:
    fout.write("Rayset\n")
    fout.write("  Name " + name + "\n")
    fout.write("  ColorModel " + color_model + "\n")
    fout.write("  NormalFlux " + normal_flux + "\n")
    fout.write("  Scale " + str(scale) + "\n")
    fout.write("  RayNumber " + str(ray_number) + "\n")
    fout.write("  RayFlux " + ray_flux + "\n")
    fout.write("  Rays\n\n")

    for i in range(ray_number):
        
        fout.write("   " + str(points[i].x) + "   " + str(points[i].y) + "   " + str(points[i].z))
        fout.write("   " + str(points[i].x) + "   " + str(points[i].y) + "   " + str(points[i].z))
        fout.write("   1   1   1\n")

print("File saved successfully.")

