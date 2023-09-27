import random
import time
import re
from math import pi, cos, sin, acos

n_rays = [1000000]
#n_rays = [100000,]

R = 1

def parse_table(table_content: str) -> dict:
    """ method for parsing table file """

    result = {}
    table_list = table_content.split("\n")

    for idx,ln in enumerate(table_list):
        if 'def' not in ln:
            i, v = ln.split(' ')
            i = i.replace("\t", "")
            v = v.replace("\t", "")
            # converting values to float, int or string
            try:
                result[i] = float(v)
            except ValueError:
                try:
                    result[i] = int(v)
                except ValueError:
                    result[i] = v
        else:
            # parsing defined thetas
            result['def'] = parse_def(table_list, idx, result.get('theta', 31))
            break
    return result



def parse_def(table_information: list, idx: int, theta: int) -> list:
    """ method for parsing thetas from table """
    result = []
    # delta angle counting
    step = 180/(theta-1)

    for i in range(idx+1, len(table_information)-1):
        for phi in table_information[i].split():
            result.append((len(result)*step, float(phi)))

    return result


def search_b(v: list, n: float) -> tuple:
    """ Binary search """
    l = 0
    # counting not null elements
    r = len(list(filter(None, v)))+2
    while (l+1) < r:
        m = int((l+r)/2)
        if v[m] < n:
            l = m
        else:
            r = m
    return r,l

def table_to_rayset(n, table_filename):
    # converting table distribution to Rayset
    result = []
    table_str = ''

    with open(table_filename, 'r') as f:
        table_str = f.read()

    # global table configuration
    table_settings = parse_table(table_str)

    thetas = []
    for idx,theta in enumerate(table_settings['def']):
        thetas.append((((idx * 6) * pi) / 180))

    thetas2 = []
    for idx,theta in enumerate(table_settings['def']):
        thetas2.append(sin(thetas[idx]) * theta[1])

    integral = []
    tmp = 0

    for idx,theta in enumerate(thetas2):
    
        tmp = ((thetas[idx] - thetas[idx - 1]) * (thetas2[idx] + thetas2[idx - 1]) / 2) + integral[idx - 1] if integral[idx - 1:] else 0 
        integral.append(tmp)

    max_val = max(integral)
    for idx,theta in enumerate(integral):
        integral[idx] = theta / max_val

    for i in range(n):
        rnd_intensity = random.uniform(0,1)

        r, l = search_b(integral, rnd_intensity)

        interpol = 0
        rnd_local_intensity = table_settings.get('NormalFlux', 1)

        # interolation to redce lines on graph
        while rnd_local_intensity > interpol:
            rnd_theta = random.uniform(thetas[l], thetas[r])
            interpol = thetas2[l] + (thetas2[r] - thetas2[l])/(thetas[r]-thetas[l]) * (rnd_theta - thetas[l])
            rnd_local_intensity = random.uniform(0, max(thetas2[l], thetas2[r]))
            # print(interpol, rnd_local_intensity)

        
        fi = random.uniform(0,1)
        fi = 2 * pi * fi

        x = R * sin(rnd_theta) * cos(fi)
        y = cos(rnd_theta) * R
        z = R * sin(rnd_theta) * sin(fi)
        result.append((x,y,z))
    return result

def write_rayset(rays, filename):
    """ Method for saving Rayset file on disk """
    file = open(filename, "w")
    ray_number = len(rays)
    header = """Rayset
  Name triangle        ;; name of Rayset
  ColorModel RGB       ;; color model
  NormalFlux 3142       ;; luminous flux of all rays
  Scale 0.0010000     ;; specified if millimeters are scene units
  RayNumber  {ray_number}         ;; number of specified rays
  RayFlux    Relative  ;; relative (flux of Rayset = NormalFlux)
                       ;; or absolute (flux if Rayset = sum flux of all rays)
  Rays                 ;; keyword to start ray definition

;;                                                      efficiency
;;	x	y	z	xdir	ydir	zdir	R G B \n""".format(ray_number=ray_number)
    file.write(header)
    for ray in rays:
        ray_string = "	{ray[0]}	{ray[1]}	{ray[2]}	{ray[0]}	{ray[1]}	{ray[2]}	1 1 1\n".format(ray=ray)
        file.write(ray_string)
    file.flush()
    file.close()

scene = Scene()
# Observer  eduals to previous labs
po = GonioObserver()
po.res = (640, 320)
po.phenom = ObserverData.ILLUM
onode = ObserverNode(po)
onode.name = "GonioObserver 640"

# Observer for graph vizualization
po2 = GonioObserver()
po2.res = (1, 320)
po2.phenom = ObserverData.ILLUM
onode2 = ObserverNode(po2)
onode2.name = "GonioObserver 1"

# counting for different numbers of rays and creating light source for each of
# them
for nr in n_rays:
    rayset_filename = "rayset_table_{nr}.ray".format(nr=nr)
    my_rayset = table_to_rayset(nr, './table.dgr')
    write_rayset(my_rayset, rayset_filename)
    rayset = RaySet(rayset_filename)
    light = Light("Rayset light{nr}".format(nr=nr), rayset)
    transform = Transform()
    light_node = LightNode(light, name = 'Rayset light {nr}'.format(nr=nr))
    light_node.total_flux = pi * 1000
    light_node.tr = transform
    scene.AddNode(light_node)

scene.AddNode(onode)
scene.AddNode(onode2)

# saving lumicept scene
LoadScene(scene)
scene.Save("LR_4_Aleksandrov", overwrite=0)