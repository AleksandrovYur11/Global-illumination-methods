import random

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
offset = 30

p1 = Vec3(0, 0, 0)
p2 = Vec3(0, 10, 0)
p3 = Vec3(0, 10, 10)

points_triangle = []
points_triangle.append(p1)
points_triangle.append(p2)
points_triangle.append(p3)

for i in points_triangle:
    if(i.x == 0):
        i.x +=offset
    else:
        i.x = i.x * 60 - offset
    if(i.y == 0):
        i.y +=offset
    else:
        i.y = i.y * 60 - offset
    if(i.z == 0):
        i.z +=offset
    else:
        i.z = i.z * 60 - offset

v1_2 = p2 - p1
v1_3 = p3 - p1

array_ray_numbers = []
array_ray_numbers.append(1000)
array_ray_numbers.append(10000)
array_ray_numbers.append(100000)
array_ray_numbers.append(1000000)

for i in range(array_ray_numbers.__len__()):
    colorR = [[0 for _ in range(600)] for _ in range(600)]
    colorG = [[0 for _ in range(600)] for _ in range(600)]
    colorB = [[0 for _ in range(600)] for _ in range(600)]

    count = array_ray_numbers[i]
    while(count > 0):
        random_number_1 = random_double()
        random_number_2 = random_double()

        if random_number_1 + random_number_2 > 1:
            continue

        p = ((v1_2.normalize() * random_number_1) * v1_2.length()) + ((v1_3.normalize() * random_number_2) * v1_3.length()) + p1

        colorR[int(p.y)][int(p.z)] = 100
        count-=1

    output_file_name = "LR2_Aleksandrov_triangle_to_nit_" + str(array_ray_numbers[i]) + ".nit"

    pp = PostProcessor(PPDataUnits.ILLUMINANCE, [], colorR, colorG, colorB)  
    pp.SaveToHDR(output_file_name, overwrite = OverwriteMode.OVERWRITE)


