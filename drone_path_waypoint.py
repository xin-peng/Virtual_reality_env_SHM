
import math
import rospy
import airsim
import numpy  as np


def main():
	# connect the simulator
	with open('airsim_pose_control.txt') as f:
		lines = f.readlines()
	client = airsim.MultirotorClient()
	client.confirmConnection()
	client.enableApiControl(True)
	client.armDisarm(True)
	client.takeoffAsync().join()
	velocity = 1
	# up
	client.moveToPositionAsync(0, 0, -6, velocity).join()
	# backward
	client.moveToPositionAsync(-2, 0, -6, velocity).join()
	# left
	client.moveToPositionAsync(-2, -5, -6, velocity).join()
	# right
	client.moveToPositionAsync(-2, 5, -6, velocity).join()
	# forward
	client.moveToPositionAsync(0, 5, -6, velocity).join()
	# turn raw angle for 30 degrees
	client.rotateToYawAsync(-30,5,1).join()
	client.landAsync().join()
	print(5)
	client.armDisarm(False)

	# that's enough fun for now. let's quit cleanly
	client.enableApiControl(False)


if __name__ == "__main__":
	main()