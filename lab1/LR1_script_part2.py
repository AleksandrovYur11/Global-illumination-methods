# New scene
scene = Scene()

# TruncatedEllipsoid 1
TruncatedEllipsoidClass = GetClass(Shape, 'TruncatedEllipsoid')
truncateEllipsoid_1 = TruncatedEllipsoidClass()
truncateEllipsoid_1.axes = (2000, 2000, 2000)
truncateEllipsoid_1.hz = 900
truncateEllipsoid_1.rev = True
truncateEllipsoid_1.name = 'FirstEllipsoid'
truncateEllipsoid_1.parts[0].surf_attrs.front_side.kd = 0.98
truncateEllipsoid_1.parts[0].surf_attrs.front_side.kd_color = SpecSurfColor([1.0] * 41, range(380, 790, 10))
truncateEllipsoid_1.parts[0].front_medium = scene.GetMedium('env')
truncateEllipsoid_1.parts[0].back_medium = scene.GetMedium('env')
truncateEllipsoid_1_node = MeshNode(truncateEllipsoid_1)
truncateEllipsoid_1_transform = XYZTransform()
truncateEllipsoid_1_transform.pos = (0, 0, 0)
truncateEllipsoid_1_node.tr = truncateEllipsoid_1_transform

# TruncatedEllipsoid 1
truncateEllipsoid_2 = TruncatedEllipsoidClass()
truncateEllipsoid_2.axes = (2000, 2000, 2000)
truncateEllipsoid_2.hz = -900
truncateEllipsoid_2.rev = False
truncateEllipsoid_2.name = 'SecondEllipsoid'
truncateEllipsoid_2.parts[0].surf_attrs.front_side.kd = 0.3
truncateEllipsoid_2.parts[0].surf_attrs.front_side.kd_color = SpecSurfColor([1.0] * 41, range(380, 790, 10))
truncateEllipsoid_2.parts[0].front_medium = scene.GetMedium('env')
truncateEllipsoid_2.parts[0].back_medium = scene.GetMedium('env')
truncateEllipsoid_2_node = MeshNode(truncateEllipsoid_2)
truncateEllipsoid_2_transform = XYZTransform()
truncateEllipsoid_2_transform.pos = (0, 0, 0)
truncateEllipsoid_2_node.tr = truncateEllipsoid_2_transform

# Light: Cone
light_lib = GetLibrary(Light) 
light_source = light_lib.GetItem("Cone") 
light_source.radiometric = True
light_source.total_flux = 100
light_source.cone_angle = 5
light_source.color = SpecLightColor( [1.0] * 41, range(380, 790, 10))
light_node = LightNode(light_source, name = 'coneLight', )
light_node.medium = scene.GetMedium('env')
light_transform = Transform()
light_transform.pos = (-100, 0, 0)
light_transform.azim = 180
light_transform.rot = 0
light_transform.tilt = 90
light_node.tr = light_transform
light_node.targ_dist = 900

#Color model
cm = ColorModel([it * 10 + 370 for it in range(1, 42)])
cm.SetSpectral()

# Observrer_R_0_0 :
pobs = PlaneObserver()    
pobs.res = 3, 3
pobs.thresh_ang = 90                                            
pobs.org = (997, -25, 25)
pobs.x_side = (0, 50, 0)
pobs.y_side = (0, 0, -50)
pobs.dir = (300, 0, 0)
pobs.phenom = ObserverData.ILLUM
onode = ObserverNode(pobs)
onode.name = "Plane Observer_R_0_0"    
onode.color = (255, 255, 0)

# Observrer_0_R_0 :
pobs1 = PlaneObserver()    
pobs1.res = 3, 3
pobs1.thresh_ang = 90                                            
pobs1.org = (-25, 997, 25)
pobs1.x_side = (50, 0, 0)
pobs1.y_side = (0, 0, -50)
pobs1.dir = (0, 300, 0)
pobs1.phenom = ObserverData.ILLUM
onode1 = ObserverNode(pobs1)
onode1.name = "Plane Observer_0_R_0"    
onode1.color = (255, 255, 0)

# Observrer_0_0_R :
pobs2 = PlaneObserver()    
pobs2.res = 3, 3
pobs2.thresh_ang = 90                                            
pobs2.org = (25, -25, 997)
pobs2.x_side = (-50, 0, 0)
pobs2.y_side = (0, 50, 0)
pobs2.dir = (0, 0, 300)
pobs2.phenom = ObserverData.ILLUM
onode2 = ObserverNode(pobs2)
onode2.name = "Plane Observer_0_0_R"    
onode2.color = (255, 255, 0)


# camera R_0_0
camera_R_0_0 = Camera(6, 1000)
camera_R_0_0_transform = XYZTransform()
camera_R_0_0_transform.pos = (0, 0, 0)
camera_R_0_0_transform.x_rot_ang = -90
camera_R_0_0_transform.y_rot_ang = 0
camera_R_0_0_transform.z_rot_ang = 90
camera_R_0_0.tr = camera_R_0_0_transform
camera_R_0_0.name = "rend_R_0_0"

# camera 0_R_0
camera_0_R_0 = Camera(6, 1000)
camera_0_R_0_transform = XYZTransform()
camera_0_R_0_transform.pos = (0, 0, 0)
camera_0_R_0_transform.x_rot_ang = 90
camera_0_R_0_transform.y_rot_ang = 0
camera_0_R_0_transform.z_rot_ang = 0
camera_0_R_0.tr = camera_0_R_0_transform
camera_0_R_0.name = "rend_0_R_0"

# camera 0_0_R
camera_0_0_R = Camera(6, 1000)
camera_0_0_R_transform = XYZTransform()
camera_0_0_R_transform.pos = (0, 0, 0)
camera_0_0_R_transform.x_rot_ang = 180
camera_0_0_R_transform.y_rot_ang = 0
camera_0_0_R_transform.z_rot_ang = 90
camera_0_0_R.tr = camera_0_0_R_transform
camera_0_0_R.name = "rend_0_0_R"

#Add object Node 
scene.AddNode(light_node)
scene.AddNode(truncateEllipsoid_1_node)
scene.AddNode(truncateEllipsoid_2_node)
scene.AddNode(onode) 
scene.AddNode(onode1)
scene.AddNode(onode2)
scene.Notebook().AddCamera(camera_R_0_0)
scene.Notebook().AddCamera(camera_0_R_0)
scene.Notebook().AddCamera(camera_0_0_R)
scene.color_model = cm

LoadScene(scene) 

#IMAPS
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 180
imaps.SetObserverAsAccSource(onode1)
kernel = GetKernel()
kernel.CalculateIMaps()