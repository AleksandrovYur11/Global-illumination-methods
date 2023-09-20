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
    
    def printVec3(self):
        print(str(self.x) + " " + str(self.y) + " " + str(self.z))

def random_double():
    return random.uniform(0.0, 1.0)

points = []

colorR = [[0 for _ in range(600)] for _ in range(600)]
colorG = [[0 for _ in range(600)] for _ in range(600)]
colorB = [[0 for _ in range(600)] for _ in range(600)]

radius = 5

center_x = 300
center_z = 300
radius = 5 * 55
array_ray_numbers = []
array_ray_numbers.append(1000)
array_ray_numbers.append(10000)
array_ray_numbers.append(100000)
array_ray_numbers.append(1000000)

for i in range(array_ray_numbers.__len__()):
    for k in range(array_ray_numbers[i]):
        random_number_1 = random.uniform(0, 1)
        random_number_2 = random.uniform(0, 1)

        theta = 2 * math.pi * random_number_1
        r = radius * math.sqrt(random_number_2)

        y = center_x + r * math.cos(theta)
        z = center_z + r * math.sin(theta)

        p = Vec3(0, y, z)
        colorR[int(p.z)][int(p.y)] = 100
        
    output_file_name = "LR2_Aleksandrov_circle_to_nit_" + str(array_ray_numbers[i]) + ".nit"

    pp = PostProcessor(PPDataUnits.ILLUMINANCE, [], colorR, colorG, colorB)  
    pp.SaveToHDR(output_file_name, overwrite = OverwriteMode.OVERWRITE)     


