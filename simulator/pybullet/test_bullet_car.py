import pybullet as p
import time

cid = p.connect(p.SHARED_MEMORY)
if (cid<0):
	p.connect(p.GUI)
	
p.resetSimulation()
p.setGravity(0,0,-10)

useRealTimeSim = 1

#for video recording (works best on Mac and Linux, not well on Windows)
#p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, "racecar.mp4")
p.setRealTimeSimulation(useRealTimeSim) # either this
p.loadURDF("data/plane.urdf")
#p.loadSDF("stadium.sdf")

car = p.loadURDF("data/bullet_racecar/racecar.urdf")
#car = p.loadURDF("data/jazebo_car.urdf")
for i in range (p.getNumJoints(car)):
	print (p.getJointInfo(car,i))

inactive_wheels = []
power_wheels = []
steer_wheels = []
for i in range(p.getNumJoints(car)):
	for field in [str(x) for x in p.getJointInfo(car, i)]:
		#if all(x in field for x in ['front', 'wheel']) 
		if all(x in field for x in ['steer', 'hinge']):
			steer_wheels.append(i)
			break
		elif all(x in field for x in ['back', 'wheel']) or all(x in field for x in ['rear', 'wheel']):
                        power_wheels.append(i)
			break
print 'power_wheels', power_wheels
print 'steer_wheels', steer_wheels
 


for wheel in inactive_wheels:
		p.setJointMotorControl2(car,wheel,p.VELOCITY_CONTROL,targetVelocity=0,force=0)
	
steering = [4,6]

targetVelocitySlider = p.addUserDebugParameter("wheelVelocity",-10,10,0)
maxForceSlider = p.addUserDebugParameter("maxForce",0,10,10)
steeringSlider = p.addUserDebugParameter("steering",-0.5,0.5,0)
while (True):
	maxForce = p.readUserDebugParameter(maxForceSlider)
	targetVelocity = p.readUserDebugParameter(targetVelocitySlider)
	steeringAngle = p.readUserDebugParameter(steeringSlider)
	#print(targetVelocity)
	
	for wheel in power_wheels:
		p.setJointMotorControl2(car,wheel,p.VELOCITY_CONTROL,targetVelocity=targetVelocity,force=maxForce)
		
	for steer in steer_wheels:
		p.setJointMotorControl2(car,steer,p.POSITION_CONTROL,targetPosition=steeringAngle)
		
	steering
	if (useRealTimeSim==0):
		p.stepSimulation()
	time.sleep(0.01)
