# A Virtual Reality Environment for Developing and Testing Autonomous UAV-based Structural Inspection
## Unreal Engine, AirSim, ROS, SLAM

This documentation is an instruction to help users to create a virtual reality environment for developing and testing autonomous UAV-based structural inspection algorithm. The full instruction including examples and demoes will be post after EWSHM2022. https://www.ewshm2022.com/
## Related paper
A Virtual Reality Environment for Developing and Testing Autonomous UAV-based Structural Inspection, X. Peng, G. Su, Z. Chen, R. Sengupta, EWSHM 2022.
## Dependencies
- ROS
- Unreal Engine (Version 4.25)
- AirSim
- Direct Sparse Odometry
- HDL Graph SLAM

## Installation
### Unreal Engine
https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Linux/BeginnerLinuxDeveloper/SettingUpAnUnrealWorkflow/
Please make sure you are installing with branch 4.25.
### AirSim
- Build AirSim
```sh
git clone https://github.com/Microsoft/AirSim.git
cd AirSim
./setup.sh
./build.sh
```
- Enable AirSim as a plugin for Unreal Engine
1. Open a Unreal Engine project and create a C++ class.
2. Close the project and change the project file xx.uproject with an editor, including adding "AdditionalDependencies": ["AirSim"] to "Modules" and adding {"Name":"AirSim","Enabled":true} to "Plugins".
3. Reopen the project, changing game mode to AirSim, and click play.
- Change drone sensor types and parameter by changing Documents/AirSim/settings.json. There is one example of settings.json, which represents a drone with lidar, IMU, camera, and GPS.
- Set up the environment variables for ROS
```sh
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
- Build
```sh
cd ros
catkin build # or catkin_make
```
- Running
```sh
source devel/setup.bash
rosrun
roslaunch airsim_ros_pkgs airsim_node.launch
```
Now AirSim will publish the drone location and sensor data lively. You can run rostopic list to check the name of sensor topic. The next step is running SLAM algorithm based on it.
### DSO
One of SLAM algorithm we choose as an example is Direct Sparse Odometry(https://vision.in.tum.de/research/vslam/dso). We develop a ROS version for DSO, which forks from (https://github.com/JakobEngel/dso). One change we made is that the DSO will subscribe the image data with a topic name and publish the estimated pose and feature point as point cloud.
- Install DSO https://github.com/JakobEngel/dso
- Install our version of DSO ROS https://github.com/koufongso/dso_ros
- Start to run DSO ROS 
```sh
	rosrun dso_ros dso_live image:=[ros_image_topic] \
		calib=XXXXX/camera.txt \
		gamma=XXXXX/pcalib.txt \
		vignette=XXXXX/vignette.png \
```
### HDL Graph SLAM
 - Install hdl graph SLAM through https://github.com/koide3/hdl_graph_slam
 - Follow the instruction of use hdl_graph_slam in your system
### GPS way-point control 
To control the virtual drone flies in the Unreal Engine environment, there is a python script for setting up the predefined GPS way-point control system (drone_path_waypoint.py).
### Example
The following demo shows one example of controlling UAV in the lab and the results of DSO and HDL Graph SLAM.

https://user-images.githubusercontent.com/38301806/187311952-c8a17743-d18c-4023-8618-49a6f1faa755.MP4


