from panda3d.core import *
from panda3d.bullet import *


world = BulletWorld()
world.setGravity(Vec3(0, 0, -10.0))

body = BulletRigidBodyNode('Sphere')
body.setMass(1.0)
body.addShape(BulletSphereShape(0.1))
body.setTransform(TransformState.makePos(VBase3(0,0,1)))
world.attachRigidBody(body)
for i in range(2):
    world.doPhysics(1.0/30.0)
print body.getTransform().getPos()[2]
