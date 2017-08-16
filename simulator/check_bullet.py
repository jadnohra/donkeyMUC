import pybullet as p
p.connect(p.DIRECT)
p.setGravity(0,0,-10)
bodyId = p.createMultiBody(1.0, p.createCollisionShape(p.GEOM_SPHERE,radius=0.1), -1, [0,0,1], [0,0,0,1])
p.stepSimulation()
cubePos, cubeOrn = p.getBasePositionAndOrientation(bodyId)
print(cubePos,cubeOrn)
p.disconnect()

